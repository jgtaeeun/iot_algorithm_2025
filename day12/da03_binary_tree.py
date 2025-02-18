# 초기화
memory =[]
root =None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


if __name__ == '__main__' :
    node = TreeNode()
    node.data = nameAry[0]
    root = node
    memory.append(root)

    for name in nameAry[1:] :
        node = TreeNode()
        node.data = name
        
        current = root
        while True:
            if name < current.data :
                if current.left == None:
                    current.left = node
                    break
                else :
                    current = current.left
            else :
                if current.right == None :
                    current.right = node
                    break
                else :
                    current = current.right
        memory.append(node)
    print('이진탐색 트리 구성 완료!') 

    # 이진 탐색 트리의 검색
    # findName = input('찾을 이름 입력> ')
    # current = root 
    # while True :
    #     if findName == current.data :
    #         print(f'{findName} 찾음')
    #         break
    #     elif findName < current.data :
    #             if current.left == None :
    #                 print(f'{findName} 없음')
    #                 break
    #             else :
    #                 current = current.left
    #     else :
    #             if current.right == None :
    #                 print(f'{findName} 없음')
    #                 break
    #             else :
    #                 current = current.right

    # 이진 탐색 트리의 삭제
    deleteName = input('삭제할 이름 입력>')
    current = root
    parent =None
    while True :
        if deleteName == current.data :


            # 리프노드
            if current.left == None and current.right == None :
                if parent.left == current :
                    parent.left == None
                else :
                    parent.right == None
                del(current)

            # 왼쪽으로만 자식노드가 있을 경우
            elif current.left != None and current.right == None:
                if parent.left == current :     # 부모의 왼쪽일 때
                    parent.left = current.left
                else :                          # 부모의 오른쪽일 때
                    parent.right = current.left
                del(current)

            # 오른쪽으로만 자식노드가 있을 경우
            elif current.left == None and current.right !=None : 
                if parent.left == current :     # 부모의 왼쪽일 때
                    parent.left = current.right
                else :                          # 부모의 오른쪽일 때
                    parent.right = current.right
                del(current)

            print(f'{deleteName}을 삭제함')
            break
        
        elif deleteName <current.data :
            if current.left == None :
                print(f'{deleteName} 없음')
                break
            else :
                parent = current
                current = current.left
        else :
            if current.right == None :
                print(f'{deleteName} 없음')
                break
            else :
                parent = current
                current = current.right