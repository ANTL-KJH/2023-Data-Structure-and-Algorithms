"""
* Project Name : Data Structure and Algorithms HW02.1
* Program Description :
* - Find missing number
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.30      v1.0        FirstWrite
"""
import random

def main():
    n = int(input("input n : "))
    L = random.sample(range(0, n), n-1)     # gen Sample List

    for i in range(0, n):                   # find missing number
        if i not in L:
            print("{} not in List".format(i))
            break

if __name__ == "__main__":
    main()