import datetime

# -----------------------------
# Tool 1: Calculator
# -----------------------------
def calculator(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid calculation."


# -----------------------------
# Tool 2: Weather (Mock)
# -----------------------------
def weather(city="your city"):
    return f"The weather in {city} is sunny (mock data)."


# -----------------------------
# Tool 3: Text Summarizer
# -----------------------------
def summarize(text):
    # Simple summarizer: return first sentence
    sentences = text.split(".")
    return sentences[0] if sentences[0] else "No summary available."