import random

dataArray =[]
memory =[]
head, curr, prev = None, None, None

class Node():
    def __init__(self, data):
        self.__data =data
        self.__link = None

    def setLink(self, link):
        self.__link = link

    def getLink(self):
        return self.__link 

    def getData(self):
        return  self.__data
    
    def __str__(self):
        return self.data

def addNode(data):
    global memory, head, curr , prev

    if head == None :
        node = Node(data)
        head = node
        head.setLink(head)
        memory.append(head)
        return

    curr = head

    if curr.getLink() == head :
        node = Node(data)
        head.setLink(node)
        node.setLink(head)
        memory.append(node)
        return
    
    while curr.getLink() != head:
        curr =curr.getLink()

        
    node = Node(data)
    curr.setLink(node)
    node.setLink(head)
    memory.append(node)
    
def countOddEven():
    global head
    even_count =0
    odd_count = 0

    if head is None:
        print(f'odd : { odd_count} | even : {even_count}')
        return
    
    curr = head    
    while True : 
        if (curr.getData() % 2 !=0 ):
            odd_count += 1
        else :
            even_count += 1
        curr = curr.getLink()

        if curr == head :
            break
    
    print(f'odd : { odd_count} | even : {even_count}')   

def printNode():
    global head
    curr = head

    if head is None:
        print("The list is empty.")
        return
    
    while True:
        print(curr.getData(), end=' ')
        curr = curr.getLink()
        if curr == head:  # Break when we loop back to head
            break
    print()        
    
if __name__ == '__main__' :
    for _ in range(7):
        dataArray.append(random.randint(1,100))

    for i in dataArray:
        addNode(i)

    printNode()
    countOddEven()
    
  