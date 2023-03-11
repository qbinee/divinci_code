m, n = map(int, input().split())
x = int(input())

d = [(0, 1), (1, 0), (0, -1),(-1, 0) ] # x, y 위 오른쪽 아래 왼쪽
cx, cy = 0, 0 # 현재위치
if m*n < x: #
    print(0)
else:
    cnt = 2 # 초기값
    di = 0 # list d의 index의미
    arr = [[0] * m for _ in range(n)] # m * n 배열 초기화
    flag = 0
    arr[0][0] = 1
    while True:
        # 종료조건
        # 갈 길이 없을때 break
        # 가득 차서 네 방향 모두 갈 수 없을때
        if flag == 4:
            break

        # 이동을 할때 좌석의 범위가 넘지 않아야한다
        nx , ny = cx + d[di][0], cy + d[di][1] # 이동한 위치
        if 0<= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 0: # 티켓이 아직 할당되지 않았으면
                flag = 0
                arr[ny][nx] = cnt # 현재 위치의 값을 넣어줌
                cnt += 1 # 다음 번호 할당
                cx, cy = nx, ny # 현재 위치 변경
            else: # 가려는 방향에 사람이 있다면
                flag += 1
                di += 1
                di %= 4
        else: # 범위를 넘으려고 한다면
            # 방향을 바꿔줘야함
            flag += 1
            di += 1
            di %= 4

    for i in range(m): # x
        for j in range(n): # y
            if arr[j][i] == x:
                print(i+1, j+1)
                break



