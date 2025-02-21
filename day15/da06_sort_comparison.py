# 453쪽 선택정렬과 퀵 정렬 성능 비교하기

import random
import time

# 선택정렬
def selectSort(ary):
    n= len(ary)
    for i in range(0, n-1) :
        minIndex = i 
        for j in range(i+1, n):
            if ary[minIndex] > ary[j]:
                minIndex = j
        ary[i] , ary[minIndex] = ary[minIndex] , ary[i]
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
countAry = [1000, 10000, 12000, 15000]

for count in countAry :
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'데이터수> {count}개')
    
    start = time.time()
    selectAry = selectSort(selectAry)
    end = time.time()
    print(f'선택정렬 소요시간>{(end - start):10.3f}초')

        
    start = time.time()
    quickSort(quickAry)
    end = time.time()
    print(f'퀵정렬 소요시간>{(end - start):10.3f}초')

    print()