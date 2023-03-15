"""
* Project Name : Data Structure and Algorithms Lab01.6
* Program Description :
* - lotto number sampling
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import random


# Q : 로또 번호 생성기 구현
def main():
    S = set(random.sample(range(1, 21), 10))
    T = set(random.sample(range(1, 21), 10))
    print(S, T)
    print("교집합 = {}".format(S & T))
    print("합집합 = {}".format(S | T))
    print("차집합 = {}".format(S - T))


if __name__ == "__main__":
    main()
