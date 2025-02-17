
memory =[]
head, curr, prev = None, None, None

class Info():
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def __str__(self):
        return f'[{self.__name},{self.__phone}] '
    
class Node():
    def __init__(self,data):
        self.__link = None
        self.__data = data

    def setLink(self, link):
        self.__link = link
    
    def getLink(self):
        return self.__link
    
    def getData(self):
        return self.__data

def addNode(data):
    global memory ,head, curr, prev 
    
    if head == None :
        node =Node(data)
        head = node
        memory.append(node)
        return
    
    node =  Node(data)
    memory.append(node)

    for i in range(len(memory)-1):
        memory[i].setLink(memory[i+1])


def  insertNode(data,loc) : 
    global memory ,head, curr, prev 

    # 맨 처음에 입력
    if head.getData().getName() == loc:
        node =Node(data)
        node.setLink(head)
        head = node
        memory.insert(0,node)
        return
    
    # 중간에 입력
    curr = head
    while curr.getLink() != None :
        prev = curr
        curr = curr.getLink()
        if curr.getData().getName()  == loc:
            node = Node(data)
            prev.setLink(node)
            node.setLink(curr)
            memory.insert(memory.index(curr),node)
            return
    
    # 마지막에 입력
    node = Node(data)
    curr.setLink(node)

def deleteNode(name):
    global memory ,head, curr, prev 
    curr = head

    if curr.getData().getName() == name :
        prev = head 
        head =curr.getLink()
        memory.remove(prev)
        del(prev)
        return

    while curr.getLink() != None :
        prev = curr
        curr = curr.getLink()
        if curr.getData().getName() == name :
            prev.setLink(curr.getLink())
            memory.remove(curr)
            del(curr)
            return 

def findNode(name):
    global memory ,head, curr, prev 
    curr = head

    if curr.getData().getName() == name :
        return curr.getData()
    
    while curr.getLink() != None :
        curr = curr.getLink()
        if curr.getData().getName() == name :
            return  curr.getData()
        
def printNode():
    curr = head

    if curr == None :
        return
    print(curr.getData() , end=' -> ')

    while(curr.getLink() != None):
        curr = curr.getLink()
        
        if curr.getLink() == None :
            print(curr.getData() , end=' ')
        else :
            print(curr.getData() , end=' -> ')

    print()  
    
def run():
    
    while True :
        print('명함 관리 프로그램')
        mode = input('등록|삽입|삭제|검색|전체보기|종료: ')

        if mode == '등록':
            name, phone = input('이름|전화번호 : ').split('|')
            info = Info(name, phone)
            addNode(info)
            print('등록완료')

        elif mode == '삽입' :
            name, phone = input('이름|전화번호 : ').split('|')
            info = Info(name, phone)
            loc = input('삽입위치: ')
            insertNode(info,loc)
            print('삽입완료')

        elif mode == '삭제' :
            name = input('삭제할 이름: ')
            deleteNode(name)
            print('삭제완료')

        elif mode == '검색':
            name = input('검색할 이름: ')
            print(findNode(name))
    
        elif mode == '전체보기':
            printNode()
        elif mode == '종료':
            break
        else :
            print('입력 키워드 범위 :등록|삭제|검색|전체보기|종료')


if __name__ == '__main__':
    run()