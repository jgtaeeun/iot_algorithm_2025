from tkinter import *

root = Tk()

# 윈도우창을 다 덮음->그림을 그리기 위해서
canvas = Canvas(root, width= 1000, height= 1000 , bg = 'white')
canvas.pack()

# 캔버스 생성 이후

# #1. 기본 원그리기
# cx = 1000 // 2  # 1000픽셀의 캔버스에서 x축 중앙 (500)
# cy = 1000 // 2  # 1000픽셀의 캔버스에서 y축 중앙 (500)
# r = 400         # 원의 반지름
# #create_oval()은 tkinter의 Canvas 위젯에서 원을 그릴 때 사용하는 메서드
# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red' )

# 전역변수
count =0
wSize =1000
radius = 400
# 2. 프랙탈 원그리기 재귀 함수

def drawCircle(x, y, r) :
    global count
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.create_text(x, y-r, text=str(count), font = ('',30))

    if r >= radius/2 :          # 아직 매개변수로 받는 반지름이 기본사이즈보다 크면
        drawCircle(x-r//2 , y, r//2)    # 중심의 왼쪽
        drawCircle(x+r//2, y, r//2)     # 중심의 오른쪽

drawCircle(wSize//2, wSize//2, radius)




root.mainloop()