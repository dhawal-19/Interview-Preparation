import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


numbers = get_ints()
print(numbers)
hashTable = set()
target = int(input())
for number in numbers:
    if target - number in hashTable:
        print(number, target-number)
        exit()
    else:
        hashTable.add(number)
print("Not Found")



