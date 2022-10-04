a = input().split('-')
answer = sum(map(int, a[0].split('+')))
del a[0]
for i in a:
    answer -= sum(map(int, i.split('+')))
print(answer)
