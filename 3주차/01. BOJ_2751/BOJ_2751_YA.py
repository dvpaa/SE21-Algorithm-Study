import sys

input = sys.stdin.readline
N = int(input())
num = sorted(list(int(input().rstrip()) for _ in range(N)))
print(*num, sep='\n')
