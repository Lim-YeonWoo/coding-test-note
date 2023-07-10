'''
[ 방법1. dx dy ]
    dx = [+1, -1, 0, 0]
    dy = [0, 0, +1, -1]
'''
x, y = 1, 1
dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

for i in range(len(dx)):
    nx = x + dx[i] # nx next x
    ny = y + dy[i]

    # 조건에 해당되면 x, y 갱신
    if (nx>=1 and nx<=8 and ny>=1 and ny<=8):
        x = nx
        y = ny

'''
[방법2. steps]
    steps = [(+1,0), (-1,0), (0,+1), (0,-1)]
'''
x, y = 1, 1
steps = [(+1,0), (-1,0), (0,+1), (0,-1)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if (nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
        x = nx
        y = ny