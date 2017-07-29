import math

no_of_floor = int(input().strip())

a = 1
b = 1
c = -2 * no_of_floor

sub = b ** 2 - 4 * a * c

x = (-b + math.sqrt(sub)) / 2 * a

print(math.ceil(x))
