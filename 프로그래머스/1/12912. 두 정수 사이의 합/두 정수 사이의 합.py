def solution(a, b):
    # (abs(a - b) + 1) * (a + b) // 2
    # sum(range(start, end + 1))
    answer = 0
    for i in (range(a, b+1) if a <= b else range(b, a+1)):
        answer += i
    return answer