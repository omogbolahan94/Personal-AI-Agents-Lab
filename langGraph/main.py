import nest_asyncio
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
import textwrap

# Running a nested eventloop (since python async code only allows for one "event loop" processing aynchronous events)
nest_asyncio.apply()


async_browser =  create_async_playwright_browser(headless=False) 
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()

for tool in tools:
    print(f"{tool.name}={tool}")

# tool_dict = {tool.name:tool for tool in tools}

# navigate_tool = tool_dict.get("navigate_browser")
# extract_text_tool = tool_dict.get("extract_text")

    
# await navigate_tool.arun({"url": "https://www.cnn.com"})
# text = await extract_text_tool.arun({})


# print(textwrap.fill(text))
# all_tools = tools + [tool_push]
# llm = ChatOpenAI(model="gpt-4o-mini")
# llm_with_tools = llm.bind_tools(all_tools)


# def chatbot(state: State):
#     return {"messages": [llm_with_tools.invoke(state["messages"])]}


# graph_builder = StateGraph(State)
# graph_builder.add_node("chatbot", chatbot)
# graph_builder.add_node("tools", ToolNode(tools=all_tools))
# graph_builder.add_conditional_edges( "chatbot", tools_condition, "tools")
# graph_builder.add_edge("tools", "chatbot")
# graph_builder.add_edge(START, "chatbot")

# memory = MemorySaver()
# graph = graph_builder.compile(checkpointer=memory)
# display(Image(graph.get_graph().draw_mermaid_png()))