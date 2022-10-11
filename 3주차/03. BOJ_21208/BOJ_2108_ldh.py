from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
list = []
for i in range(N):
    list.append(int(input()))

print(round(sum(list) / len(list)))

list.sort()
print(list[N // 2])

cnt = Counter(list).most_common(2)

if len(cnt) == 1:
    print(list[0])
else:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

print(max(list) - min(list))
