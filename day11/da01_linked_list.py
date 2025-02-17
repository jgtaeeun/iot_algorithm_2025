# 단순연결리스트

## 전역변수
memory =[]  #컴퓨터 메모리처럼 보이게 만든 변수
head , prev, curr = None, None, None
array =['예지','채령','리아','류진','유나']

class Node():
    def __init__(self, data):
        self.__data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link
        
    def getData(self):
        return self.__data
    
    def getLink(self):
        return self.__link
    
    def __str__(self):
        return self.__data
    
def printNodes(start):
    curr = start

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

def insertNode(findData, insertData):
    global memory, head, curr, prev

    # 맨 처음에 데이터 삽입
    if head.getData() == findData :
        node = Node(insertData)
        node.setLink(head)  
        head = node
        return
    
    # 중간에 데이터 삽입
    curr = head
    while curr.getLink() != None :
        prev = curr
        curr = curr.getLink()
        if curr.getData() == findData :
            node = Node(insertData)
            node.setLink(curr)
            prev.setLink(node)
            return
        
    # 마지막에 데이터 삽입
    node = Node(insertData)
    curr.setLink(node)

def deleteNode(deleteData):
    global memory, head, prev, curr 

    # 첫번째 노드 삭제
    if head.getData() == deleteData :
        curr = head
        head = head.getLink()
        del(curr)
        return
    
    curr = head
    while curr.getLink() != None :
        prev=curr
        curr = curr.getLink()
        if curr is None : return # 단순로직으로 예외처리
        if curr.getData() == deleteData :
            prev.setLink(curr.getLink())
            del(curr)
            return
    
def findNode(findData):
    global memory, head, curr, prev

    curr = head
    if curr.getData() == findData :
        return curr

    while curr.getLink() != None :
        curr = curr.getLink()
        if curr.getData() == findData :
            return curr
        
    return None
    
# 연결리시ㅡ트 생성, 삽입, 삭제 구현
if __name__ == '__main__' :
    node = Node(array[0])
    head = node
    memory.append(node)

    for name in array[1:] :
        prev = node
        node = Node(name)
        prev.setLink(node)
        memory.append(node)

    printNodes(head)

    # 데이터 삽입 구현
    insertNode('예지', '믿지')
    printNodes(head)

    insertNode('리아', 'jyp')
    printNodes(head)

    insertNode(' ', '있지')  
    printNodes(head)

    # 데이터 삭제 구현
    deleteNode('믿지')
    printNodes(head)

    deleteNode('jyp')
    printNodes(head)

    deleteNode('있지')
    printNodes(head)

    print(findNode('채령'))