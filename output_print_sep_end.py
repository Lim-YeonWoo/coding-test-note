'''파이썬 print'''

# sep : 기본값은 빈칸
# end : 기존값은 개행(\n)

a, b, c = 10, 20, 30
print(a, b, c)
print(a, b, c, sep=", ")
print(a, b, c, end="!") #이 출력문 뒤에는 엔터가 없다.
print(a, b, c, end="!\n")
print(a, b, c, sep="+", end="") #이 출력문 뒤에도 엔터가 없다.
print(a, b, c)

'''
[output]
10 20 30
10, 20, 30
10 20 30!10 20 30!
10+20+3010 20 30
'''