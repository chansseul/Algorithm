def solution(s):
    ans = []
    words = s.split(' ')
    
    for word in words:
        ans.append(word.capitalize())
    
    return ' '.join(ans)