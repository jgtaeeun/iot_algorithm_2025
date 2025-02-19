# 최소 비용신장 트리

from operator import itemgetter # 튜플이나 리스트의 인덱스의 해당 아이템을 가져올 때 쓰는 모듈


# 전역변수
G = None
nameAry =['춘천', '서울','속초','대전','광주','부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0 , 1, 2, 3, 4, 5
SIZE =len(nameAry)

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(graph):
    print(' ', end='\t')
    for v in range(graph.SIZE):
        print(nameAry[v], end='\t')
    print()


    for i in range(graph.SIZE):
        print(nameAry[i], end='\t')
        for j in range(graph.SIZE):
            print(f'{graph.graph[i][j]:>2d}', end='\t')
        print()
    print()


# 1. 특정 정점에 그래프가 연결확인 함수
def findVertex(g, findVtx):
    stack =[]
    visitedAry =[]
    
    current = 0
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0 : # stack의 길이가 0인 것은 모든 정점을 방문했다는 것이다
        next = None
        for vertex in range(SIZE):
            if g.graph[current][vertex] != 0 :  # 가중치는 0초과이므로 
                if vertex in visitedAry :
                    continue
                else :
                    next = vertex
                    break
        
        if next != None :
            current = next
            stack.append(current)
            visitedAry.append(current)
        else : 
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else :
        return False
    
# 2. 초기화
G = Graph(SIZE)
G.graph[춘천][서울]=10;G.graph[춘천][속초]=15
G.graph[서울][춘천]=10;G.graph[서울][속초]=40;G.graph[서울][광주]=50;G.graph[서울][대전]=11
G.graph[속초][춘천]=15;G.graph[속초][서울]=40;G.graph[속초][대전]=12
G.graph[대전][속초]=12;G.graph[대전][서울]=11;G.graph[대전][광주]=20;G.graph[대전][부산]=30
G.graph[광주][서울]=50;G.graph[광주][대전]=20;G.graph[광주][부산]=25
G.graph[부산][광주]=25;G.graph[부산][대전]=30

printGraph(G)

# 3. 가중치 간선 목록
edgeAry = []
for row in range(SIZE):
    for col in range(SIZE):
        if G.graph[row][col] !=0 :  
            edgeAry.append((G.graph[row][col], row, col))   # (가중치, 도시, 도시) 튜플형태로 리스트에 append
print('간선목록=>' , end= ' ')
print(edgeAry)

# 4. 가중치별 간선 내림차순 정렬
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True) # (가중치, 도시, 도시)일 때, 가중치를 기준으로 내림차순 정렬
print('간선목록 정렬=>' , end= ' ')
print(edgeAry)

# 5. edgeAry에서 중복 간선 제거
newAry =[]
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

print('간선목록 정렬(중복제외)=>' , end= ' ')
print(newAry)

# 6 . 가중치가 높은 간선부터 제거
index = 0   # newAry를 하나씩 보기 위해
while len(newAry) > (SIZE-1 ) : # 최소 신장트리는 간선수=정점-1
    start = newAry[index][1]
    end = newAry[index][2]
    saveWeight = newAry[index][0]

    G.graph[start][end] = 0
    G.graph[end][start] = 0

    if findVertex(G, start) and findVertex(G, end) :    # 두 정점 모두 그래프와 연결되어 있다면
        del(newAry[index])
    else :
        G.graph[start][end] = saveWeight
        G.graph[end][start] = saveWeight
        index += 1
    
# 결과 출력
print('--최소비용 신장트리 결과--')
printGraph(G)










