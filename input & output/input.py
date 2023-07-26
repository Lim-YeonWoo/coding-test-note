'''코딩테스트 입력 받는 방법'''

'''
[Input]
8
10
3 5 7
12 34 56 67 56
123456789
'''

# 방법1
a = int(input()) # 8
b = int(input()) # 10

# 방법2
x, y, z = map(int, input().split()) # 3, 5, 7

# 방법3
array_name = list(map(int, input().split())) # [12, 34, 56, 67, 56]

# 방법4 (input()이 속도가 느리다)
'''
import sys
c = sys.stdin.readline().rstrip() # 123456789

위의 방법이 맞긴한데 귀찮으니까 아래처럼 이용
input().rstrip()이 input()하나 인 것처럼 쓰기
'''

import sys
input = sys.stdin.readline
c = input().rstrip()
d, e = input().rstrip().split()

print(a)
print(b)
print(x)
print(y)
print(z)
print(c)
