N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

start = 1
end = M
distance = 0

for apple in apples:
    if apple < start:
        distance += (start - apple)
        start = apple
        end = apple + M - 1

    elif apple > end:
        distance += (apple - end)
        end = apple
        start = end - M + 1

print(distance)
