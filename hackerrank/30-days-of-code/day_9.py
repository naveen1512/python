
def factorial(number):
    if (number <= 1):
        return number
    else:
        return number * factorial(number - 1)

n = int(input().strip())

print(factorial(n))