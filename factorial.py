def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = int(input("Enter a number: "))
iterative_result = factorial_iterative(number)
recursive_result = factorial_recursive(number)


print(f"Iterative factorial of {number}: {iterative_result}")
print(f"Recursive factorial of {number}: {recursive_result}")