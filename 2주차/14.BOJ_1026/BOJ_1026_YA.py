n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
print(sum([a * b for a, b in zip(A, B)]))
