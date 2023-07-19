'''
[4. 계수 정렬]

* [알고리즘]    :  max(a)+1 길이의 list를 선언 & 0 으로 초기화
                  데이터의 값과 동일한 인덱스의 데이터를 1씩 증가 => 리스트에는 각 데이터가 몇번 등장했는지 기록됨
                  그 리스트의 인덱스를 값만큼 출력하면 끝

* [시간 복잡도] :  O(N + K), N은 데이터 개수, K는 가장 큰 수

* [특징]       :  공간복잡도 비효율적일 수도.
                 성적(0~100점) 처리에 유용.

                  cf) 기수정렬(radix sort)와 계수정렬이 현존하는 정렬 알고리즘 중 가장 빠름
                      기수정렬이 조금더 느리지만, 처리할 수 있는 정수의 크기가 크다. (코테에는 기수정렬 문제 안나옴)
'''
def count_sort(a):
    # [1] count_list 길이는 max(a)+1, 값은 0으로 초기화
    count_list = [0] * (max(a)+1)

    # [2] count 시작
    for i in a:
        count_list[i] += 1

    # [3] 결과 출력
    res = []
    for i in range(len(count_list)):
        for j in range(count_list[i]): # 횟수만큼 출력
            res.append(i)
    return res

'''실행 결과'''
a = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(count_sort(a))
