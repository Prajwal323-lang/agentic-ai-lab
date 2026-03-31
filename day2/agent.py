from tools import calculator, weather, summarize


# -----------------------------
# Input Handler
# -----------------------------
def handle_input():
    return input("Enter your command: ").lower()


# -----------------------------
# Decision Logic (Tool Selection)
# -----------------------------
def select_tool(user_input):
    if "calculate" in user_input:
        return "calculator"
    
    elif "weather" in user_input:
        return "weather"
    
    elif "summarize" in user_input:
        return "summarizer"
    
    else:
        return "unknown"


# -----------------------------
# Tool Executor
# -----------------------------
def execute_tool(tool, user_input):
    if tool == "calculator":
        expression = user_input.replace("calculate", "").strip()
        return calculator(expression)
    
    elif tool == "weather":
        return weather("pune")  # mock city
    
    elif tool == "summarizer":
        text = user_input.replace("summarize", "").strip()
        return summarize(text)
    
    else:
        return "Sorry, I don't understand."


# -----------------------------
# Main Agent Loop
# -----------------------------
def run_agent():
    while True:
        user_input = handle_input()

        if user_input == "exit":
            print("Goodbye!")
            break

        tool = select_tool(user_input)
        response = execute_tool(tool, user_input)

        print(response)


if __name__ == "__main__":
    run_agent()