# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.


SIZE = 5
top = -1
stack = [None for _ in range(SIZE)]

def isStackFull():
    global top, stack, SIZE

    if top == SIZE -1 :
        return True
    else :
        return False
    
def isStackEmpty():
    global top, stack

    if top == -1 :
        return True
    else :
        return False
    
def push(data):
    global top, stack
    if isStackFull():
        print('stack is full')
    else :
        top += 1
        stack[top] =data

def pop():
    global top, stack
    if isStackEmpty():
        print('stack is Empty')
        
    else :
        data = stack[top]
        stack[top]= None
        top -= 1
        return data
    
def peek():
    global top, stack
    if isStackEmpty():
         print('stack is Empty')
         return None
    else :
        return stack[top]

def printStack():
    global top
    for i in range(top):
        print(stack[i])

i = int(input())
for _ in range(i):
  
        try :
            select =input()
            select, data =map(int, select.split())
        except :
             select = int(select)
        finally:

            if select == 1 :
                push(data)
            elif select == 2 :
                if isStackEmpty():
                    print(-1)
                else :
                    print(pop())

            elif select == 3 :
                print(top+1)

            elif select == 4 :
                if isStackEmpty():
                    print(1)
                else :
                    print(0)
                    
            elif select == 5 :
                if isStackEmpty():
                    print(-1)
                else :
                    print(peek())

