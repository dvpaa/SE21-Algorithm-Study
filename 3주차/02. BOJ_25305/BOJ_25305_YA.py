N, K = map(int, input().split())
score = sorted(list(map(int, input().split())), reverse=True)
print(score[K-1])
