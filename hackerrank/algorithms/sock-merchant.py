n = int(input().strip())
c = [int(temp) for temp in input().strip().split(' ')]

count = {}
for temp in c:
    if temp in count:
        count[temp] += 1
    else:
        count[temp] = 1

total_sock_pairs = 0
for k,v in count.items():
    total_sock_pairs += v//2

print(total_sock_pairs)

