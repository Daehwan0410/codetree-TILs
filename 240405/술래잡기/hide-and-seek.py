from collections import deque
import sys

s= sys.stdin
n, m, h, k =  map(int, s.readline().split())
hlist = []
for i in range(m):
    x, y, d = map(int, s.readline().split())
    hlist.append([x-1, y-1, d, True])
tree = []
for i in range(h):
    x, y= map(int, s.readline().split())
    tree.append([x-1, y-1])
dxy = [[-1,0], [0,1], [1,0], [0,-1]]
px, py, pd = n//2, n//2, 0
a = [i for i in range(2, n)]
b = [i for i in range(1, n)]
a = a + b
a.append(n-1)
a.sort(reverse = True)
a = deque(a)
count = 0
check = 1
answer = 0
# print(hlist)
for _ in range(1,k+1):
    #move hide people
    for i , (x, y , d, bt) in enumerate(hlist):
        if not bt:
            continue
        if abs(px -x) + abs(py- y) <=3:
            nx = x + dxy[d][0]
            ny = y + dxy[d][1]
            if 0<= nx <n and 0 <= ny < n and [nx, ny] != [px , py]: 
                hlist[i][:2] = [nx, ny]
            else:
                if i ==2:
                    print(nx, ny, d, px, py)
                d = (d+2) % 4
                nx = x + dxy[d][0]
                ny = y + dxy[d][1]
                if nx != px and ny != py:
                    hlist[i]= [nx, ny, d, bt]
    #move people               
    if [px, py] ==[0, 0] :
        a.reverse()
    elif [px, py] == [n//2, n//2]:
        a =list(a)
        a = deque(sorted(a))
    px = px + dxy[pd][0]
    py = py + dxy[pd][1]
    count +=1
#     print('count:', count,'check', check)
    if count == check:
        a.append(count)
        check = a.popleft()
        pd = (pd+1) % 4
        count = 0
    tSum = 0
    for i in range(3):
        nx = px + dxy[pd][0]*i
        ny = py + dxy[pd][1]*i
        if nx < 0 or nx>=n or ny<0 or ny>= n:
            break
        if[nx, ny] in tree:
            continue
        for j, (bx, by, d, bt) in enumerate(hlist):
            if nx == bx and ny == by and bt:
                hlist[j][3] = False
                tSum +=1
    answer += tSum*_
print(answer)