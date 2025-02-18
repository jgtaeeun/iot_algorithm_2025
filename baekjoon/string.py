# 문자열을 입력받고 문자열의 특정 위치를 읽어 봅시다.
# s = input('영어소문자와 대문자로만 이루어진 단어: ')
# i = int(input('찾고 싶은 글자 위치: '))

# print(s[i-1])

# 문자열을 입력받고 길이를 재는 문제
# print(len(input()))

# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
# n = int(input())
# store =[]
# for _ in range(n):
#     s=input()
#     store.append((s[0], s[len(s)-1]))

# for i in store:
#     print(i[0] + i[1])

# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
# try :
#     s=input()
#     if len(s) == 1 :
#         print(ord(int(s)))
# except : 
#     print(ord(s))

# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 
# 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력한다.
# N = int(input())
# s= input()
# sum = 0
# if len(s)==N:
#     for i in s:
#         sum += int(i)
# print(sum)

# N = int(input())
# s= list(map(int,input()))
# if len(s) ==N :
#     print(sum(s))

# 알파벳 찾기
# s = input()
# idx =[-1 for i in range(26)]
# for i, v in enumerate(s):
#     if idx[ord(v)-97] == -1 :
#         idx[ord(v)-97]=i
# print(idx)
# # print(ord('a'), ord('z')) # 97 122

# s = input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in s:
#        print(s.index(i), end=' ')
#     else :
#         print(-1 , end=' ') 

# 문자열 반복
# T = int(input())
# for _ in range(T):
#     R, S = input().split()
#     R= int(R)
#     for i in  S:
#         print( i * R , end='')
#     print()   

# 단어 개수 세기
# T = list(input().split())
# print(len(T))

# 거꾸로 숫자읽어 크기 비교
A, B = input().split()
# A =int( A[2] + A[1] + A[0])
# B =int( B[2] + B[1] + B[0])
A = A [::-1]
B = B [::-1]
if A >B :
    print(A)
elif A <B :
    print(B)
else :
    print(A, B)

