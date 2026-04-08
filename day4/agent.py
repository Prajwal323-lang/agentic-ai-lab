from planner import create_plan
from tools import (
    extract_numbers,
    compute_average,
    summarize_result,
    multiply_numbers,
    divide_number
)
import re


def run_agent():
    while True:
        user_input = input("Enter your query: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Step 1: Create Plan
        plan = create_plan(user_input)
        print(f"Plan: {plan}")

        data = None

        # Step 2: Execute Steps
        for step in plan:
            if step == "extract_numbers":
                data = extract_numbers(user_input)
                print(f"Step: Extract Numbers → {data}")

            elif step == "compute_average":
                data = compute_average(data)
                print(f"Step: Compute Average → {data}")

            elif step == "multiply_numbers":
                data = multiply_numbers(data)
                print(f"Step: Multiply → {data}")

            elif step == "divide":
                # Extract divisor from input 
                match = re.search(r'divide by (\d+)', user_input.lower())
                if match:
                    divisor = int(match.group(1))
                    data = divide_number(data, divisor)
                    print(f"Step: Divide → {data}")
                else:
                    print("Step: Divide → No divisor found")

            elif step == "summarize":
                data = summarize_result(data)
                print(f"Step: Summarize → {data}")

        # Final Output
        print(f"\nFinal Output: {data}\n")


if __name__ == "__main__":
    run_agent()