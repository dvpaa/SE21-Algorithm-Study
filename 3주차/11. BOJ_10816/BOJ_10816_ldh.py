import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

def bs(i):
