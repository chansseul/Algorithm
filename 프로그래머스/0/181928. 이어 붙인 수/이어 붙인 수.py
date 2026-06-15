def solution(num):
    a = b = ''
    for n in num:
        if n%2 == 0:
            a += str(n)
        else:
            b += str(n)
    return int(a) + int(b)