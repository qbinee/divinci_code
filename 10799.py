bar_razor = list(input())
answer = 0
st = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(': # 막대기 생성
        st.append('(')

    else: # 닫힌 괄호일 경우에
        if bar_razor[i-1] == '(': # 바로 전 요소가 열린 괄호라면 즉, 레이저라면
            st.pop() 
            answer += len(st) # 남은 스택의 크기를 정답에 더한다

        else: # 쇠막대기 끝인 경우
            st.pop() 
            answer += 1 # 한개씩 더해준다

print(answer)