'''코딩테스트 입력 받는 방법'''

'''
[Input]
8
10
3 5 7
12 34 56 67 56
'''
a = int(input()) # 8
b = int(input()) # 10

x, y, z = map(int, input().split()) # 3, 5, 7

array_name = list(map(int, input().split())) # [12, 34, 56, 67, 56]

print(a)
print(b)
print(x)
print(y)
print(z)
print(array_name)
