def solution(p):
    return p.replace(p[:-4], '*'*(len(p)-4))