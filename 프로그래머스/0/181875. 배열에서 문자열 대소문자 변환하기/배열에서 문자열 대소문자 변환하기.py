def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())  # 짝수 인덱스는 소문자로
        else:
            answer.append(strArr[i].upper())  # 홀수 인덱스는 대문자로
    return answer