def solution(s):
    ps = 0
    ys = 0

    for i in s:
        if i == 'p' or i == 'P':
            ps += 1
        # elif를 사용하면 조금 더 효율적입니다.
        elif i == 'y' or i == 'Y':
            ys += 1
    
    # 두 개수가 같은지만 확인 (둘 다 0인 경우도 포함됨)
    return ps == ys