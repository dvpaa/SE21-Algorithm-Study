N = int(input())
vote_1 = int(input())
vote = [int(input()) for _ in range(N - 1)]
count = 0

if N == 1:
    print(0)
else:
    while max(vote) >= vote_1:
        max_val = max(vote)
        max_idx = vote.index(max_val)
        vote_1 += 1
        vote[max_idx] -= 1
        count += 1

    print(count)
