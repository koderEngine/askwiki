# import streamlit for the app 
import streamlit as st

# Import langchain stuff 
from langchain.agents import load_tools, initialize_agent 
from langchain.llms import OpenAI

# Import apikey and set it to the environment
import os 

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')
  st.markdown("""
  ### TIP:
  1. Enter in your OPENAI Key
  2. Enter in your question
  3. Click on the button
  
  """)

def generate_response(input):
  if input:
    # Initializing the LLM and the Toolset
    llm = OpenAI(temperature=0, max_tokens=2048,openai_api_key=openai_api_key)
    tools = load_tools(["wikipedia"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    text = agent.run(input)
    st.info(text)


st.title('Request from Wikipedia')

# Collect the prompt from the user 

with st.form('my_form'):
  text = st.text_area('Enter text:', max_chars=2048)
  submitted = st.form_submit_button('Submit')
  if submitted:
    if text and openai_api_key:
      generate_response(text)
    else:
      st.caption(':red[Please enter a valid question and your OPENAI API Key]')



