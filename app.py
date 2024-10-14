import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGOSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

import os
from dotenv import load_dotenv

# Used the inbuild tools of Arxiv
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
# Making the Arxiv tool with name arxiv
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)



# Used the inbuild tools of wikipedia
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
# Making the wikipedia tool with name wiki
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

search = DuckDuckGOSearchRun(name = "Search")

st.title("Langchain - Chat With Search")
"""
In This exaple, we're using `StreamlitCallbackHandler` to display the thoughts and actions
Try more Langchain Streamlit AGent example at [github.com/langchain-ai/]
"""
## Sidebar for Settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Open AI API Key :",type="password")


if "message" not in st.session_state:
    st.session_state['messgaes'] = [
            {
                "role":"assistant",
                "content":"Hi, I'm a chatbot who can search the web. How can I help you?"
            }
        ]
for msg in st.session_state.message:
    st.chat_message(msg['role'].write(msg['content']))

if prompt:=st.chat_input(placeholder = "what is machine Learning?"):
    st.session_state.message.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    llm = ChatGroq(groq_api_key = api_key, model_name = "Llama3-8b-8192", streaming = True)

    tools = [search, arxiv,wiki]

    search_agent = initialize_agent(tools,llm,agents =AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors= True)

    

