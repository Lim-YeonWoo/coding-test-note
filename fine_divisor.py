'''
[약수 구하기]

루트n까지만 따져보면됨. [1, 루트n]

루트n은 n**(1/2)

3*3=9 같은건 예외처리 해줘야함. 3 한번만 들어가게.
'''


def find_divisor(n):
    divisor_list = []

    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            divisor_list.append(i)

            if ((i**2) != n): # 2*2 = 4 처럼 완전제곱 인게 아니라면
                divisor_list.append(n//i)
    divisor_list.sort()
    return divisor_list