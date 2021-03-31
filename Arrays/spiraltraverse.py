import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

if __name__ == '__main__':
    array = get_ints()
    print(array)