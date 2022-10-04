n = int(input())
seat = input()

if seat.count("S") == n:
    print(seat.count("S") + seat.count("L") // 2)
else:
    print(seat.count("S") + seat.count("L") // 2 + 1)
