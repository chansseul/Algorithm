def solution(n):
    for i in range(len(n)):
        if n[i] < 0:
            return i
    return -1