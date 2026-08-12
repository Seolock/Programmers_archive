def solution(sizes):
    x,y = 0,0    
    for wh in sizes:
        if x<max(wh[0],wh[1]):
            x = max(wh[0],wh[1])
        if y<min(wh[0],wh[1]):
            y = min(wh[0],wh[1]) 
    return x*y