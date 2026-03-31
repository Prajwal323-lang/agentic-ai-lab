import datetime
import re

# Input Handler
def handle_input():
    user_input = input("Enter your command: ")
    return user_input.lower()

# Decision Logic
def detect_intent(user_input):
    if "hello" in user_input or "hi" in user_input:
        return "greeting"
    
    elif "date" in user_input:
        return "date"
    
    elif "calculate" in user_input:
        return "calculation"
    
    else:
        return "unknown"

# Action Functions
def greet():
    return "Hello! How can I help you?"


def get_date():
    return str(datetime.date.today())


def calculate(user_input):
    try:
        # Extract expression after "calculate"
        expression = user_input.replace("calculate", "").strip()
        
        # Evaluate safely (basic)
        result = eval(expression)
        return f"Result: {result}"
    
    except Exception:
        return "Invalid calculation input."


def unknown():
    return "Sorry, I didn't understand that."

# Action Executor
def perform_action(intent, user_input):
    if intent == "greeting":
        return greet()
    
    elif intent == "date":
        return get_date()
    
    elif intent == "calculation":
        return calculate(user_input)
    
    else:
        return unknown()

# Main Agent Loop
def run_agent():
    while True:
        user_input = handle_input()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        intent = detect_intent(user_input)
        response = perform_action(intent, user_input)
        
        print(response)


# Run
if __name__ == "__main__":
    run_agent()