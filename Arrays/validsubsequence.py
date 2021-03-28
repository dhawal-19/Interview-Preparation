import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


array = get_ints()
sequence = get_ints()
arrayIndex = 0
sequenceIndex = 0
while arrayIndex < len(array) and sequenceIndex < len(sequence):
    if array[arrayIndex] == sequence[sequenceIndex]:
        sequenceIndex += 1
    arrayIndex += 1
print(len(sequence) == sequenceIndex)

