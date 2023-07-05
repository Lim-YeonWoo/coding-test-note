'''코딩테스트 입력 받는 방법'''
# cf) 변수명을 input으로 하면 안된다. (예약어)

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
import sys
c = sys.stdin.readline().rstrip() # 123456789

print(a)
print(b)
print(x)
print(y)
print(z)
print(c)
