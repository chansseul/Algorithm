def solution(arr, divisor):
    ans = []
    for i in arr:
        if i%divisor == 0:
            ans.append(i)
    if not ans:
        ans = [-1]
    return sorted(ans)