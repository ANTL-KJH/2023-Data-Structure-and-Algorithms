"""
* Project Name : Data Structure and Algorithms Lab01.2
* Program Description :
* - find max float in 3 float
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


# Q : 세 개의 실수를 입력 받아, 가장 큰 수를 출력하라.
def main():
    #l = list(map(float, (input("세 개의 실수를 입력하시오 : ").split())))
    #print("max value : {}".format(max(l)))
    x, y, z = input("세 개의 실수를 입력:").split()
    x, y, z = float(x), float(y), float(z)
    if x>y:
        if x>z:
            print("가장 큰 수 =", x)
        else:
            print("가장 큰 수 =", z)
    else:
        if y >z:
            print("가장 큰 수 =", y)
        else:
            print("가장 큰 수 =", z)

if __name__ == "__main__":
    main()
