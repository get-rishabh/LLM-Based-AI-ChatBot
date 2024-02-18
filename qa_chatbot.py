#For Initializing enviornemnt variables
from dotenv import load_dotenv 
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini's model response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response.text.split(" ")

#Initialing st
st.set_page_config(page_title="Q&A Chatbot")
st.header("Q&A ChatBot Using Gemini")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input = st.text_input("input :", key="input")
submit = st.button("Chat With Bot")

if submit and input:
    #Adding User Query in Chat-History
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is:")

    message = st.empty()
    result = ""
    for chunk in chat.send_message(input, stream=True):
        result += chunk.text
        message.markdown(result + "❚ ") # Using ❚, for Adding The Typing Effect
    message.markdown(result)
    st.session_state['chat_history'].append(("Bot",result))

st.subheader("The Chat-History is:")

for role,text in st.session_state['chat_history']:
    st.write(f"*{role}: {text}")
    

