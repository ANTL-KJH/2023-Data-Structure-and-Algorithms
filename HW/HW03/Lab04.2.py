"""
* Project Name : Data Structure and Algorithms Lab04.2
* Program Description :
* - magic square
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.04.04      v1.0        FirstWrite
"""


def main():
    n = int(input("n을 입력하시오:"))
    M = [[0] * n for _ in range(n)]
    x, y = 0, n // 2
    for value in range(1, n ** 2 + 1):
        M[x][y] = value
        x -= 1
        y -= 1
        if x < 0:
            x = n - 1
        if y < 0:
            y = n - 1
        if


if __name__ == "__main__":
    main()
