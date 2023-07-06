'''list, tuple, dict 의 정렬 : sorted() 함수'''

'''[1] 리스트의 원소로 리스트나 튜플이 존재할 때'''
arr = [("a",2), ("b", 23), ("c", 1)]
result = sorted(arr, key=lambda x: x[1])
print(result)

'''[2] dict 정렬'''
d = {
    "a":23,
    "b":235,
    "c":39
}

# d.items()를 이용해 [1]의 경우와 동일한 형식으로 만들기
result = sorted(d.items(), key=lambda x:x[1])
print(result)
