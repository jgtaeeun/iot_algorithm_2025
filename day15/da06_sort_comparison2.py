# 457쪽
# 이미 정렬된 줄에 끼어들기

# 버블정렬, 퀵정렬 비교결과 
# 데이터 개수>1000000
# 끼어 든 위치>915690
# 버블정렬 소요시간>     0.131초
# 퀵정렬 소요시간>     0.777초

from random import *
from time import *

def bubbleSort(ary):
    n= len(ary)
    for i in range(n-1, 0, -1) :
        changeYN = False
        for j in range(0, i) :
            if ary[j] > ary[j+1] :
                ary[j], ary[j+1]  =ary[j+1] ,ary[j]
                changeYN = True

        if not changeYN :
            break
    return ary

# 퀵정렬
def qSort(ary, start, end) :
    
    if end <= start :   return

    low = start
    high = end
    pivot = ary[(start+end)//2]

    while low<=high :
        while ary[low] < pivot :
            low += 1
        while ary[high] > pivot :
            high -= 1
        if low <= high :
            ary[low] , ary[high] = ary[high] , ary[low]
            low += 1
            high -= 1

    mid = low

    qSort(ary, start, mid-1)
    qSort(ary, mid, end)

def quickSort(ary) :
    qSort(ary, 0, len(ary)-1)


# 메인코드 부분

# 이미 정렬된 줄
tempAry = [randint(10000,99999) for _ in range(1000000)]
tempAry.sort()

# 아무곳에 끼워넣기
rndPos = randint(0,len(tempAry)-1)
print(f'데이터 개수>{len(tempAry)}')
print(f'끼어 든 위치>{rndPos}')
tempAry.insert(rndPos, tempAry[-1])

bubbleAry= tempAry[:]
quickAry = tempAry[:]


start = time()
bubbleAry = bubbleSort(bubbleAry)
end = time()
print(f'버블정렬 소요시간>{(end - start):10.3f}초')

    
start = time()
quickSort(quickAry)
end = time()
print(f'퀵정렬 소요시간>{(end - start):10.3f}초')

print()