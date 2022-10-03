N = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)

max_val = -float('inf')
for idx, val in enumerate(trees):
    max_val = max(max_val, val + idx + 1)

print(max_val + 1)
