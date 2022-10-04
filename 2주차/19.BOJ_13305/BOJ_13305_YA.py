n = int(input())
distance = list(map(int, input().split()))
gas = list(map(int, input().split()))

p = gas[0]
cost = 0
for i in range(len(distance)):
    if gas[i] < p:
        p = gas[i]
    cost += p * distance[i]
print(cost)
