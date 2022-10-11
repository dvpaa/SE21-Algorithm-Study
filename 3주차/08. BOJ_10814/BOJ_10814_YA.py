N = int(input())
# member = sorted(list(list(input().split()) for _ in range(N)), key=lambda x: x[0])
member = list(list(input().split()) for _ in range(N))
for i in range(len(member)):
    member[i][0] = int(member[i][0])
member = sorted(member, key=lambda x: x[0])
for i in member:
    print(*i)
