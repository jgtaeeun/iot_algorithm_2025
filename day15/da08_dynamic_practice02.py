
def growRich():

    memo = [[0 for _ in range(5)] for _ in range(5)]
    memo[0][0] =goldRoad[0][0]
    count =  goldRoad[0][0]
   

    # 1행(인덱스 0)
    for i in range(1,ROW) :
        count += goldRoad[0][i]
        memo[0][i] = count

    # 1열(인덱스 0)
    count =  goldRoad[0][0]
    for i in range(1,COL) :
        count += goldRoad[i][0]
        memo[i][0] = count

    # 2행 2열부터 시작(1,1)
    for row in range(1,ROW):
        for col in range(1, COL):
            value1 =memo[row-1][col]
            value2 =memo[row][col-1]
            if value1 > value2 :
                memo[row][col] =  value1 + goldRoad[row][col]
            else :  
                memo[row][col] =  value2  + goldRoad[row][col]

    return memo

def printMemo(memo):
    
    for i in range(ROW):
        for j in range(COL):
            print(f'{memo[i][j]:>2d}', end=' ')
        print()
    print()
    
def printLine(memo):
    # 도착점에서 출발지로 거꾸로 감
    row, col = ROW -1 , COL -1 
    memo[row][col]= 0
    while row !=0 or col!=0 :  #출발지(0,0)은 시작점이니 
        if row-1 >=0 and col-1>=0 :
            if memo[row-1][col] > memo[row][col-1] :
                row -= 1
            else :
                col -= 1
        elif row-1 <0 and col -1 >=0 :
                col -= 1
        else :
                row -= 1
        memo[row][col]=0



# 전역변수
ROW ,COL = 5,5
goldRoad = [ [1,4,4,2,2],
            [1,3,3,0,5],
            [1,2,4,3,0],
            [3,3,0,4,2],
            [1,3,4,5,3],
            ]


memo = growRich()
value_gold = memo[ROW-1][COL-1]
print('##메모이제이션##')
printMemo(memo)

print('##메모이제이션(길표시)##')
printLine(memo)
printMemo(memo)


print(f'황금 미로에서 얻은 최대 황금개수 -> {value_gold}개')
