# 이미지처리를 정렬알고리즘으로 구현


from tkinter import *

def quickSort(arr , start, end):
    if end <= start :
        return
    
    low = start
    high = end
    pivot = arr[(low +high)//2]

    while low <= high :
        while arr[low] <pivot :
            low += 1
        while arr[high] > pivot :
            high -= 1
        if low <= high :
            arr[low] ,arr[high] = arr[high] ,arr[low]
            low +=1 
            high -=1 
    mid = low
    quickSort(arr, start, mid-1)
    quickSort(arr, mid, end)
    
    
root =Tk()
root.title ('이미지처리-퀵정렬로 중앙값 찾기')
root.geometry('600x600')

photo = PhotoImage(file='./image/cupdog.png')

# 1차원배열로 만들기
photoAry =[]
h = photo.height() # 600
w = photo.width()  # 600
for i in range(h):
    for j in range(w):
        r, g, b = photo.get(i, j)
        value = (r+g+b) //3         
        photoAry.append(value)

# 퀵정렬: 퀵정렬 중앙값을 기준으로 흑백 나누기
dataAry = photoAry[:]
quickSort(dataAry, 0, len(dataAry)-1)
midValue = dataAry[h*w //2]

for i in range(len(photoAry)):
    if photoAry[i] <=midValue:
        photoAry[i]=0
    else :
        photoAry[i]=255

pos = 0
for i in range(h):
    for j in range(w):
        r= g = b = photoAry[pos]
        pos += 1
        photo.put(f'#{r:02x}{g:02x}{b:02x}' , (i, j))

paper = Label(root, image=photo)
paper.pack(expand=1, anchor=CENTER)


root.mainloop()