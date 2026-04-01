def extract_numbers(text):
    import re
    return list(map(int, re.findall(r'\d+', text)))


def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def summarize_result(avg):
    return f"The average is {avg}, which represents the central value."

def multiply_numbers(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def divide_number(value, divisor):
    if divisor == 0:
        return "Cannot divide by zero"
    return value / divisor