import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
longestPeakLength = 0
for index in range(1, len(array) - 1):
    isPeak = array[index - 1] < array[index] and array[index + 1] < array[index]
    if not isPeak:
        index += 1
        continue
    leftIndex = index - 2
    while leftIndex >= 0 and array[leftIndex] < array[leftIndex+1]:
        leftIndex -= 1
    rightIndex = index + 2
    while rightIndex < len(array) and array[rightIndex] < array[rightIndex+1]:
        rightIndex += 1
    currentPeakLength = rightIndex - leftIndex + 1
    longestPeakLength=max(currentPeakLength,longestPeakLength)
    index = rightIndex
print(longestPeakLength)



