'''
[이진탐색]
    : 이미 정렬된 데이터
    : 시작점, 끝점, 중간점 idx 이용
    : 찾으려는 데이터(target)과 중간점 위치의 데이터(a[mid])를 반복적으로 비교
    : O(logN)
    : start>end면 종료. while start<=end:
'''

'''1. 재귀함수'''
def binary_search_recursive(a, target, start, end):

    #못 찾은 경우 return None
    if start > end:
        return None

    mid = (start+end)//2

    if a[mid]==target:
        return mid
    elif a[mid] > target:
        return binary_search_recursive(a, target, start, mid-1) # return해줘야함을 주의!!!
    else:
        return binary_search_recursive(a, target, mid+1, end) # return해줘야함을 주의!!!


'''2. 반복문'''
def binary_search_iter(a, target, start, end):

    while start<=end:
        mid = (start+end)//2

        if a[mid]==target:
            return mid
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None # 못찾았다면 None을 return


'''실행 결과'''
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
target2 = 4

print(binary_search_recursive(a, target, 0, 9))
print(binary_search_recursive(a, target2, 0, 9))

print(binary_search_iter(a, target,0, 9))
print(binary_search_iter(a, target2,0, 9))