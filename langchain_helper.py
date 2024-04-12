import streamlit as st
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv
import os


load_dotenv()

hugginface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.5, token=hugginface_api_key)

def generate_pet_name(animal_type, pet_color):

    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type','pet_color'],
        template = f"I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me ten cool names for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})


    return response

def langchain_agent():

    tools=load_tools(["wikipedia", "llm-math"], llm=llm)

    agent =initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run("What is the average age of a dog? Multiply the age by 3")

    print(result)


if __name__ == "__main__":
    #print(generate_pet_name("Dog", "Black"))
    langchain_agent()
