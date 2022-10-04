board = input()
valid = True
X = board.split('.')
for item in X:
    if len(item) % 2 != 0:
        valid = False
if valid is True:
    board = board.replace('XXXX', 'AAAA')
    board = board.replace('XX', 'BB')
    print(board)
else:
    print(-1)
