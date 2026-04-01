def create_plan(user_input):
    user_input = user_input.lower()
    plan = []

    if "average" in user_input:
        plan.extend(["extract_numbers", "compute_average"])

    elif "multiplication" in user_input or "multiply" in user_input:
        plan.extend(["extract_numbers", "multiply_numbers"])

    # Handle division AFTER multiplication
    if "divide" in user_input:
        plan.append("divide")

    if "summarize" in user_input:
        plan.append("summarize")

    return plan