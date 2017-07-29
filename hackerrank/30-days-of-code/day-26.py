from datetime import date

actualReturnDate = [int(ele) for ele in input().strip().split(' ')]
expectedReturnDate = [int(ele) for ele in input().strip().split(' ')]

actualDate = date(actualReturnDate[2], actualReturnDate[1], actualReturnDate[0])
expectedDate = date(expectedReturnDate[2], expectedReturnDate[1], expectedReturnDate[0])

delta = actualDate - expectedDate

if delta.days <= 0:
    print(0)
elif actualReturnDate[1] == expectedReturnDate[1] and actualReturnDate[2] == expectedReturnDate[2]:
    print(15 * (actualReturnDate[0] - expectedReturnDate[0]))
elif actualReturnDate[2] == expectedReturnDate[2]:
    print(500 * (actualReturnDate[1] - expectedReturnDate[1]))
else:
    print(10000)
