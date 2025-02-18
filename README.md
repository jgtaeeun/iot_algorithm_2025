# iot_algorithm_2025
iot 개발자 자료구조와 알고리즘(코딩테스트 포함)

### 9일차 : 2월 13일
- 자료구조와 알고리즘 소개
1. 자료구조 : 데이터를 구성하고 효율적으로 관리하는 형태
    - 자료구조 종류
        - 단순 : 정수, 실수 ,문자, 문자열
        - 선형 : 배열, 리스트, 스택, 큐
        - 비선형 : 트리, 그래프
        - 파일 : 순차, 색인, 직접

2. 알고리즘 : 문제를 해결하는 논리적인 방법, 순서
    - 알고리즘 성능
        - 빅오 표기법
            - $O(1)$ : 데이터 수에 관계없이 항상 일정한 시간이 걸리는 것
            - $O(log n)$ : 단순 for문인데 전체 중 일부만 처리하는 것
            - $O(n)$ : 단순 for문
            - $O(n log n)$ : 이중 for문인데 안쪽 for문이 전체 중 일부만 처리
            - $O(n^2)$ : 이중 for문
            - $O(n^3)$ : 삼중 for문
            - $O(2^n)$ : 팩토리얼 등등 ...

- 리스트 
    - 생성, 값할당, 인덱싱, 슬라이싱
    - 내장함수 
        - 리스트명.copy() 
        - del(리스트명[index]) , 리스트명.remove(value), 리스트명.clear()
            - remove(value)일 때, value가 리스트에 여러개라면 인덱스 작은 것부터 제거된다.
            - `리스트명.clear()하면 데이터 다 날라갈 수 있으니 리스트명 =[]으로 하기`
        - 리스트명.append(value) , 리스트명.extend([2,3]) 
- 2차원리스트
 ```python
    matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
    # 행
    matrix[2]
    # 열
    b = [i[3] for i in matrix]
 ```
- 문자열포맷팅
    - `:2d , :>3d(3자리, 오른쪽 정렬)`
    ```python
    print(f'{list2[i][j]:<3d}', end=' ')
    ```

### 10일차 : 2월 14일
- 파이썬 기초 문법
    - 리스트 컴프리헨션 [노트북](./day10/da01_list.ipynb)
        - 배수, 2차원리스트 

- 자료구조
    - 선형 리스트 [노트북](./day10/da02_linear_list.ipynb)
         - 배열이라고 가정하면, 빈공간을 만들고 shift시켜야함.
    - 단순 연결리스트 [노트북](./day10/da04_linked_list.ipynb)

### 11일차 : 2월 17일 
- 연결리스트 :  [파이썬](./day11/da01_linked_list.py)
    - 연결리스트 실습 : 주소록 [파이썬](./day11/da02_linked_list_practice.py)
    - 이중연결 리스트 : 앞에서 검색, 뒤에서 검색 용이
    - 원형 리스트 : 시작노드 변경시 오버헤드 없음 [파이썬](./day11/da02_circle_list_practice.py)
    - 파이썬 list() : 연결리스트와 유사    

- 스택 : [노트북](./day11/da03_stack.ipynb)
    - 스택 실습 : 웹사이트 방문 기록 [파이썬](./day11/da04_stack_practice.py)

- 큐 : [노트북](./day11/da04_queue.ipynb)


### 12일차 : 2월 18일 
- 백준 코딩 
    - `문자열 : 역순은 슬라이싱 [::-1] `
    - 큐 , 스택

- 큐
    - `전역변수로 선언한 변수들을 def() 함수 내에서 값을 변경해야 할 때, global을 쓴다.`
    - 스택의 peek() : stack[top]
    - 큐의 peek() : queue[front+1]

- 원형큐
    - 
    
- 이진트리
    - 포화 이진 트리 : 모든 노드의 차수가 2인 것 <img src ='https://velog.velcdn.com/images/seochan99/post/c4e0bd13-a15f-47da-aa1d-5632e7e81e94/image.png' width =300>
    - 완전 이진 트리 : <img src =https://velog.velcdn.com/images/seochan99/post/2c8de65b-062a-4632-afd8-9b28ad785f1c/image.png width =300>
    - 일반 이진 트리 :<img src =  https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCKHWl%2FbtrRY1UM8jm%2FJkAVBnpwUQOaoKuuwcV2vK%2Fimg.png width =300>
    - 편향 이진 트리 : <img src = https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FPEvrB%2FbtrR1gqqTZR%2F7w5nQZ54VJD4V2hYvkKrl1%2Fimg.png  width =300>