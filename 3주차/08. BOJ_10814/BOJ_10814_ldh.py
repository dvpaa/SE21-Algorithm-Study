import sys
input = sys.stdin.readline

n = int(input())
member = []

for i in range(n):
    [tel, name] = map(str, input().split())
    tel = int(tel)
    member.append([tel, name])

member.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(member[i][0], member[i][1])