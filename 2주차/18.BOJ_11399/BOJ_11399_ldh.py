n = int(input())
p = list(map(int, input().split()))
p.sort()
timeSum = 0
total = 0

for i in p:
    timeSum += i
    total += timeSum

print(total)
