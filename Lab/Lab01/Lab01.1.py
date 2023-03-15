"""
* Project Name : Data Structure and Algorithms Lab01.1
* Program Description :
* - test add string, integer
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


# Q : n을 입력받고 n + nn + nnn을 계산하여 출력하라. 예를 들어, n이 20이면 nn은 2020, nnn은 202020이 된다.
def main():
    n = input("정수를 입력하세요 : ")
    nn = n + n
    nnn = n * 3
    print("n = {}, nn = {}, nnn = {}".format(n, nn, nnn))
    print("n + nn + nnn = {}".format(int(n) + int(nn) + int(nnn)))
    print(f"{n}+{nn}+{nnn} = {int(n) + int(nn) + int(nnn)}")


if __name__ == "__main__":
    main()
