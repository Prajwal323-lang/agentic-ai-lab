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
    #handle list input
    if isinstance(value, list):
        if len(value) == 0:
            raise ValueError("No numbers to divide")
        value = value[0]

    #handle division by zero
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")

    return value / divisor