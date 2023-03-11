n, p = map(int, input().split())
l = []
a = n # 초기 값 설정
while True:
    r = (a*n) % p
    if r in l: # 이미 나온 값이라면
        print(len(l) - l.index(r))
        break
    l.append(r) # 노드 값 갱신
    a = r # 나머지로 갱신