# 고급 정렬 알고리즘의 응용
# 컬러 이미지를 흑백이미지로 만들기

from tkinter import *

root =Tk()
root.title ('이미지처리-평균으로 중앙값 찾기')
root.geometry('600x600')

photo = PhotoImage(file='./image/cupdog.png')

# 1차원배열로 만들기
photoAry =[]
h = photo.height() # 600
w = photo.width()  # 600
for i in range(h):
    for j in range(w):
        r, g, b = photo.get(i, j)
        value = (r+g+b) //3         # r,g,b 세 색상의 평균 = 그레이 이미지로 변환
        photoAry.append(value)

# 흑백이미지로 만들기
# 0~127은 흑, 128~255는 백으로 변환
for i in range(len(photoAry)):
    if photoAry[i] <=127 :
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