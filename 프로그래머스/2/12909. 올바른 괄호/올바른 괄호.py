def solution(sss):
    
    stack = 0
    
    for s in sss:
        if s=='(':
            stack += 1
        else:
            stack -= 1
        if stack<0:
            return False
        
    if not stack:
        return True
    else:
        return False