'''
[1. 선택 정렬]

* [알고리즘]    :  ( 가장 작은 수 찾아서 앞쪽카드랑 자리 바꾸기 ) * (n-1) 번

* [시간 복잡도] :  O(N^2)

* [특징]       :  가장 느림.
                 가장 작은 수만 들고 있는 그 개념 알아둘 필요 있음.
'''
def selection_sort(a):
    for i in range(0, len(a)):
        # min_idx 초기화
        min_idx = i # 꼭 해줘야 함. i가 최소일 수도 있으니.

        # i~끝 중에 가장 작은 수 찾기
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j

        # i랑 가장 작은 수 swap
        a[i], a[min_idx] = a[min_idx], a[i]

    return a


'''
[2. 삽입 정렬]

* [알고리즘]    :  { 
                    i번째 수의 앞부분은 이미 다 정렬되어있고 ,
                    (앞부분의 맨뒷수와 그 바로 앞의 수를 비교하며 순서 맞추기) * (i-1)번  
                  } * (n -1)번

* [시간 복잡도] :  O(N^2) 
                  최선의 경우 = 거의 정렬 되어 있는 경우 = O(N) 

* [특징]       :  거의 정렬 되어 있는 경우 => 삽입정렬 이용
'''
def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1): # i~1까지 거꾸로 보면서
            if a[j-1] > a[j]: # j-1번째수와 j번째수 자리 맞추기
                a[j-1], a[j] = a[j], a[j-1]
            else:
                break

    return a


'''
[결과 출력]
'''
a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(selection_sort(a))

b = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(insertion_sort(b))
