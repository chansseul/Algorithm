def solution(s):
    center = len(s) // 2
    ans = s[center]
    if len(s)%2 == 0:
        ans = s[center-1:center+1]
    return ans