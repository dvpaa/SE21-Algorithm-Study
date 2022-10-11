from collections import Counter

N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))

cnt = Counter(N_list)

for m in M_list:
    isExist = False
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if m == N_list[mid]:
            isExist = True
            break
        elif m <= N_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if isExist:
        print(cnt[m], end=' ')
    else:
        print(0, end=' ')
