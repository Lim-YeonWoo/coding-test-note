'''
1. sorted()
    : input은 리스트, 딕셔너리, 집합 가능
    : 정렬된 list가 return된다
'''
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(a)
print(result)

'''
2. list 내장 함수 sort()
    : return값 없고 list가 바로 정렬된다
'''
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
a.sort()
print(a)

'''
3. sort(), sorted()에 key 값 줘서 정렬기준 부여
    : key값에는 하나의 함수가 들어가야함
'''
'''[3-1] key값에 setting함수'''
a = [("a", 1000), ("b",30), ("c", 200)]

def setting(data):
    return data[1]

res = sorted(a, key = setting)
print(res)

'''[3-2] key값에 lambda 함수'''
res2 = sorted(a, key = lambda x : x[1])
print(res2)

