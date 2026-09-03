def solution(progresses, speeds):
    
    answer = []
    
    while len(progresses)>0:
        
        done = []
        progresses = [x + y for x,y in zip(progresses,speeds)]
        
        if progresses[0] >= 100:
            done.append(0)
            for i in range(1,len(progresses)):
                if progresses[i]>=100:
                    done.append(i)
                else:
                    break
            answer.append(len(done))

            for d in done[::-1]:
                del progresses[d]
                del speeds[d]
    
    return answer