"""
* Project Name : Data Structure and Algorithms HW01.3
* Program Description :
* - Find min, max frequency in dice simulation
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import random


def main():
    diceDict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(1000):
        diceDict[random.randint(1, 6)] += 1
    maxKey = max(diceDict, key=diceDict.get)
    minKey = min(diceDict, key=diceDict.get)
    print("가장 많이 나온 번호와 빈도수 = ({},{})".format(maxKey, diceDict[maxKey]))
    print("가장 적게 나온 번호와 빈도수 = ({},{})".format(minKey, diceDict[minKey]))


if __name__ == "__main__":
    main()
