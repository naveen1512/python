"""
http://www.geeksforgeeks.org/numbers-whose-bitwise-sum-n-equal/
"""

if __name__ == '__main__':
    num = int(input().strip())
    zero_bit_counts = bin(num).count('0') - 1
    print(pow(2, zero_bit_counts))
