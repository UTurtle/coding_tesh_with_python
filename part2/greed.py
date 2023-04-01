
def big_number_rule():
    """n :arr의 크기, m :숫자가 더해지는 횟수, k :연속으로 더할 수 있는 횟수"""
    # n, m, k = map(int, input().split())
    # arr = list(map(int, input().split()))

    # Test code
    n, m, k = 5, 8, 3
    arr = [2,4,5,4,6]

    arr.sort()
    first = arr[-1]
    second = arr[-2]

    answer = 0
    while m:
        for i in range(k):
            answer += first
            m -= 1
            if m == 0:
                break
        answer += second
        m -= 1

    print(answer)



def card_game():
    # n, m = map(int, input().split())
    # matrix = []
    # for i in range(n):
    #     row = list(map(int, input().split()))
    #     matrix.append(row)

    # Test Code
    # n, m = 3, 3
    # matrix = [[3,1,2],
    #       [4,1,4],
    #       [2,2,2]]

    n, m = 2, 4
    matrix = [[7,3,1,8],
          [3,3,3,4]]
    
    min_arr = []
    for row in matrix:
        min_arr.append(min(row))

    print(max(min_arr))



def to_be_one():
    # n, m = map(int, input().split())

    # Test Code
    n, k = 25, 3

    count = 0
    while n != 1:
        if n % k == 0:
            n = n//k
        else:
            n -= 1
        count +=1
    print(count)

