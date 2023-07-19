'''
[3. 퀵 정렬]

* [알고리즘]    :  1. 피벗(pivot)을 정한다
                     (호어 분할 방식에 의해) 맨 첫번째 데이터를 피벗으로 정한다.

                  2. 왼쪽에서부터 피벗보다 큰 수 찾기
                     & 오른쪽에서부터 피벗보다 작은 수 찾기

                  3-1. ( left 랑 right idx 안 엇갈렸으면, left데이터랑 right데이터 swap. ) * 반복

                  3-2. left 랑 right idx 엇갈렸으면, 작은 데이터(right)랑 pivot swap
                     => 이제 가운데 피벗을 기준으로 "분할" "파티션" 됨
                     => 양쪽에 대해 재귀호출
                     => 재귀호출 종료조건 = 리스트에 데이터 개수가 1개.

* [시간 복잡도] :  평균의 경우 = O(NlogN)
                  최악의 경우 = 이미 데이터가 정렬되어 있는 경우 = O(N^2)
                  cf) 이미 데이터가 거의 정렬되어 있는 경우 = 삽입 정렬 쓰기, O(N) 걸림
'''
def quick_sort_original(a, start, end):
    #[1] 종료 조건
    if start>=end: #원소가 1개
        return a

    #[2] pivot, left, right 초기화 (셋 다 idx임)
    pivot = start
    left = start + 1
    right = end

    #[3] while 문
    while left<=right:
        #[3-1] 왼쪽 while
        while left<=end and a[left] <= a[pivot] :
            left += 1 #left는 end까지 증가

        #[3-2] 오른쪽 while
        while start<right and a[right] >= a[pivot] : #start<=right이면 틀림. 등호 없어야함!!!
            right -= 1 #right는 start+1까지 감소 (start에는 pivot이 있음. 가면 안됨.)

        #[3-3] swap (경우1. left랑 right swap, 경우2. right랑 pivot swap)
        if left>right: #엇갈렸으면 작은수랑 pivot 교환
            a[right], a[pivot] = a[pivot], a[right]
        else:
            a[left], a[right] = a[right], a[left]

    #[4] 재귀호출 2번 (양쪽)
    quick_sort_original(a, start, right-1) #pivot은 계속해서 start에 머무는 중. 변한 값은 right임. right가 가운데 idx임.
    quick_sort_original(a, right+1, end)

def quick_sort_python(a): # 코드가 간단하나, 정석적인 방법에 비해 비교연산횟수가 증가한다.
    # [1] 종료 조건
    if len(a)<=1:
        return a

    # [2] pivot & tail 초기화 (여기선 pivot이 idx아니고 a[idx]값 자체)
    pivot = a[0]
    tail = a[1:]

    # [3] left_side & right_side array 초기화
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # [4] return (왼쪽재귀호출 + pivot + 오른쪽재귀호출)
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)

'''실행 결과'''
a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort_original(a, 0, len(a)-1)
print(a)

b = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort_python(b))