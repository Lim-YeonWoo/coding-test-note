'''2차원 행렬을 90도 회전하는 함수'''
def rotate_a_matrix_by_90_degree(a):
    row_len = len(a)
    col_len = len(a[0])

    res = [[0]*row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            res[c][row_len-1-r] = a[r][c]

    return res

'''실행'''
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree(a))

'''
[Input]
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

[Output]
[
    [9, 5, 1], 
    [10, 6, 2],
    [11, 7, 3], 
    [12, 8, 4]
]
'''