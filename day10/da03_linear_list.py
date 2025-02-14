# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는 게 아님!
# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악할 것!

# 전역변수
katok= []
select = -1     # -1 :통과, 1 : 추가 , 2: 삽입, 3: 삭제, 4 : 종료

def add_data(friend):
    katok.append(None)
    lenKatok=len(katok)
    katok[lenKatok-1]=friend

# 중간 데이터 삽입
def insert_data(friend, position):
    # 잘못된 인덱스를 넣었을 때 예외처리 필요   #사용자가 0번부터 입력한다고 가정
    if position <0 or position > len(katok)-1:
        print('실행할 범위를 벗어났습니다.')
        return
    
    katok.append(None)
    lenKatok=len(katok)
    for i in range(lenKatok-1, position, -1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position]=friend

# 데이터를 매개변수로 받아 삭제하기
def delete_data(friend):
    if friend not in katok :
        print('존재하지 않는 데이터입니다.')
        return
    
    position = katok.index(friend)
    lenKatok=len(katok)
    for i in range(position,lenKatok-1 ):
        katok[i]=None
        katok[i]=katok[i+1]
    del(katok[lenKatok-1])

# 위치값을 매개변수로 받아 삭제하기
def delete_data_ver2(position): #사용자는 1번부터 시작이지만, 인덱스는 0부터
    if position <1 or position -1 >= len(katok) :
        print('실행할 범위를 벗어났습니다.')
        return
    lenKatok=len(katok)
    for i in range(position-1,lenKatok-1 ):
        katok[i]=None
        katok[i]=katok[i+1]
    del(katok[lenKatok-1])

if __name__ == '__main__':

    while True :
        select = int (input('선택(1 : 추가 , 2: 삽입, 3: 삭제, 4 : 종료): '))
        
        if select == 1 :
            add_data(input('입력할 데이터: '))
            print(katok)
        elif select == 2 :
            data, pos =input('입력할 데이터|위치(0부터시작): ').split('|')
            insert_data(data, int(pos))
            print(katok)
        elif select == 3 :
            # pos =input('삭제할 데이터 위치(1부터시작): ')
            # delete_data_ver2(int(pos))
            delete_data(input('삭제할 데이터 : '))
            print(katok)
        elif select == 4 :
            break
        else :
            print('1~4 중 하나 입력하세요!')
            continue



