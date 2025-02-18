# 편의점에서 판매된 물건 목록 출력하기
import random

def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


class TreeNode():
    def __init__(self):
        self.data =None
        self.right=None
        self.left=None

memory =[]
root =None
dataAry = ['바나나맛우유','레쓰비캔커피','츄파춥스','도시락','삼다수','코카콜라','삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]

print(f'오늘 판매된 물건(중복O) -> {sellAry}')

node =TreeNode()
node.data = sellAry[0]
root = node
memory.append(root)

for name in sellAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True: 
        if name ==current.data :
            break
        elif name < current.data :
            if current.left == None :
                current.left = node 
                memory.append(node)
                break
            else :
                current = current.left
        else :
            if current.right == None :
                current.right = node 
                memory.append(node)
                break
            else :
                current = current.right
print('이진 탐색 트리 구성 완료')
print ('오늘 판매된 종류(중복x) ->')
preorder(root)
