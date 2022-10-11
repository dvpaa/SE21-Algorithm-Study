import sys

input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))


def bs(i):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr1[mid] == i:
            return True
        if i < arr1[mid]:
            right = mid - 1
        elif i > arr1[mid]:
            left = mid + 1


for i in range(m):
    if bs(arr2[i]):
        print(1)
    else:
        print(0)
