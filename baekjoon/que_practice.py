# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


SIZE = 5
queue = [None for _ in range(SIZE)]
rear = front = -1

def isEmptyQueue():
    global SIZE, queue, rear, front

    if rear == front :
        return 1
    else :
        return 0
    
def isFullQueue():
    global SIZE, queue, rear, front

    if rear != SIZE -1 :
        return False
    elif rear == SIZE -1 and front == -1:
        return True
    else :
        for i in range(front+1, rear):
            queue[i-1]= queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def push(data):
    global SIZE, queue, rear, front
    if isFullQueue():
        pass
    else :
        rear += 1
        queue[rear] = data

def pop():
    global SIZE, queue, rear, front
    if isEmptyQueue():
        print(-1)
    else :
        front += 1
        data = queue[front]
        queue[front] = None
        print(data)

def sizeData() :
    global SIZE, queue, rear, front
    if isEmptyQueue():
        print(0)
    else :
        print(rear+1)

def frontData():
    global SIZE, queue, rear, front
    if isEmptyQueue():
        print(-1)
    else :
        data = queue[front+1]
        print(data)

def backData():
    global SIZE, queue, rear, front
    if isEmptyQueue():
        print(-1)
    else :
        data = queue[rear]
        print(data)

if __name__ == '__main__':
    c = int(input())
    for _ in range(c):
        mode=list(input().split())
        
        
        if mode[0] == 'push':
            push(int(mode[1]))
        elif mode[0] == 'pop':
            pop()
        elif mode[0] == 'size':
            sizeData()
        elif mode[0] == 'empty':
            print(isEmptyQueue())
        elif mode[0]== 'front':
            frontData()
        elif mode[0] == 'back':
            backData()