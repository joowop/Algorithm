from collections import deque

def solution(s):
    rotate = len(s)
    queue = deque(s)
    answer = 0
    
    for i in range(rotate):
        if i != 0:
            sym = queue.popleft()
            queue.append(sym)
            
        stack = []
        for q in queue:
            # print("q",q)
            # print("1",stack)
            if stack:
                # print("stack 이 있을 때",stack)
                if stack[-1] == '[' and q == ']': 
                    # print("stack에 []",stack)
                    stack.pop()
                elif stack[-1] == '{' and q == '}':
                    stack.pop()
                elif stack[-1] == '(' and q == ')':
                    stack.pop()
                else:
                    # print("stack이 있지만 if 성립안할때",stack)
                    stack.append(q)
            else:
                # print("stack이 비어있을 떄",stack)
                stack.append(q)

        if len(stack) == 0:
            answer += 1

    return answer