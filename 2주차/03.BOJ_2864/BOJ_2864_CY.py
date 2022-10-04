a,b = input().split()

a_min = a.replace('6','5')
b_min = b.replace('6','5')
a_max = a.replace('5','6')
b_max = b.replace('5','6')

print(int(a_min)+int(b_min),int(a_max)+int(b_max))
