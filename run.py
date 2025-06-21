import autogen
from autogen import ConversableAgent
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor

from dotenv import load_dotenv
import os
# import pdb; pdb.set_trace()
import task_message
from utils import get_stock_prices, plot_stock_prices
import user_inputs

load_dotenv()

stock1, stock2 = user_inputs.get_user_inputs()

config_list = {
    "model": "gpt-4.1-mini",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "cache_seed": 42,
}

## Command Line Executor

executor = LocalCommandLineCodeExecutor(
    virtual_env_context=None,
    timeout=200,
    work_dir="coding",
    functions=[get_stock_prices, plot_stock_prices],
)
# print("FORMAT FUNCTIONS FOR PROMPT: ", executor.format_functions_for_prompt())

# Prepare system message for Coder Agent
code_agent_system_msg = (
    task_message.coder_agent_default_sys_msg
    + executor.format_functions_for_prompt()
)

## Agent 1: LLM Agent
coder_agent = autogen.AssistantAgent(
    name="coder_agent",
    llm_config=config_list,
    system_message=code_agent_system_msg,
    code_execution_config=False,
    human_input_mode="NEVER"
)

## Agent 2: Non LLM Agent (Human Input)
code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
    default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'",
)

chat_result = code_executor_agent.initiate_chat(
    recipient=coder_agent,
    message=task_message.build_task_msg(stock1, stock2)
)


## get_stock_prices(stock_symbols, start_date, end_date)
## plot_stock_prices(stock_prices, filename)

