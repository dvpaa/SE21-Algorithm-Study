N = int(input())
data = list(map(int, input().split()))
next_milk = {0: 1, 1: 2, 2: 0}
pointer = 2
result = 0

for x in data:
    if x == next_milk[pointer]:
        result += 1
        pointer = (pointer + 1) % 3

print(result)
