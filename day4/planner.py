def create_plan(user_input):
    user_input = user_input.lower()
    plan = []

    # extract numbers if any math operation is present
    if any(word in user_input for word in ["average", "multiply", "multiplication", "divide"]):
        plan.append("extract_numbers")

    if "average" in user_input:
        plan.append("compute_average")

    if "multiplication" in user_input or "multiply" in user_input:
        plan.append("multiply_numbers")

    if "divide" in user_input:
        plan.append("divide")

    if "summarize" in user_input:
        plan.append("summarize")

    return plan