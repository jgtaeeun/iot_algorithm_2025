# 스택 동작확인 구현
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 


def isStackFull():
    global SIZE, stack, top

    if ( top == SIZE -1 ):  #실무에서 쓰는 스택은 거의 무제한
        return True
    else :
        return False
    
def isStackEmpty():
    global SIZE, stack, top

    if top == -1 :
        return True
    else :
        return False
    
def push(data):
    global SIZE, stack, top
    
    if isStackFull()  :
        print('스택 가득 참')
    else :
        top += 1
        stack[top] = data

def pop():
    global SIZE, stack, top

    if isStackEmpty :
        print('스택이 비었음')
        return None
    else :
        data = stack[top] 
        stack[top] =None
        top -= 1
        return data
    
def peek() :
    global SIZE, stack, top
    if isStackEmpty:
        print('스택이 비었음')
    else :
        print(stack[top])
    
if __name__ == '__main__' :
    
    while True:
        select = input('삽입(I)|추출(E)|확인(V)|종료(Q):')
        if select == 'Q' :
            break
        elif select == 'I' :
            data = input('입력데이터 -> ')
            push(data)
            print(f'스택상태\n{stack}')
        elif select == 'E' :
            print(f'추출 데이터 : {pop()}')
            print(f'스택상태\n{stack}')
        elif select == 'V' :
            print(f'확인 데이터 : {peek()}')
            print(f'스택상태\n{stack}')    
        else :
            print('입력오류')

print('스택종료')       
