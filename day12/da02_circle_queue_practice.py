# 콜센터 응답 대기 시간 계산하기
# 원형 큐 

def isFull():
    global SIZE, rear, front, queue
    if (rear+1) % SIZE == front:
        return True
    else :
        return False
def isEmpty():
    global SIZE, rear, front, queue
    if rear == front :
        return  True
    else :
        return False
    
def enQueue(data):
    global SIZE, rear, front, queue
   
    if isFull():
        
        return False
    else :
        rear = (rear+1) % SIZE
        queue[rear] = data
        return True
       
def deQueue():
    global SIZE, rear, front, queue
    if isEmpty():
        print('empty')
        return None
    
    else :
        front = (front+1) % SIZE
        data =queue[front]
        queue[front]= None
        return data

def timeDelay():
    global SIZE, rear, front, queue
    time = 0
    for i in range((front+1)%SIZE, (rear+1)%SIZE):
        time += int(queue[i][1])
    return time

SIZE = int(input('큐 크기 입력> '))
rear = front = 0
queue = [None for _ in range(SIZE)]

if __name__ == '__main__':
    print('콜센터 응답 대기 시간 계산 프로그램 시작')

    for _ in range(SIZE-1):
       
        print(f'귀하의 대기 예상시간은 {timeDelay()}분입니다.')
        print(f'현재 대기줄 -> {queue}')
        enQueue(input().split()) 
    
   
    print(f'최종 대기줄 -> {queue}')
        
    print('프로그램 종료')