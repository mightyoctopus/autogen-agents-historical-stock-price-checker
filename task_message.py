from datetime import datetime
import user_inputs

today = datetime.now().date()
# print(today)

coder_agent_default_sys_msg = """
You are a helpful AI assistant.
Solve tasks using your coding and language skills.
In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
    1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
    2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
Reply "TERMINATE" in the end when everything is done.
"""

def build_task_msg(stock1:str, stock2:str) -> str:
    return f"""
    Today is {today}. 
    - Create a plot showing the normalized price of the {stock1} stock and {stock2} for the last 5 years 
    with their 50 weeks moving average normalized price for each asset. 
    - Make sure the code is in markdown code block, print the normalized prices, save the figure
    to a file asset_analysis.png and implement the png file to pop up to display upon the completion of all the agentic processes. 
    - Provide all the code necessary in a single python block and in asset_analysis.py file.
    - Re-provide the code block that needs to be executed with each of your messages. 
    - If python packages are necessary to execute the code, provide a markdown 
    sh block with only the command necessary to install them and no additional comments or explanation.
    - You have to modularize code into the 2 pre-defined functions in the functions=[get_stock_prices, plot_stock_prices]
    BUT MAKE SURE to just call the function blocks of code by importing from functions.py.
    """