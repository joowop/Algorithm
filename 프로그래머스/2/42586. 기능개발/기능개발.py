from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        # 현재 진도와 속도 가져오기
        p = progresses[0]
        s = speeds[0]
        
        # 필요한 일수 계산
        days = (100 - p) // s
        if (100 - p) % s != 0:
            days += 1
        
        # 첫 번째 작업 완료 후, 그 뒤의 작업도 완료되는지 확인
        count = 1
        progresses.popleft()
        speeds.popleft()
        
        while progresses and progresses[0] + speeds[0] * days >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        answer.append(count)
    
    return answer