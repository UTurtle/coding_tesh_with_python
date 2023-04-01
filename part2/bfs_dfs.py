# 그래프 문제 2문제 총 19분

from collections import deque

def see_matrix(matrix):
    for row in matrix:
        print(row)
    print("="*25)

def ice_juice(): # 13분
    # n, m = map(int, input().split())
    # matrix = []
    # for i in range(n):
    #     row = list(map(int, list(input())))
    #     matrix.append(row)
    
    n, m = 15, 14
    matrix = []
    data_set = """00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111""".split('\n')
    for row in data_set:
        matrix.append(list(map(int, list(row.strip()))))
   
    # print(matrix)

    def fill(y, x):
        """bfs로 근처에 같은 원소 채우기"""
        moves = [(0,1),(0,-1),(-1,0),(1,0)]    
        que = deque([[y,x]])

        while que:
            y, x = que.pop()

            for a, b in moves:
                dy, dx = y + a, x + b
                if n > dy >= 0 and m > dx >= 0:
                    if matrix[dy][dx] == 0:
                        que.append([dy, dx])
                        matrix[dy][dx] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                fill(i, j) # matrix는 굳이 매개변수로 줄 필요가 없다. (포인터 값이기 때문)
                count += 1
    print(count)



def escape_maze(): # 19분
    # n, m = map(int, input().split())
    # matrix = []
    # for i in range(n):
    #     row = list(map(int, list(input())))
    #     matrix.append(row)
    
    n, m = 5, 6
    matrix = []
    data_set = """101010
111111
000001
111111
111111""".split('\n')
    for row in data_set:
        matrix.append(list(map(int, list(row.strip()))))
   
    # print(matrix)

    def bfs(y, x):
        """bfs로 최단 경로 찾기"""
        moves = [(0,1),(0,-1),(-1,0),(1,0)]    
        que = deque([[y,x]])

        while que:
            y, x = que.pop()

            for a, b in moves:
                dy, dx = y + a, x + b
                if n > dy >= 0 and m > dx >= 0:
                    if matrix[dy][dx] == 1:
                        que.append([dy, dx])
                        matrix[dy][dx] = matrix[y][x] + 1
    # see_matrix(matrix)
    bfs(0, 0)
    # see_matrix(matrix)
    print(matrix[n-1][m-1])

escape_maze()