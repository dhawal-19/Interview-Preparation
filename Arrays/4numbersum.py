import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
print(array)

target = int(input())

allPairSums = {}

quadruplets = []
for i in range(1,len(array)-1):
    for j in range(i+1,len(array)):
        currentSum = array[i] + array[j]
        differenceSum = target - currentSum
        if differenceSum in allPairSums:
            for pair in allPairSums[differenceSum]:
                quadruplets.append(pair+[array[i], array[j]])

    for k in range(0, i):
        currentSum = array[i] + array[k]
        if currentSum not in allPairSums:
            allPairSums[currentSum] = [[array[i], array[k]]]
        else:
            allPairSums[currentSum].append([array[i], array[k]])
print(quadruplets)

#Input
#7 6 4 -1 1 2