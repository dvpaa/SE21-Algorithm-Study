N, k = map(int, input().split())

score = list(map(int, input().split()))

score.sort()
print(score[-k])

