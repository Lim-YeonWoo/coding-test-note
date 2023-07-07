'''
[heap]
    : 파이썬의 heap은 최소힙(min heap)
    : heapq.heappush(h, 50) 에서
    AttributeError: partially initialized module 'heapq' has no attribute 'heappush' (most likely due to a circular import)
    에러 뜨는데 왜 그런지 모르겠음.
'''

'''1. heapq 이용방법'''
import heapq

h = []
# heappush()
heapq.heappush(h, 50)
heapq.heappush(h, 10)
heapq.heappush(h, 30)
heapq.heappush(h, 20)

# heappop()
top = heapq.heappop(h)
print(top)

# heapify() : list를 heap으로 변경. O(logN)
a = [2, 3, 7, 4]
heapq.heapify(a)
print(a)

'''
2. [오름차순 정렬] 
    min heap 이니까 넣었다가 빼면됨
'''
def heapsort(a):
    h = []
    result = []

    # 이렇게 하나씩 넣거나 아니면 heapq.heapify(a)로 해도 된다.
    for value in a:
        heapq.heappush(value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

'''
3. [내림차순 정렬] 
    파이썬에서는 max heap을 지원하지 않는다.
    따라서 원소의 부호를 임시로 변경하는 방법.
'''
def heapsort(a):
    h = []
    result = []

    # 이렇게 하나씩 넣거나 아니면 heapq.heapify(a)로 해도 된다.
    for value in a:
        heapq.heappush(-value) #-value를 넣는다.

    for _ in range(len(h)):
        result.append(-heapq.heappop(h)) #pop()할때 다시 - 해서 원래대로 돌려준다

    return result