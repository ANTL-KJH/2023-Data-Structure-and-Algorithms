"""
* Project Name : Data Structure and Algorithms Lab01.6
* Program Description :
* - set handling
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


# Q : 문자열을 입력받아, 한 글자씩 회전시켜 모두 출력하는 프로그램을 작성하시오.
#     문자열을 입력하세요:소프트웨어
#     프트웨어소
#     트웨어소프
#     웨어소프트
#     어소프트웨
#     소프트웨어
def main():
    word = input("문자열을 입력하세요: ")
    for x in range(1, len(word) + 1):
        print(word[x:] + word[:x])


if __name__ == "__main__":
    main()
