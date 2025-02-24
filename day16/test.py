# def preorder(root) :
#         if root == None :
#               return
#         print(root.data , end=' ')
#         preorder(root.left)
#         preorder(root.right)
#         print()
# class TreeNode():
#     def __init__(self):
#         self.right = None
#         self.left = None
#         self.data = None
# items =['콘말차', '삿포로 맥주', '아카페라 벤티 헤이즐넛', '레어치즈푸딩', '척오리지널 메가 사워', '요아정 요거트컵', '페퍼로니피자주먹밥', '널담 슈톨렌', 
#         '딸기마시멜로케이크', '버니공쥬 딸기뚱카롱', '고추잡채호빵, 체다 슈크림붕어스낵']
# count = 0
# while True :
       
        
#         select = input('등록|종료>')
#         if select == '종료':
#                break

#         item = input('사용자 구매 물품 >').split('|')
#         for i in range(len(item)):
#             if count == 0 :
#                     node = TreeNode()
#                     node.data = item[i]
#                     root = node
#                     count += 1
                        

#             else :
#                     node = TreeNode()
#                     node.data = item[i]
#                     curr = root
#                     while True :
#                             if node.data == curr.data :   # 중복
#                                     break
#                             elif node.data > curr.data:   #오른쪽자식
#                                     if curr.right == None :
#                                             curr.right = node
#                                             break
#                                     else : 
#                                             curr = curr.right
#                             else :                          #오른쪽자식
#                                     if curr.left == None :
#                                             curr.left = node
#                                             break
#                                     else :
#                                             curr = curr.left
#         preorder(root)     
             

import random


def binSearch(ary, data):
    pos = -1
    start =0
    end = len(ary)-1
    count = 0

    while (start <=end):
        count +=1
        mid = (start +end) //2
        if data == ary[mid]:
            return mid, count
        elif data > ary[mid]:
            start = mid +1
        else :
            end = mid -1
    return pos, count

dataAry = [random.randint(0,100000) for _ in range(100000)]
findData = random.choice(dataAry)
pos, count = binSearch(dataAry, findData)
print(f'배열일부->{dataAry[:5]} ~~~{dataAry[-1:-6:-1]}')
print(f'{findData}는 {pos} 위치에 있음')
print(f'##{count}회 검색함')