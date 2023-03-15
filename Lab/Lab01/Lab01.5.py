"""
* Project Name : Data Structure and Algorithms Lab01.5
* Program Description :
* - Data Processing about Student Score
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


# Q : 5명의 성적을 차례대로 입력받아 리스트에 저장한 후, 아래 내용을 차례대로 수행하여라.
#     성적을 오름차순으로 정렬하여 출력
#     최고 성적과 최저 성적을 출력
#     성적의 합과 평균을 출력
#     성적이 90점 이상인 학생의 수를 출력
def main():
    l = list(map(int, input("5명의 성적을 입력하시오 : ").split()))
    l.sort()
    print("sorted Student score : {}".format(l))
    print("max Score : {}, min Score : {}".format(max(l), min(l)))
    print("sum of Score : {}".format(sum(l)))
    print("average of Score : {}".format(sum(l) / 5.0))

    count = 0
    for i in range(5):
        if l[i] >= 90:
            count += 1
    print("90점 이상인 학생의 수 : {}".format(count))


if __name__ == "__main__":
    main()
