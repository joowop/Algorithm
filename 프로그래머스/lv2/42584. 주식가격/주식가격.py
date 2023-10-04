from collections import deque
# testcase : [3, 1, 2, 2, 3, 1] -> [1, 4, 3, 2, 1, 0]
def solution(prices):
    answer = []
    cnt = 0
    q = deque(prices)
    for _ in range(len(prices)):
        qpop = q.popleft()

        for i in q:
            if qpop <= i:
                cnt += 1
            else:
                cnt += 1
                break
        if cnt != 0:
            answer.append(cnt)
        else:
            answer.append(1)

        cnt = 0
    answer[-1] = 0
    return answer