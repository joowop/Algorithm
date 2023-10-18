import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(heapq.heappop(scoville))
    if scoville[0] < K:
        while True:
            answer+= 1
            
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            
            heapq.heappush(scoville, s1 + (s2*2))
            
            if scoville[0] >= K:
                break
            elif len(scoville) == 1 and scoville[0] < K:
    
                return -1        
    return answer