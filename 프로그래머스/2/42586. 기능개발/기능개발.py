import math

def solution(progresses, speeds):
    answer = []
    
    # 1. 각 작업의 남은 일수 계산
    # (100 - 현재진도) / 속도 를 올림(ceil) 합니다.
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 2. 함께 배포될 수 있는 기능 개수 세기
    max_day = days[0]
    count = 0
    
    for day in days:
        if day <= max_day:
            # 앞의 작업보다 먼저 끝나거나 같이 끝나면 함께 배포
            count += 1
        else:
            # 앞의 작업보다 오래 걸리면, 이전까지 쌓인 기능들을 배포하고 새로 시작
            answer.append(count)
            max_day = day
            count = 1
            
    answer.append(count) # 마지막 남은 기능들 배포
    
    return answer