import sys
from collections import Counter

n = int(input())
num = sorted([int(sys.stdin.readline()) for _ in range(n)])

counter = Counter(num).most_common(2)
# counter = {}
# for value in num:
#     if value in counter:
#         counter[value] += 1
#     else:
#         counter[value] = 1
# a = sorted([(key, value) for key, value in counter.items()], key=lambda x: x[1], reverse=True)

# print(max(counter, key=counter.get))

print(round(sum(num) / n))
print(num[n//2])
# if len(a) == 1:
#     print(a[0][0])
# else:
#     if a[0][1] == a[1][1]:
#         print(a[1][0])
#     else:
#         print(a[0][0])
if len(counter) == 1:
    print(counter[0][0])
else:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
print(num[-1] - num[0])
