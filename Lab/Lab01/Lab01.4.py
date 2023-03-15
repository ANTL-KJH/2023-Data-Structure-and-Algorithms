"""
* Project Name : Data Structure and Algorithms Lab01.4
* Program Description :
* -
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


# Q : 양의 정수 n을 입력받은 후, 1부터 n까지 역수의 합(1+1/2+1/3+...+1/n)을 구하시오
def main():
    n = int(input("양의 정수를 입력하세요: "))
    result = 0.0
    for i in range(1, n + 1):
        result += 1 / i
    print("1부터 {}까지 역수의 합 = {}".format(n, result))


if __name__ == "__main__":
    main()
