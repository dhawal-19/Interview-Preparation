import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
isNonDecreasing=True
isNonIncreasing=True
for index in range(1,len(array)):
    if array[index]<array[index-1]:
        isNonDecreasing = False
    if array[index] > array[index - 1]:
        isNonIncreasing = False
print(isNonIncreasing or isNonDecreasing)