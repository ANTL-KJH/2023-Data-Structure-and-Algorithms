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


# Q : 문장을 입력받은 다음, 각 문자에 대해 발생 빈도수를 dictionary에 저장하고 이를 출력하라. 그리고 발생 빈도수가 가장 많은 문자와 빈도수를 출력하라.
def main():
    sentence = input("문장을 입력: ")
    freq = {}
    for ch in sentence:
        freq[ch] = freq.get(ch, 0) + 1      # key가 없는 경우 default 값인 0을 return

    print("문자의 발생 빈도수 =", freq)
    max_freq = 0
    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            max_key = key

    print(f"가장 많이 나타난 문자 = {max_key} (빈도수 = {max_freq})")


if __name__ == "__main__":
    main()
