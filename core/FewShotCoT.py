import os
import json

from langchain.prompts import PromptTemplate
from langchain import OpenAI

from dotenv import load_dotenv
load_dotenv()

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List

from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts.few_shot import FewShotPromptTemplate

from .common.utils import isEnglish
from .few_shot_example import COT_EXAMPLE

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

examples = COT_EXAMPLE

example_prompt = PromptTemplate(
  input_variables=["Instruction", "response"], template="Instruction: {Instruction}\n{response}\n",
)

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # This is the list of examples available to select from.
    examples,
    # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
    OpenAIEmbeddings(),
    # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
    Chroma,
    # This is the number of examples to produce.
    k=1
)

prompt = FewShotPromptTemplate(
    example_selector=example_selector, 
    example_prompt=example_prompt, 
    suffix="{input}", 
    input_variables=["input"]
)

class SubTopic(BaseModel):
    main_topic: str = Field(description="Main topic entered by user")
    sub_topic: List[str] = Field(description="list of specific subtopics of entered topic")
    source: str = Field(description="source used to answer the topic entered by user, should be google website url.")

class LayoutComponents(BaseModel):
    topic: str = Field(description="topic entered by user")
    contents: List[str] = Field(description="list of contents. Contents are noun phrases")
    source: str = Field(description="source used to answer the topic entered by user, should be google website url.")
    
class fewShotCoT:
  def __init__(self, model_name="text-davinci-003", creative_temperature=0.7, informatic_temperature=0.0) :
    self.creative_model = OpenAI(model_name=model_name, temperature=creative_temperature)
    self.informatic_model = OpenAI(model_name=model_name, temperature=informatic_temperature)
    
    self.topic_parser = PydanticOutputParser(pydantic_object=SubTopic)
    self.components_parser = PydanticOutputParser(pydantic_object=LayoutComponents)
    
    self.initial_prompt = PromptTemplate(
        template="{template}\n{format_instructions}\n",
        input_variables=["template"],
        partial_variables={"format_instructions": self.topic_parser.get_format_instructions()},
    )
    
    self.advanced_prompt = PromptTemplate(
        template="{delimiter}\n{format_instructions}\n",
        input_variables=["delimiter"],
        partial_variables={"format_instructions": self.components_parser.get_format_instructions()},
    )
    
  def __getInitialPromptTemplate(self, query):
    if isEnglish(query):
        template = f"""Let's work this out in a step by step way to be sure we have the right answer.\n
                      Generate a table of contents: The table contains specific topics of the {query}."""
    else:
        template = f"""'{query}'의 하위 주제를 제시해줘. 한글로 작성해줘."""
    _input = self.initial_prompt.format_prompt(template=template)
    
    return _input
  
  def __getAdvancedPromptTemplate(self, query):
    if isEnglish(query) :
      format_txt = f"Generate components to explain the {query}. The contents is noun phrase"
    else:
      format_txt = f"아래 형식을 참고해 '{query}'을 설명하는 구성요소를 출력해줘. 이때 내용은 한글로 된 명사구야."
    few_shot_template = prompt.format(input=format_txt)
    _input = self.advanced_prompt.format_prompt(delimiter="##########")
    few_shot_template += f"\n{_input.to_string()}"
    
    return few_shot_template
  
  def getContentsOfTable(self, query):
    _input = self.__getInitialPromptTemplate(query=query)
    output = self.creative_model(_input.to_string())
    out = self.topic_parser.parse(output)
    
    return out
  
  def getContents(self, query):
    _input = self.__getAdvancedPromptTemplate(query=query)
    print(_input)
    output = self.informatic_model(_input)
    out = self.components_parser.parse(output)
    
    return out