from langchain_community.chat_models import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent

from app.agent.tools.product_search import product_search_tool
from app.agent.tools.finance_planing import financing_tool
from app.agent.tools.value_proposition_rag import value_prop_rag_tool
from app.agent.prompts.prompts import prompt_1 as prompt


llm = ChatOpenAI(model_name="gpt-4", temperature=0)
prompt = prompt

toolkit = [
    product_search_tool,
    financing_tool,
    value_prop_rag_tool
]

sales_agent = create_openai_tools_agent(llm, toolkit, prompt)
agent_executor = AgentExecutor(agent=sales_agent, tools=toolkit, verbose=True)
