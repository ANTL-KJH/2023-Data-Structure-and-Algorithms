"""
* Project Name : Data Structure and Algorithms Lab03.1
* Program Description :
* - Hanoi Tower
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""

# Hanoi tower 문제를 recursion으로 해결해보자.
# 입력 : 쟁반의 수 n(n은 양의 정수이며, 1 <= n <= 64)
# 출력 : 탑 A, B, C가 존쟇며 A에 저장된 n개의 쟁반을 C로 모두 이동하는 순서 출력
# 예 (n =3): A -> C , A -> B, C -> B, A -> C, B -> A, B -> C, A -> C
import time


def hanoi(n, first, second, third):
    if n == 1:
        #print("{} -> {}".format(first, third))
        return
    else:
        hanoi(n - 1, first, third, second)
        #print("{} -> {}".format(first, third))
        hanoi(n - 1, second, first, third)


def main():
    # n = int(input("쟁반의 수 n:"))
    for n in range(10, 20):
        start = time.time()
        hanoi(n, 'A', 'B', 'C')
        end = time.time()
        print("n = {}일 때, 실행 시간 = {}".format(n, end - start))
    # hanoi(n, 'A', 'B', 'C')


if __name__ == "__main__":
    main()
