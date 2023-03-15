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
    lotto = []
    while len(lotto) < 6:
        num = random.randint(1, 45)
        if num not in lotto:
            lotto.append(num)
    lotto.sort()
    print("이번 주의 로또 번호 = {}".format(lotto))
    print("이번 주의 로또 번호 = {}".format(sorted(random.sample(range(1, 46), 6))))


if __name__ == "__main__":
    main()
