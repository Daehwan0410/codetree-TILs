from collections import deque
import sys

def FindBase(i):
    x, y = shop[i]
    queue = deque()
    queue.append([x, y, 0])
    fvisited = [[False]* n for _ in range(n)]
    fvisited[x][y]= True
    alist = []
    maxCount = 256
    while queue:
        qx, qy, count  = queue.popleft()
        for dx, dy in dxy:
            nx = qx + dx
            ny = qy + dy
            if 0<= nx <n and 0<= ny <n and  not visited[nx][ny] and not fvisited[nx][ny]:
                if [nx, ny] in baseCamp and count<= maxCount:
                    maxCount = count
                    alist.append([nx, ny])
                elif count <maxCount:
                    queue.append([nx, ny, count+1])
                    fvisited[nx][ny] = True
    alist.sort()
    nx , ny = alist[0]
    visited[nx][ny] = True
    baseCamp.remove([nx, ny])
    return nx, ny
                
def bfs(x, y, j):
    queue = deque()
    queue.append([x, y, 1])
    qvisited[x][y]= 1
    while queue:
        qx, qy, nn = queue.popleft()
        if [qx, qy] == shop[j]:
            return nn
        for dx, dy in dxy:
            nx = qx + dx
            ny = qy + dy
            if 0 <= nx < n and 0<= ny < n :
                if nn + 1 < qvisited[nx][ny] and not visited[nx][ny]:
                    qvisited[nx][ny] = nn + 1
                    queue.append([nx, ny, nn+1])
    return 226
            
s= sys.stdin
n,m = map(int,s.readline().split())
baseCamp = []
board = [list(map(int,s.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            baseCamp.append([i,j])
shop = []
for _ in range(m):
    x, y = map(int,s.readline().split())
    x, y = x-1, y-1
    shop.append([x,y])
dxy = [[-1,0], [0,-1], [0,1], [1,0]]

visited = [[False]* n for _ in range(n)]

i = 1
mcount = 0
baseList = []
while True:
    for j , (ex, ey,check) in enumerate(baseList):
        if not check:
            continue
        lCount = []
        qvisited = [[226]* n for _ in range(n)]
        qvisited[ex][ey]=0
        for dx, dy in dxy:
            nx = ex + dx
            ny = ey + dy
            if 0 <= nx < n and 0<= ny < n and not visited[nx][ny]:
                lCount.append(bfs(nx, ny, j))
            else:
                lCount.append(226)
        baseList[j][:2] = ex + dxy[lCount.index(min(lCount))][0], ey + dxy[lCount.index(min(lCount))][1]
#         board[ex][ey] = 0
#         board[ex+ dxy[lCount.index(min(lCount))][0]][ey + dxy[lCount.index(min(lCount))][1]] = j+2
        
    for j, (ex, ey, check) in enumerate(baseList):
        if check and [ex, ey] == shop[j]:
            visited[ex][ey]= True
            baseList[j][2]= False
            mcount +=1 
            
    if mcount == m:
        print(i)
        break
    
    if i <= m:
        fx, fy =FindBase(i-1)
        baseList.append([fx, fy, True])
        board[fx][fy] = i+1
#     for a in range(n):
#         print(board[a])
#     print('-------------------------------------------')
    i+=1