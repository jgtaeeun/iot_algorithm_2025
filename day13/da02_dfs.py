# 그래프 깊이 우선 탐색 - 무방향 그래프



stack = []          # 스택
visitedAry = []     # 방문기록

# 그래프 클래스
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 메인코드
G1 =Graph(4)

# A B C D - 0 1 2 3
G1.graph[0][2]=1
G1.graph[0][3]=1
G1.graph[1][2]=1
G1.graph[2][0]=1
G1.graph[2][1]=1
G1.graph[2][3]=1
G1.graph[3][0]=1
G1.graph[3][2]=1

print('---G1 무방향 그래프---')
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end='\t')
    print()

print('---DFS시작---')
# 첫번째 정점 방문
current = 0
stack.append(current)
visitedAry.append(current)

while len(stack) != 0 : # stack의 길이가 0인 것은 모든 정점을 방문했다는 것이다
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1 :
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

print('방문순서' , end='->')
for i in visitedAry :
    print(chr(i+ord('A')), end=' ')







