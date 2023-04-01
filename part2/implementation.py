# 구현문제 4문제 총 53분

def up_down_left_right(): # 10분
    # n = int(input())
    # moves = list(input().split())

    n = 5
    moves = ["R", "R", "R", "U", "D", "D"]

    y, x = 0, 0
    move_dic = {"U":(-1, 0), "D":(1, 0), "L":(0,-1), "R":(0,1)}

    for m in moves:
        a, b = move_dic[m]
        dy, dx = y + a, x + b
        if n > dy >= 0 and n > dx >= 0:
            y = dy
            x = dx

    print(x+1, y+1)



def time_count(): # 12분
    # n = int(input())
    n = 5

    count = 0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    count += 1
    print(count)



def knight(): # 20분
    pos = input()
    x, y = pos
    # x, y = "a", "1"

    x = int(str(ord(x) - 96))-1
    y = int(y)-1

    # print(y, x)
    moves = [(2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2), (-2,1), (-2,-1)]

    count = 0
    for a, b in moves:
        dy, dx = y + a, x + b
        if 7 > dy >= 0 and 7 > dx >= 0:
            count += 1
    print(count)


def dev_game(): # 53분
    """x, y는 0, 0 부터, direct는 0, 1, 2, 3 -> 북 동 남 서"""
    # n, m = map(int, input().split())
    # x, y, direct = map(int, input().split())

    # matrix = []
    # for i in range(n):
    #     row = list(map(int, list(input())))
    #     matrix.append(row)

    n, m = 4, 4
    x, y, direct = 1, 1, 0
    matrix = []
    data_set = """1111
    1001
    1101
    1111""".split('\n')
    for row in data_set:
        matrix.append(list(map(int, list(row.strip()))))
        
    # print(matrix)

    def turn(direct):
        if direct == 0:
            direct = 3
        else:
            direct -= 1
        return direct

    # direct -> move를 결정 북(-1,0) 남(1,0), 서(0,-1), 동(0,1)
    move_dic = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

    visited_count = 0

    # 1~3단계 반복
    while True:
        direct = turn(direct)
        turn_count = 0

        # 1~2단계 반복
        while turn_count != 4:
            a, b = move_dic[direct]
            dy, dx = y + a, x + b
            if n > dy >= 0 and m > dx >= 0 and matrix[dy][dx] == 0:
                y = dy
                x = dx
                visited_count += 1
                matrix[dy][dx] = 2
                turn_count = 0
            else:
                direct = turn(direct)
                turn_count += 1

        # 3단계에서 
        a, b = move_dic[direct]
        a, b = -a, -b
        dy, dx = y + a, x + b
        if n > dy >= 0 and m > dx >= 0 and matrix[dy][dx] != 1: # 바다가 아닌 경우 뒤로 한 칸 이동하여 다시 1단계 부터
            y = dy
            x = dx
        else: # 만약 뒤가 바다라면 종료
            break
    # print(matrix)
    print(visited_count)

