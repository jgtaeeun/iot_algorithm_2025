# 허니버터칩이 가장 많이 남은 편의점 찾기


# dfs
# graph()클래스, 인접행렬 할당, while문 통해 깊이 탐색


from operator import itemgetter # 튜플이나 리스트의 인덱스의 해당 아이템을 가져올 때 쓰는 모듈

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end='\t')
    for i in nameAry :
        print(f'{i[0]:>9s}', end=' ')
    print()

    for row in range(g.SIZE):
        print (f'{nameAry[row][0]:9s}', end=' ')
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>8d}' , end=' ')
        print()

G = Graph(5)
nameAry = [('GS25', 30),('CU', 60),('SEVEN11', 10) ,('MINISTOP',90),('emart24', 40),]
GS25 , CU,SEVEN11,  MINISTOP, EMART24 = 0,1,2,3,4

G.graph[GS25][CU]=1;G.graph[GS25][SEVEN11]=1
G.graph[CU][MINISTOP]=1;G.graph[CU][GS25]=1;G.graph[CU][SEVEN11]=1
G.graph[SEVEN11][CU]=1;G.graph[SEVEN11][GS25]=1;G.graph[SEVEN11][MINISTOP]=1
G.graph[MINISTOP][SEVEN11]=1;G.graph[MINISTOP][CU]=1;G.graph[MINISTOP][EMART24]=1
G.graph[EMART24][MINISTOP]=1

printGraph(G)

# 깊이 탐색
stack = []
visitAry = []

# 정점
current =0
stack.append(current)
visitAry.append(current)

maxStore  = current
maxCount = nameAry[current][1]

while len(stack) != 0 :
    next = None
    for v in range(5) :
        if G.graph[current][v] == 1 :
            if v in visitAry :
                continue
            else :
                next = v
                break
    if next != None :
        current = next
        stack.append( current)
        visitAry.append( current)

        if nameAry[current][1] > maxCount :
            maxStore = current
            maxCount = nameAry[current][1]

    else :
        current = stack.pop()

print(f'허니버터칩 최대 보유 편의점(개수):{nameAry[maxStore][0]}({maxCount})')