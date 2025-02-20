# 421쪽 성적별로 조 편성하기
# 삽입정렬
def insertSort(ary) :
    for i in range(1, len(ary)) :
        for j in range(i, 0, -1 ):
            if ary[j-1][1]  > ary[j][1] :
                tmp = ary[j]
                ary [j] = ary[j-1]
                ary [ j-1] = tmp
    return ary





scoreAry = [['선미',88],['초아',90],['화사',71],['영탁',78],['영웅',67],['민호',92]]
print(f'정렬 전->{scoreAry}')
scoreAry=insertSort(scoreAry)
print(f'정렬 후->{scoreAry}')


print(f'정렬 후 짝으로 조 이루기-> ' )
for i in range(0, len(scoreAry)//2) :
    print(f'{i+1}조 : {scoreAry[i][0]} ,{scoreAry[5-i][0]} ')
