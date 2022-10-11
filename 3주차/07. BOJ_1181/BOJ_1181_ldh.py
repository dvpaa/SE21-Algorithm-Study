import sys
input = sys.stdin.readline

n = int(input())
word = []

for i in range(n):
    word.append(input().rstrip())

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)