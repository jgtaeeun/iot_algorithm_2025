#415쪽 1차원 배열의 중앙값 계산
# 선택정렬

def selectionSort(ary) :
    for i in range(0,len(ary)-1) :
        minIndex = i
        for j in range(i+1, len(ary)) :
            if ary[minIndex] > ary[j] :
                minIndex = j
                
        tmp = ary[i]
        ary[i] = ary[minIndex]
        ary[minIndex] = tmp

    return ary
 
moneyAry = [7,5,11,6,9,8000,10,6,15,12]

print(f'정렬 전->{moneyAry}')
moneyAry = selectionSort(moneyAry)
print(f'정렬 후->{moneyAry}')
print(f'중앙값 - >{moneyAry[len(moneyAry)//2]}')