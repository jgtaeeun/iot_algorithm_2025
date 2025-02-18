# 큐 자료구조 구현



def isQueueFull():
    global SIZE, queue, rear, front
    # 1. 가장 일반적 로직
    # if rear == SIZE -1 :
    #     return True
    # else :
    #     return False
    
    # 2. 개선로직
    if rear != SIZE -1 :
        return False
    elif rear == SIZE -1 and front == -1 :
        return True
    else :
        for i in range(front+1, SIZE):
            queue[i-1]=queue[i]         # front + 1  위치부터 rear위치까지 왼쪽으로 한 칸씩 이동시킨다.
            queue[i]=None
        front -= 1                      
        rear -= 1
        return False


def isQueueEmpty():
    global SIZE, queue, rear, front
    if rear == front:
        return True
    else :
        return False
    
def enQueue(data):
    global SIZE, queue, rear, front
    if isQueueFull() :
        print('Queue is full')
    else :
        rear += 1
        queue[rear] = data

def deQueue():
    global SIZE, queue, rear, front
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else :
        front += 1
        data = queue[front]
        queue[front] = None
        return data

def peek():
    global SIZE, queue, rear, front
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else :
        return queue[front+1]
    

# 초기화
SIZE = int(input('큐 크기 입력: '))
queue = [None for _ in range(SIZE)]
front = rear = -1

# 메인모듈
if __name__ == '__main__':
    # 함수선언, 초기화 후 메인모듈 실행되기에 SIZE에 대한  input()이 실행되고 print('메인시작')이 실행된다/ 다른 모듈이 메인일 경우, 함수선언과 초기화만 실행된다.
    print('메인시작!')

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