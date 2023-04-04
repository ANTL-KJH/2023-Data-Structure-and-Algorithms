"""
* Project Name : Data Structure and Algorithms HW02.3
* Program Description :
* - printout binary
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.30      v1.0        FirstWrite
"""
import time


def getBinary(n, lists):
    bit = n % 2
    n = n // 2
    lists.append(bit)
    if n == 0:
        return lists
    else:
        return getBinary(n, lists)


def main():
    n = int(input("input positive integer : "))
    L = []
    L = getBinary(n, L)
    L.reverse()
    print("getBinary = 0b", end="")
    for i in range(len(L)):
        print(L[i], end="")

    print("\nbin(n) = {}".format(bin(n)))


if __name__ == "__main__":
    main()
