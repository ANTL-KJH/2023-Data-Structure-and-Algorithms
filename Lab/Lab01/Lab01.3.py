"""
* Project Name : Data Structure and Algorithms Lab01.3
* Program Description :
* - distinction prime number
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import math

# Q : 양의 정수 n을 입력받은 후, 소수이면 true를, 소수가 아니면 false를 출력하라.
def main():
    n = int(input("양의 정수를 입력하세요: "))
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            print("{}은(는) 소수가 아닙니다".format(n))
            return
    print("{}은(는) 소수입니다.".format(n))


if __name__ == "__main__":
    main()
