import os
import json

from langchain.prompts import PromptTemplate
from langchain import OpenAI

from dotenv import load_dotenv
load_dotenv()

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List

from .common.utils import isEnglish

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class SubTopic(BaseModel):
    main_topic: str = Field(description="Main topic entered by user")
    sub_topic: List[str] = Field(description="list of specific subtopics of entered topic")
    source: str = Field(description="source used to answer the topic entered by user, should be google website url.")

class LayoutComponents(BaseModel):
    topic: str = Field(description="topic entered by user")
    keywords: List[str] = Field(description="list of keywords. Keywords can be composed of one or more words")
    contents: List[str] = Field(description="Contents are informative noun phrases")
    source: str = Field(description="source used to answer the topic entered by user, should be google website url.")
    
class JF_PT_Prompt:
  
  def __init__(self, model_name="text-davinci-003", creative_temperature=0.7, informatic_temperature=0.1) :
    self.creative_model = OpenAI(model_name=model_name, temperature=creative_temperature)
    self.informatic_model = OpenAI(model_name=model_name, temperature=informatic_temperature)
    
    self.topic_parser = PydanticOutputParser(pydantic_object=SubTopic)
    self.components_parser = PydanticOutputParser(pydantic_object=LayoutComponents)
    
    self.initial_prompt = PromptTemplate(
      template='''{format_instructions}\n{template}''',
      input_variables=["template"],
      partial_variables={"format_instructions": self.topic_parser.get_format_instructions()},
    )
    
    self.advanced_prompt = PromptTemplate(
      template='''{format_instructions}\n{template}''',
      input_variables=["template"],
      partial_variables={"format_instructions": self.components_parser.get_format_instructions()},
    )

  def __getInitialPromptTemplate(self, query):
    if isEnglish(query):
        template = f"""
                      Generate a table of contents: The table contains specific topics of the {query}."""
    else:
        template = f"""'{query}'의 하위 주제를 제시해줘. 한글로 작성해줘."""
    _input = self.initial_prompt.format_prompt(template=template)
    
    return _input
  
  def __getAdvancedPromptTemplate(self, query):
    if isEnglish(query):
        template = f"""
                      Generate components to explain the {query}. The contents is noun phrase."""
    else:
        template = f"""위 형식을 참고해 '{query}'을 설명하는 구성요소를 생성해줘. 이때 내용은 한글로 된 명사구야."""
    _input = self.advanced_prompt.format_prompt(template=template)
    
    return _input
    
  def getContentsOfTable(self, query):
    _input = self.__getInitialPromptTemplate(query=query)
    output = self.creative_model(_input.to_string())
    out = self.topic_parser.parse(output)
    
    return out
  
  def getContents(self, query):
    _input = self.__getAdvancedPromptTemplate(query=query)
    print(_input.to_string())
    output = self.informatic_model(_input.to_string())
    out = self.components_parser.parse(output)
    
    return out