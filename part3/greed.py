

def 모험가_길드():
    # 가장 작은 녀석 부터 넣어주자.
    
    # 20분
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    count = 0
    while arr:
        a = arr[-1]
        try:
            if len(arr) >= arr[-a]:
                for i in range(a):
                    arr.pop()
                count += 1
            else:
                break
        except:
            break
        # print(arr, count)
        
    print(count)
    




def 곱하기_혹은_더하기():
    # 0 이나 1이면 곱하지 말고 더하자.
    
    # 6분
    arr = list(map(int, list(input())))
    arr = arr[::-1]
    
    s = arr.pop()
    while arr:
        a = arr.pop()
        if s == 0 or s == 1 or a == 0 or a == 1:
            s += a
        else:
            s *= a
    print(s)




def 문자열_뒤집기():
    # 0과 1중에 더 적은 부분을 return하자
    # 000011001100 일 경우, 0 1 0 1 0 으로 구분되므로, 1의 부분의 갯수 2를 return
    
    # 8분
    arr = list(input())
    
    result = 0
    if len(arr) != 0:
        
        one_count = 0
        zero_count = 0
        
        s = [arr.pop()]
        
        while arr:
            # print(arr, s)
            item = arr.pop()
            if s[-1] != item:
                if s[-1] == '0':
                    zero_count += 1
                else:
                    one_count += 1
            s.append(item)
                    
    result = min(zero_count, one_count)
    print(result)
    
    


def 만들_수_없는_금액_느린버전():
    # 모든 경우의 수를 만들 경우 너무 많은 시간이 걸린다.
    import random
    from itertools import combinations
    
    n = random.randint(1, 1000)
    arr = [random.randint(1, 1000000) for _ in range(n)]
    # n = int(input())
    # arr = list(map(int, input().split()))
    
    cases = []
    for i in range(1, n):
        cases.extend(map(lambda x:sum(x), list(combinations(arr, i))))
    
    cases.sort()
    for i in range(1, 1000000*1000):
        if not i in cases:
            print(i)
            break




def 만들_수_없는_금액():
    # 만약 1이라도 차이난다면 그 값을 만들 수 없음!
    
    # 28분!! (제한 시간 30분)
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    
    result = 0
    
    s = [0]
    while arr:
        # print(arr)
        # print(s)
        a = arr.pop()
        if s[-1] < a-1:
            result = sum(s)+1
            break
        s.append(a)

    print(result)




def 볼링공_고르기_느린버전():
    # 1초 이상 넘어가는 경우 있음
    from itertools import combinations
    
    # n, m = map(int, input().split())
    # arr = list(map(int, input().split()))
    
    import random, time
    n = 1000
    arr = [random.randint(1, 10) for _ in range(n)]
    
    start = time.time()
    cases = list(combinations(arr, 2))
    
    count = 0
    for c in cases:
        if c[0] != c[1]:
            count += 1
    
    print(count)
    
    end = time.time()
    print(end - start)
    
    
    
    
def 볼링공_고르기():
    # 1회차 30분 초과
    # 2회차 힌트 사용 2분 (어 근데 정답 코드랑 다른데 어케 푼거지)
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    
    count = 0
    # 헛 짚은 점.
    # 1. nCr은 10억이 넘어가는 경우가 아니면 안쓰임
    # 2. 반대로 combinations은 일반적으로 n이500 이상 넘어가면 쓰기 어려움
    # 3. 결론적으로 그 중간인 이중 for문을 쓰면 1000*1000 = 1,000,000 의 연산 만으로도 구할 수 있음
    for i in range(n):
        for j in range(i, n): # i~n까지 만 선택해야 순서가 다른 친구가 생기지 않음.
            if arr[i] != arr[j]: # 하지만 무게가 서로 같으면 선택 X
                count += 1
    
    print(count)
    

    
    



