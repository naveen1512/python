
result = []

testcases = int(input())

for i in range(0, testcases):
    str = input()

    evenCharStr = '';
    oddCharStr = '';

    strLen = len(str)
    for index in range(0, strLen):
        if index % 2 == 0:
            evenCharStr += str[index]
        else:
            oddCharStr += str[index]

    result.append({'even':evenCharStr, 'odd':oddCharStr})

for i in range(0, testcases):
    print(result[i]['even'] + " " + result[i]['odd'])