from math import gcd

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        # 두 수의 최소공배수 = (a * b) // 최대공약수
        answer = (answer * arr[i]) // gcd(answer, arr[i])
    return answer