
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

    return memo[ROW-1][COL-1]
    
# 전역변수
ROW ,COL = 5,5
goldRoad = [ [1,4,4,2,2],
            [1,3,3,0,5],
            [1,2,4,3,0],
            [3,3,0,4,2],
            [1,3,4,5,3],
            ]
maxGold = growRich()
print(f'황금 미로에서 얻은 최대 황금개수 -> {maxGold}개')
