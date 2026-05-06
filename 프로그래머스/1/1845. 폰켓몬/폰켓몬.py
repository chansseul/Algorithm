def solution(nums):
    lst = list(nums)
    s = set(lst)
    res = min(len(lst)//2, len(s))
    return res