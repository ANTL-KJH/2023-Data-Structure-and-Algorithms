"""
* Project Name : Data Structure and Algorithms HW01.2
* Program Description :
* - Find duplicate elements
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
* JH KIM            2023.03.21      v1.1        Algorithms Upgraded
"""
import random


def main():

    A = tuple(random.randint(1, 9) for i in range(0, 15))
    B = set(A)
    S = set()
    print("A = {}".format(A))
    for x in A:
        if x in B:
            B.remove(x)
        else:
            S.add(x)

    print("중복된 데이터의 집합 S = {}".format(S))

if __name__ == "__main__":
    main()
