from tools import calculator, weather, summarize
from logger import log
import re

# -----------------------------
# Simulated LLM Tool Selector
# -----------------------------
def select_tool_with_llm(user_input):
    """
    Simulates LLM reasoning for tool selection.
    This mimics how an LLM would decide based on input.
    """

    user_input = user_input.lower()

    # Simulated reasoning (acts like LLM decision)
    if any(symbol in user_input for symbol in ["+", "-", "*", "/"]) or "calculate" in user_input:
        return "calculator"

    elif any(word in user_input for word in ["weather", "temperature", "forecast"]):
        return "weather"

    elif "summarize" in user_input or len(user_input.split()) > 12:
        return "summarizer"

    else:
        return "unknown"


# -----------------------------
# Tool Execution
# -----------------------------
def execute_tool(tool, user_input):
    if tool == "calculator":
        # Extract only numbers and operators
        expression = re.sub(r'[^0-9+\-*/().]', '', user_input)

        if expression == "":
            return "No valid expression found."

        return calculator(expression)

    elif tool == "weather":
        return weather("pune")  # mock city

    elif tool == "summarizer":
        text = user_input.replace("summarize", "").strip()
        return summarize(text)

    else:
        return "Sorry, I couldn't determine the appropriate tool."


# -----------------------------
# Main Agent Loop
# -----------------------------
def run_agent():
    while True:
        user_input = input("Enter your command: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Step 1: LLM decides tool
        tool = select_tool_with_llm(user_input)

        # Step 2: Execute tool
        output = execute_tool(tool, user_input)

        # Step 3: Log everything
        log(user_input, tool, output)

        # Step 4: Show result
        print(output)


# -----------------------------
# Run Agent
# -----------------------------
if __name__ == "__main__":
    run_agent()