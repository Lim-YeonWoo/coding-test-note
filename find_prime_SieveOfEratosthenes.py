'''
[소수 찾기] [에라토스테네스의 체 (sieve of Eratosthenes)]
: 소수를 대량으로 빠르고 정확하게 구하는 방법
: 배열 이름이 sieve. sieve[x]=1이면 소수, 0이면 합성수.

1. sieve 배열 1으로 초기화
2. 2부터 검사 시작.
    sieve[2]=1
    2의 배수들은 sieve[4] = sieve[6] = sieve[8] = … = 0 으로 변경
3. 그 다음 수 검사. (sieve[x]=0이면 검사 안하고 건너뜀)
'''

n = 1000
sieve = [1]*n
sieve[0] = 0
sieve[1] = 0
primes=[]

for i in range(2, n):
    if sieve[i]==1: #소수라면
        primes.append(i)
        for j in range(2*i, n, i):
            sieve[j]=0
    else:
        continue
print(primes)