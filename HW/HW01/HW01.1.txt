"""
* Project Name : Data Structure and Algorithms HW01.1
* Program Description :
* - Gen n by n matrix and printout
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


def main():
    n = int(input("1부터 10 사이의 정수를 입력하세요:"))     # n 입력
    mtrx=[]
    count = 1
    for i in range(n):                                  # mtrx 생성
        tmp = []
        for j in range(n):
            tmp.append(count)
            count += 1
        mtrx.append(tmp)

    for i in range(n):                                  # 출력
        if i % 2 == 1:
            mtrx[i].reverse()                           # ㄹ 형태 출력을 위해 list 역순으로 변경
        for j in range(n):
            print("{:2} ".format(mtrx[i][j]), end="")
        print()

if __name__ == "__main__":
    main()
