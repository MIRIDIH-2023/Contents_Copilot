import os

from langchain import OpenAI, Wikipedia
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.agents.react.base import DocstoreExplorer

from dotenv import load_dotenv
load_dotenv()

docstore = DocstoreExplorer(Wikipedia())
tools = [
    Tool(
        name="Search",
        func=docstore.search,
        description="useful for when you need to ask with search",
    ),
    Tool(
        name="Lookup",
        func=docstore.lookup,
        description="useful for when you need to ask with lookup",
    ),
]

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.0, model_name="text-davinci-003")
main_topic = input("What is topic do you want to generate?: ")

recommend_topic = llm(f"list a table of contents of the {main_topic}")
print("How about these topics?")
print(recommend_topic)

react = initialize_agent(tools, llm, agent=AgentType.REACT_DOCSTORE, verbose=True)

_input = input("Press enter key if you don't want to change, or type your topic:\n")
if _input == "" :
    _input = main_topic

question = f"What is {_input}? explain it in one key sentence"
print(react.run(question))