import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_tavily import TavilySearch
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
load_dotenv()

## Arxiv and Wikipedia tools
api_wrapper_arvix=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arx=ArxivQueryRun(api_wrapper=api_wrapper_arvix)


api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

st.title("Chatbot with Search Tool")

## Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

tavily_api_key=os.getenv("TAVILY_API_KEY")
search_options=["DuckDuckGo"]
if tavily_api_key:
    search_options.append("Tavily")
search_provider=st.sidebar.radio("Search Provider:",search_options,index=0)

if search_provider=="Tavily" and tavily_api_key:
    max_results=st.sidebar.slider("Tavily Max Results:",min_value=1,max_value=10,value=5)
    search=TavilySearch(max_results=max_results,api_key=tavily_api_key)
else:
    search=DuckDuckGoSearchRun(name="Google-Search")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi i am a chatbot who can search the web. How can i help you?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt:=st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(groq_api_key=api_key,model="meta-llama/llama-4-scout-17b-16e-instruct",streaming=True)
    tools=[search,arx,wiki]

    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_error=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)