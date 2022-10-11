N = int(input())
word = sorted(list(set(input() for _ in range(N))))
word.sort(key=len)
print(*word, sep='\n')
