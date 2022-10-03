S = input()
S = S.replace("XXXX", "AAAA").replace("XX", "BB")

print(-1) if "X" in S else print(S)
