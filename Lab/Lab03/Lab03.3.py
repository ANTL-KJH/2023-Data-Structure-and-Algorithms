"""
* Project Name : Data Structure and Algorithms Lab03.2
* Program Description :
* - sum of i to n's reciprocal
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""

# 리스트 A에 속한 두 원소의 합이 target이 되는 원소를 찾아보자
#

import time
import random


def findElement(A, target):
    found = False
    for x in range(len(A) - 1):
        for y in range(x + 1, len(A)):
            if (A[x] + A[y]) == target:
                print("A[{}] + A[{}] = {}".format(A[x], A[y], A[x] + A[y]))
                print("A[x] = {}, A[y] = {}".format(A[x], A[y]))
                return

    print("합이 {}인 쌍을 찾을 수 없습니다.".format(target))


def main():
    target = int(input("원하는 합을 입력하세요:"))
    A = random.sample(range(1, 1000001), 100000)
    findElement(A, target)


if __name__ == "__main__":
    main()
