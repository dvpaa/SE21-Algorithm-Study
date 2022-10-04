N = int(input())
SeatInform = input()
#전체 N석에서 (L석의 수//2)한 값을 뺀다.
cnt = N - SeatInform.count('L') // 2

#왼쪽이나 오른쪽 끝에 L석이 위치하면
if SeatInform[0] == 'L' or SeatInform[-1] == "L":
    cnt += 1
if len(SeatInform) % 2 == 0:
    cnt += 1

print(cnt)