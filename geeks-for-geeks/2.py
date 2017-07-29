# http://www.geeksforgeeks.org/amazon-interview-experience-set-333-internship/
#
# Question 1

def extractMaxInt(str):
    maxNum = '-1'
    currMax = '0'
    for c in str:
        if c.isdigit():
            currMax += c
        elif int(maxNum) < int(currMax):
            maxNum = currMax
            currMax = '0'
        else:
            currMax = '0'

    return  maxNum


if __name__ == '__main__':
    str = input().strip();
    print(extractMaxInt(str))