# Author : Shivam Goel

def isPrime(n):
    # corner case
    if n <= 1:
        return False

    # Check from 2 to n
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def checkPrime(n):
    for i in range (2, n + 1):
        if isPrime(i):
            print(i, end = " ")


if __name__ == '__main__':
    n = input("Enter the value of N")
    q = int (n)
    checkPrime (q)