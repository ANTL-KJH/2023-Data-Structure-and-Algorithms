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

# 1부터 n까지의 역수를 더하는 함수를 작성해보자
# 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
import time


def rsum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + rsum(n - 1)


def main():
    n = int(input("n:"))
    print(rsum(n))


if __name__ == "__main__":
    main()
