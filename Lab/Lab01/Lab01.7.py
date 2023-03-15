"""
* Project Name : Data Structure and Algorithms Lab01.7
* Program Description :
* - lotto number sampling
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


# Q : 사용자로부터 문장을 입력받은 다음, split()을 수행하고 그 결과를 words 튜플에 저장한다.
#     문장의 단어수를 출력하라. 세번째로 입력된 단어를 출력하라. 단어들을 정렬하여 출력하라.
def main():
    words = tuple(input("문장을 입력하세요: ").split())
    print("문장의 단어수 =", len(words))
    print("세번째로 입력된 단어 =", words[2])
    print("단어들을 정렬하여 출력:", sorted(words))


if __name__ == "__main__":
    main()
