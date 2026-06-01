def solution(my_string, s, e):
    # s부터 e까지의 구간을 뒤집어서 슬라이싱합니다. (e번째 인덱스까지 포함해야 하므로 e+1)
    reversed_part = my_string[s:e+1][::-1]
    
    # 처음부터 s 전까지 + 뒤집은 부분 + e 이후부터 끝까지 결합
    return my_string[:s] + reversed_part + my_string[e+1:]