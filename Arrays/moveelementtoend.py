import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
target = int(input())

i = 0
j = len(array)-1
while i < j:
    while i < j and array[j] == target:
        j -= 1
    if array[i] == target:
        array[i], array[j] = array[j], array[i]
    i += 1
print(array)


# Input
# 2 1 2 2 2 3 4 2