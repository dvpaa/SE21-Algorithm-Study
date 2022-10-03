N = int(input())
data = list(map(int, input().split()))
result = 0

for i in range(N):
    if data[i] == result % 3:
        result += 1

print(result)
