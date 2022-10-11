N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for b in B:
    isExist = False
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if b == A[mid]:
            isExist = True
            break
        elif b <= A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if isExist:
        print(1)
    else:
        print(0)
