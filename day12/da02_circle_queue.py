# 원형 큐 구현

SIZE = 5
rear = front = 0
queue = [None for _ in range(SIZE)]

def isFullQueue():
    global SIZE, rear, front, queue
    if (rear +1 ) % SIZE == front :
        return True
    else :
        return False

def isEmptyQueue():
    global SIZE, rear, front, queue
    if rear == front :
        return True
    else :
        return False

def enQueue(data):
    global SIZE, rear, front, queue
    if isFullQueue():
        print('full')       

    else :
        rear = (rear+1) % SIZE
        queue[rear] = data

def deQueue():
    global SIZE, rear, front, queue
    if isEmptyQueue():
        print('empty')
        return None
    
    else :
        front = (front+1) % SIZE
        data = queue[front]
        queue[front] = None
        return data


def peek():
    global SIZE, rear, front, queue
    if isEmptyQueue():
        print('empty')
        return None
    
    else :
        data = queue[(front+1)%SIZE]
        return data

# 메인모듈
if __name__ == '__main__':
     while True:
        select = input('삽입(I)|추출(E)|확인(V)|종료(Q):').upper()

        if select == 'Q' :
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태:{queue}')

        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태:{queue}')

        elif select == 'V':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태:{queue}')
        else :
            print('입력오류')