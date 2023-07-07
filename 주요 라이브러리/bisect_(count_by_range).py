'''
[bisect]
    : 이진탐색 binary search할때 유용
    : 이미 정렬된 리스트에서 특정값 찾거나 특정값 넣기
'''

'''
1. bisect 이용방법
'''
from bisect import bisect_left, bisect_right

#    0  1  2  3  4  5  6
a = [2, 3, 4, 4, 4, 4, 5, 5, 6]

start = bisect_left(a, 4) # 2
end = bisect_right(a, 4) # 6
print(start, end)

'''
2. 정렬된 리스트에서 "값이 특정 범위에 속하는 원소의 개수" 구하기
    : left_value <= x <= right_value인 원소 개수
    : O(logN)
'''
def count_by_range(a, left_value, right_value):
    left_idx = bisect_left(a,left_value)
    right_idx = bisect_right(a, right_value)

    return right_idx - left_idx

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

#값이 4인 데이터 개수
print(count_by_range(a, 4, 4))

#값이 [-1, 3]인 데이터 개수
print(count_by_range(a, -1, 3))
