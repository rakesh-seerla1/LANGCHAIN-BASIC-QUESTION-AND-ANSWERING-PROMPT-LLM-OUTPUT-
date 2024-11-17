# -*- coding: utf-8 -*-
"""
Spyder Editor

####WORKINGDIRECTORY NAME:(langchainbasic)

This is a temporary script file.
"""

# Importing essential libraries 
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate # prompt
from langchain_google_genai import ChatGoogleGenerativeAI # LLM
from langchain_core.output_parsers import StrOutputParser # output parser
import traceback

# Creating LLM
google_api_key = "AIzaSyC2wwbtfXzeAOqS81zHYlGtJQcrE-KidHs"
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    max_token=None,
    temperature=0,
    timeout=None,
    max_retrieves=2, #past 2 memory saves(prompts)
    google_api_key=google_api_key
)

# ***PROMPT/TEMPLATE***

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful AI"),
        ("human", "Question: {Question}")
    ]
)

# Streamlit interface
st.title("LANGCHAIN BASIC QUESTION AND ANSWERING (PROMPT-LLM-OUTPUT)")
input_text = st.text_input("Enter your question here:")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if st.button("Execute"):
    if input_text:
        try:
            st.write("Input Text:", input_text)
            response = chain.invoke({"Question": input_text})  # Use invoke method here
            st.write("Generated Response:")
            st.write(response)
        except Exception as e:
            st.write("An error occurred:")
            st.write(e)
            st.write(traceback.format_exc())
    else:
        st.write("Please enter a question.")
