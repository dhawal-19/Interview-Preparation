import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
print(array)

minOutOfOrder = float("inf")
maxOutOfOrder = float("-inf")


def isoutoforder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


for i in range(len(array)):
    num = array[i]
    if isoutoforder(i, num, array):
        minOutOfOrder = min(minOutOfOrder, num)
        maxOutOfOrder = max(maxOutOfOrder, num)

if minOutOfOrder == float("inf"):
    print([-1, -1])
    exit(0)
subArrayLeftIdx = 0
while 0 <= subArrayLeftIdx <= len(array) - 1 and minOutOfOrder >= array[subArrayLeftIdx]:
    subArrayLeftIdx += 1
subArrayRightIdx = len(array) - 1
while 0 <= subArrayRightIdx <= len(array) - 1 and maxOutOfOrder <= array[subArrayRightIdx]:
    subArrayRightIdx -= 1
print([subArrayLeftIdx, subArrayRightIdx])



# Input
# 1 2 4 7 10 11 7 12 6 7 16 18 19