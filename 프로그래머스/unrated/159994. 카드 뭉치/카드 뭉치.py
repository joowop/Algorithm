from collections import deque
def solution(cards1, cards2, goal):
    card1 = deque(cards1)
    card2 = deque(cards2)
    answer = 'Yes'
    for i in range(len(goal)):
        if card1 and goal[i] == card1[0]:
            card1.popleft()
        elif card2 and goal[i] == card2[0]:
            card2.popleft()
        else:
            answer = 'No'
    return answer