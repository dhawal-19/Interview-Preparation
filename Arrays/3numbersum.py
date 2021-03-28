import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
array.sort()
target = int(input())
triplets = []
for index in range(len(array)-2):
    left = index+1
    right = len(array) - 1
    while left < right:
        currentSum = array[index] + array[left] + array[right]
        if currentSum == target:
            triplets.append([array[index], array[left], array[right]])
            left += 1
            right -= 1
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
print(triplets)


