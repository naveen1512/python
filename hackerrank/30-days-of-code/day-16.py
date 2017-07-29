import sys

S = input().strip()

def testException():
    try:
        print(int(S))
    except ValueError:
        print('Bad String')
        raise
    else:
        print('Else')
    finally:
        print('Finally')

if __name__ == '__main__':
    testException()