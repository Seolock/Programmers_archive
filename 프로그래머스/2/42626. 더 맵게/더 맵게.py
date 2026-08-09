import heapq

def solution(scoville, K):
    
    answer,x,y = 0,0,0
    heapq.heapify(scoville)

    while(len(scoville)>1 and scoville[0]<K):
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville,x+y*2)
        answer += 1

    if scoville[0]<K:
        answer = -1
    
    return answer