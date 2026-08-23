def solution(n, lost, reserve):
    
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
        
    reserve.sort()

    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
            
    answer = n - len(lost)
    
    return answer