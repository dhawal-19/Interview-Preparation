import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array1 = get_ints()
array2 = get_ints()
smallestDifference = sys.maxsize
currentDifference = sys.maxsize
smallestPair = []
array1.sort()
array2.sort()
idx1 = 0
idx2 = 0
while idx1 < len(array1) and idx2 < len(array2):
    firstNum = array1[idx1]
    secondNum = array2[idx2]
    if firstNum < secondNum:
        currentDifference = secondNum - firstNum
        idx1 += 1
    elif secondNum < firstNum:
        currentDifference = firstNum - secondNum
        idx2 += 1
    else:
        print(firstNum,secondNum)
        break
    if smallestDifference > currentDifference:
        smallestDifference = currentDifference
        



