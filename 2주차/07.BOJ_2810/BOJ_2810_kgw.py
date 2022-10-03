N = int(input())
seats = input()

if "LL" in seats:
    print(seats.count("S") + seats.count("LL") + 1)
else:
    print(len(seats))
