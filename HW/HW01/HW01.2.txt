"""
* Project Name : Data Structure and Algorithms HW01.2
* Program Description :
* - Find duplicate elements
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import random


def main():
    A = ()
    l = []
    S = set()
    for i in range(15):
        l.append(random.randint(1, 9))      # gen random integer
    A = tuple(l)
    print("A = {}".format(A))
    for i in range(1, 10):
        if A.count(i) > 1:
            S.add(i)
    print("중복된 데이터의 집합 S = {}".format(S))

if __name__ == "__main__":
    main()
