def solution(arr):
    ans = []
    for i in arr:
        if not ans or i != ans[-1]:
            ans.append(i)
    return ans