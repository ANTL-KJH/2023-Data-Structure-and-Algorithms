"""
* Project Name : Data Structure and Algorithms HW04.1
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
        x, y = x - 1, y - 1
        if x < 0:
            x = n - 1
        if y < 0:
            y = n - 1
        if M[x][y] != 0:
            x, y = x + 2, y + 1
            if y >= n:
                y = 0
            if x >=n:
                x -= n

    for x in range(n):          # printout
        for y in range(n):
            print("{:2} ".format(M[x][y]), end="")
        print()


if __name__ == "__main__":
    main()
