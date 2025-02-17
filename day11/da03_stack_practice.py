
# 웹 서핑에서 이전 페이지 돌아가기
import webbrowser

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


def isEmptyStack():
    global top, stack, SIZE

    if top ==-1:
        return True
    else :
        return False
    
def isFullStack():
    global top, stack, SIZE

    if top == (SIZE-1) :
        return True
    else :
        return False

def push(data):
    global stack, top
    if isFullStack() :
        print('stack is full')
    else :
        top += 1
        stack[top] = data
        print(f'스택상태:{stack}\n')
        webbrowser.open('http://'+data)

def pop():
    global stack, top
    if  isEmptyStack() :
        print('stack is Empty')
    else :
        data = stack[top]
        stack[top] = None
        top -= 1

        print(f'이전페이지:{data}\n')
        print(f'스택상태:{stack}\n')
        webbrowser.open('http://'+data)


if __name__ == '__main__' :
    
    while True:
        sel = input('웹 사이트 방문|이전 페이지>')
        if sel == '웹 사이트 방문':
            url = input('웹 사이트 url :')
            push(url)

        elif sel == '이전 페이지':
            pop()
        else :
            print('입력오류')