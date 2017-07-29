import math

def isPrime(n):
    if n == 2 or n == 3:
        return True

    squareRoot = math.ceil(math.sqrt(n))
    for i in range(2, squareRoot+1):
        if n % i == 0:
            return False

    return True


testCase = int(input().strip())
list = []

for n in range(testCase):
    list.append(int(input().strip()))

for n in list:
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")