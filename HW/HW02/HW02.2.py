"""
* Project Name : Data Structure and Algorithms HW02.2
* Program Description :
* - recursion bcoef(n, k)
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.30      v1.0        FirstWrite
"""
import time


def bcoef(n, k):
    if k == 0 or k == n:
        return 1
    return bcoef(n - 1, k - 1) + bcoef(n - 1, k)    # bcoef함수에서 두번의 bcoef함수 호출이 일어나므로 시간복잡도는 2^n


def main():
    n, k = map(int, input("input n, k:").split())
    start = time.time()     # start time check
    print(start)
    result = bcoef(n, k)
    end = time.time()       # end time check
    print(end)
    print("bcoef({}, {}) = {}, {:.10f}sec elapsed".format(n, k, result, end-start))


if __name__ == "__main__":
    main()
