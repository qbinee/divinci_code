k = int(input())
folds = input().split() # 접는순서 2n개
h = int(input())

N = 2 ** k

df = { 'D': [2,3,0,1], # d 로 인하여 펴일때 위쪽에 한개가 더 생기며 2개가 된다
       'U': [2,3,0,1],
       "R": [1,0,3,2],
       "L": [1,0,3,2]
       }

# 01 1 0  2 3
# 23 3 2

paper = [[0] * N for _ in range(N)]
fs = [(2 ** i) for i in range(k, -1, -1)] # fold step

def solve(fi, fj, si, ei, sj, ej):
    if fi == k and fj == k:
        paper[si][sj] = h
        return

    f = folds[fi+fj]
    if f == 'D': # Down인 경우 -> 상하를 나타내는 i의값을 1 늘려줌
        # 접음
        solve(fi+1, fj, (si+ei)//2 + 1, ei, sj, ej) # 3+1을 해주어 시작갑ㅅ을 재갱신
        # 재귀가 끝날때마다  = 반대로 피는것
        # 한개일때 펴지면, 한개가 늘어나고
        # 두개일 때 펴지면 두개가 늘어나서 두배씩 커지게 된다
        for i in range(fs[fi]):
            for j in range(sj, ej+1):
                paper[si+i][j] = df[f][paper[ei -i][j]]

    elif f == 'U':
        solve(fi+1, fj, si, (si+ei)//2, sj, ej)

        for i in range(fs[fi]):
            for j in range(sj, ej+1):
                paper[ei-i][j] = df[f][paper[si+i][j]]
    elif f == 'R':
        solve(fi, fj+1, si, ei, (sj+ej)//2 + 1, ej )

        for i in range(si, ei+1):
            for j in range(fs[fj]):
                paper[i][sj+j] = df[f][paper[i][ej-j]]
    else: # 옆으로 접어주는것임으로 열은 그대로고 열이 변한다, j
        solve(fi, fj+1, si, ei, sj, (sj+ej)//2)

        for i in range(si, ei+1):
            for j in range(fs[fj]):
                paper[i][ej-j] = df[f][paper[i][sj+j]]



solve(0, 0, 0, N-1, 0, N-1)

for row in paper:
    print(*row)
