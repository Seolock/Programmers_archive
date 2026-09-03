def solution(sss):
    
    stack = 0
    
    for s in sss:
        if s=='(':
            stack += 1
        else:
            stack -= 1
        if stack<0:
            return False
        
    return stack==0