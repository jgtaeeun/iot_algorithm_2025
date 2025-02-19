# 최소 비용신장 트리



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


# 특정 정점에 그래프가 연결확인 함수
def findVertex(g, findVtx):
    stack =[]
    visitedAry =[]
    
    current = 0
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0 : # stack의 길이가 0인 것은 모든 정점을 방문했다는 것이다
        next = None
        for vertex in range(SIZE):
            if g.graph[current][vertex] != 0 :
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
    
# 초기화
G = Graph(SIZE)
G.graph[춘천][서울]=10;G.graph[춘천][속초]=15
G.graph[서울][춘천]=10;G.graph[서울][속초]=40;G.graph[서울][광주]=50;G.graph[서울][대전]=11
G.graph[속초][춘천]=15;G.graph[속초][서울]=40;G.graph[속초][대전]=12
G.graph[대전][속초]=12;G.graph[대전][서울]=11;G.graph[대전][광주]=20;G.graph[대전][부산]=30
G.graph[광주][서울]=50;G.graph[광주][대전]=20;G.graph[광주][부산]=25
G.graph[부산][광주]=25;G.graph[부산][대전]=30

printGraph(G)








