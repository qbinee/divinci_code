h, m  = map(int, input().split())
add_time = int(input())
# 다 분으로 바꾸고 더한거를 시간: 분
# 날짜/ 시간
all_time = h * 60 + m + add_time # 전체를 분으로 변경
H, M = 0, 0

if all_time // 60 < 24:
    H = all_time // 60
    M = all_time % 60
else:
    all_time -= 24*60
    H = all_time // 60
    M = all_time % 60
print(H, M)
