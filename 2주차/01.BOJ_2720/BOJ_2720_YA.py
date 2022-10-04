for _ in range(int(input())):
    c = int(input())
    quarter = c // 25
    c %= 25
    dime = c // 10
    c %= 10
    nickel = c // 5
    c %= 5
    penny = (c % 5) // 1

    print(quarter, dime, nickel, penny)