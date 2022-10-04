n = int(input())
rope = sorted([int(input()) for _ in range(n)])
weight = [rope[i] * (n - i) for i in range(n)]
print(max(weight))
