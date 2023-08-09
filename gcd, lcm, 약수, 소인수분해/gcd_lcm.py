'''
    * [최대공약수 gcd Greatest Common Divisor]
        : 유클리드 호제법 Euclidean Algorithm
            O(logN)
            a와 b의 최대공약수
            = b와 a%b의 최대공약수
            = ...
            = a%b가 0인 순간 b의 값이 최대공약수

    * [최소공배수 lcm Least Common Multiple]
        : a와 b의 최소공배수
         = a*b / (a와b의 gcd)
'''

def gcd(a, b): #맨처음에 a>b가 아니더라도 한번 돌고 나면 자동으로 a>b가 된다. 신경안써도됨
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a*b / gcd(a, b)

