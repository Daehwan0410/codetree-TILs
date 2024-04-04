import sys

s = sys.stdin
n, m, k = map(int, s.readline().split())
board = [list(map(int, s.readline().split())) for _ in range(n)]
pl = []
pds = []
for _ in range(m):
    x, y, d, sp = map(int, s.readline().split())
    pl.append([x-1, y-1])
    pds.append([d, sp, 0])
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]   
score = [0]* m
for _ in range(k):
    for i, (x, y) in enumerate(pl):
        nx = x + dxy[pds[i][0]][0]
        ny = y + dxy[pds[i][0]][1]
        if nx < 0 or nx >= n or ny <0 or ny >= n:
            pds[i][0] = (pds[i][0] + 2) % 4
            nx = x + dxy[pds[i][0]][0]
            ny = y + dxy[pds[i][0]][1]
            
#         이동한 장소에 플레이어가 있을때
        if [nx, ny] in pl:
            j = pl.index([nx, ny])
            pl[i] = [nx, ny]
            lossplay = -1
            winplay = -1
            if sum(pds[i][1:]) > sum(pds[j][1:]):
                lossplay = j
                winplay = i
            elif sum(pds[i][1:])< sum(pds[j][1:]):
                lossplay = i
                winplay = j
            elif pds[i][1] > pds[j][1]:
                lossplay = j
                winplay = i
            else:
                lossplay = i
                winplay = j
                
            score[winplay] +=  abs(sum(pds[i][1:]) - sum(pds[j][1:]))
            temp2 = [pds[winplay][2], pds[lossplay][2]]             
            try:
                temp2.extend(board[nx][ny])
            except:
                temp2.append(board[nx][ny])
            pds[winplay][2] = max(temp2)
            temp2[temp2.index(max(temp2))] = 0
            board[nx][ny] = temp2 
            pds[lossplay][2] = 0
            while True:
                lnx = pl[lossplay][0] + dxy[pds[lossplay][0]][0]
                lny = pl[lossplay][1] + dxy[pds[lossplay][0]][1]
                if [lnx, lny] not in pl and 0 <= lnx< n and  0<= lny< n:
                    pl[lossplay] =[lnx, lny]
                    temp2 = []
                    try:
                        temp2.extend(board[lnx][lny])
                    except:
                        temp2.append(board[lnx][lny])
                    pds[lossplay][2] = max(temp2)
                    temp2[temp2.index(max(temp2))]= 0
                    board[lnx][lny] = temp2
                    break
                else:
                    pds[lossplay][0] = (pds[lossplay][0] + 1) % 4
                    
#         이동한 장소에 플레이어가 없을때 
        else:
            pl[i] = [nx, ny]
            temp1 = [pds[i][2]]
            try:
                temp1.extend(board[nx][ny])
            except:
                temp1.append(board[nx][ny])
            pds[i][2] = max(temp1)
            temp1[temp1.index(max(temp1))] = 0
            board[nx][ny] = temp1
print(*score)