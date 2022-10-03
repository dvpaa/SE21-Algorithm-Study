S = input()
cnt = 1
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        cnt += 1
print(cnt // 2)
