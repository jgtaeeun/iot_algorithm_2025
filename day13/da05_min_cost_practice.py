# 가장 효율적인 해저 케이블망 구성하기
from operator import itemgetter 



class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
    print('', end='\t')
    for i in nameAry :
        print(i, end='\t')
    print()

    for row in range(6):
        print(nameAry[row], end='\t')
        for col in range(6):
            print(g.graph[row][col], end='\t')
        print()
    print()

def dfs(g, findValue):
    stack = []
    visitAry = []

    curr = 0
    stack.append(curr)
    visitAry.append(curr)

    while len(stack ) !=0 :
        next = None
        for v in range(6):
            if g.graph[curr][v] !=0 :
                if v in visitAry :
                    continue
                else :
                    next = v
                    break
        if next != None:
            curr = next
            stack.append(curr)
            visitAry.append(curr)

        else :
            curr = stack.pop()

    if findValue in visitAry :
        return True
    else :
        return False


nameAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울 = nameAry.index('서울')
뉴욕 = nameAry.index('뉴욕')
런던 = nameAry.index('런던')
북경 = nameAry.index('북경')
방콕 = nameAry.index('방콕')
파리 = nameAry.index('파리')

G = Graph(6)
G.graph[서울][뉴욕] = 80 
G.graph[서울][북경] =  10
G.graph[뉴욕][서울] = 80
G.graph[뉴욕][북경] = 40 
G.graph[뉴욕][방콕] = 70
G.graph[북경][방콕] = 50 
G.graph[북경][뉴욕] = 40 
G.graph[북경][서울] = 10
G.graph[방콕][뉴욕] = 70
G.graph[방콕][런던] = 30 
G.graph[방콕][북경] =50
G.graph[방콕][파리] = 20
G.graph[런던][방콕] = 30
G.graph[런던][파리] = 60
G.graph[파리][런던] = 60
G.graph[파리][방콕] = 20

print('----------원본-----------')
printGraph(G)

# 가중치 정렬-오름차순
weightList =[]
for row in range(6):
    for col in range(6):
        if G.graph[row][col] !=0 :
            weightList.append((G.graph[row][col], row, col))

weightList= sorted(weightList, key=itemgetter(0), reverse=False)
new_Ary = [weightList[i] for i in range(0, len(weightList),2)]
 
# 간선제거
index = 0
while len(new_Ary) > 5 :

    
    start = new_Ary [index][1]
    end =new_Ary [index][2]
    saveWeight = new_Ary [index][0]

    G.graph[start][end] =0
    G.graph[end][start]=0    

    if dfs(G, start) and dfs(G, end) :
        del(new_Ary[index])
    else :
        G.graph[start][end] =saveWeight
        G.graph[end][start]=saveWeight 
        index += 1
    
print('-----가장 효율적인 해저 케이블망-----')
printGraph(G)
