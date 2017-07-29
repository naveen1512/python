count = int(input().strip())
phoneBook = {}

for i in range(0, count):
    contact = input().strip().split(' ')
    phoneBook[contact[0]] = contact[1]

while True:
    name = input().strip()
    if name == '':
        break

    phoneNo = '';
    try:
        phoneNo = phoneBook[name]
        print(name + "=" + str(phoneNo))
    except KeyError as e:
        print("Not found")