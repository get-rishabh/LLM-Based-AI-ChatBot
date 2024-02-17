from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

#for initializing enviornemnt variables
# from dotenv import load_dotenv 
# load_dotenv()

import streamlit as st


#Function to load llama2 model and get response

def get_llm_response(quesion):
    llm = Ollama(model="llama2", temperature=0.5)
    response = llm.invoke(quesion)
    return response


#Initializing ST

st.set_page_config(page_title="Q&A Demo")
st.header("LLM Based Q&A ChatBot")

input = st.text_input("input :", key="input")
result = get_llm_response(input)

submit = st.button("Ask the Question")

if submit:
    st.subheader("The Response is:")
    st.write(result)