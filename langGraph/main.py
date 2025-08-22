from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from IPython.display import Image, display
import gradio as gr
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool

from pydantic import BaseModel
import random
import requests
import os
import asyncio

# using playwright
import nest_asyncio
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
import textwrap

load_dotenv()

# Running a nested eventloop (since python async code only allows for one "event loop" processing aynchronous events)
nest_asyncio.apply()

# <<<<<<<<<<<<<<<<<<<<<<< TESTING THE PLAYWRIGHT TOOL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
async_browser =  create_async_playwright_browser(headless=False) 
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
# print(tools)

# create a dictionary for each tools
tool_dict = {tool.name:tool for tool in tools}
# print(tool_dict.keys())

#  <<<<<<<<<<<<<to run the playwright tools >>>>>>>>>>>>>>>>>>>>>>>>>>
# using the tools that navigate the browser and extract text
async def playwright_tools():
    # navigate internet tool
    navigate_tool = tool_dict.get("navigate_browser")    
    await navigate_tool.arun({
        "url": "https://www.cnn.com/", 
        # "timeout": 120000,  # 60s before playwright timeout
        "wait_until": "commit"
    })  

    # extract text tool
    extract_text_tool = tool_dict.get("extract_text")
    text = await extract_text_tool.arun({})
    text = textwrap.fill(text)
    return text


# asyncio.run(playwright_tools())

# <<<<<<<<<<<<<<<<<<<<<< OTHER TOOLS >>>>>>>>>>>>>>>>>>>>>>>>
# Built-in serper tool for google web search: but ware not using it here 
# serper = GoogleSerperAPIWrapper()

# tool_search =Tool(
#         name="search",
#         func=serper.run,
#         description="Useful for when you need more information from an online search"
#     )

# customised push over app
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"


def push(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
    

# creeate a tool object for the customized push tool function   
tool_push = Tool(
    name="send_push_notification",
    func=push,
    description="useful for when you want to send a push notification"
)

# chain all the playwright tools together with push_tool: we are not using serper tool here
all_tools = tools + [tool_push]

# <<<<<<<<<<<<<<<<<<<<<< AGENT WORKFLOW >>>>>>>>>>>>>>>>>>>>>>>>
# define state
class State(TypedDict):
    messages: Annotated[list, add_messages]


# chain all tools with LLM 
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = create_react_agent(model=llm, tools=all_tools)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING THE create_react_agent >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# query = """Check online. What is the current conversion of doller to nigeria naira. Send me the notifiation of the conversion"""
# agent_chain = create_react_agent(model=llm, tools=all_tools) 
# result = asyncio.run(agent_chain.ainvoke({"messages": [{"role": "user", "content": query}]})) # the code below also works
# result = asyncio.run(agent_chain.ainvoke({"messages": [("user", query)]}))
# print(result["messages"][-1].content)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

async def chatbot(state: State):
    result = await llm_with_tools.ainvoke(state) 
    print(result)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return result  # dict of message key and and values of list of Human inout and AI response 
# .venv/Scripts/python langgraph/main.py


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=all_tools))
graph_builder.add_conditional_edges( "chatbot", tools_condition, "tools")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# set up memory
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

# configure thread
config = {"configurable": {"thread_id": "10"}}


async def chat(user_input: str, history):
    state_message = [{"role": "user", "content": user_input}]
    result = await graph.ainvoke({"messages": state_message}, config=config)
    return result["messages"][-1].content   # AI response


gr.ChatInterface(chat, type="messages").launch()