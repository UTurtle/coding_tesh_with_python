

def ���谡_���():
    # ���� ���� �༮ ���� �־�����.
    
    # 20��
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
    




def ���ϱ�_Ȥ��_���ϱ�():
    # 0 �̳� 1�̸� ������ ���� ������.
    
    # 6��
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




def ���ڿ�_������():
    # 0�� 1�߿� �� ���� �κ��� return����
    # 000011001100 �� ���, 0 1 0 1 0 ���� ���еǹǷ�, 1�� �κ��� ���� 2�� return
    
    # 8��
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
    
    


def ����_��_����_�ݾ�_��������():
    # ��� ����� ���� ���� ��� �ʹ� ���� �ð��� �ɸ���.
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




def ����_��_����_�ݾ�():
    # ���� 1�̶� ���̳��ٸ� �� ���� ���� �� ����!
    
    # 28��!! (���� �ð� 30��)
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




def ������_����_��������():
    # 1�� �̻� �Ѿ�� ��� ����
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
    
    
    
    
def ������_����():
    # 1ȸ�� 30�� �ʰ�
    # 2ȸ�� ��Ʈ ��� 2�� (�� �ٵ� ���� �ڵ�� �ٸ��� ���� Ǭ����)
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    
    count = 0
    # �� ¤�� ��.
    # 1. nCr�� 10���� �Ѿ�� ��찡 �ƴϸ� �Ⱦ���
    # 2. �ݴ�� combinations�� �Ϲ������� n��500 �̻� �Ѿ�� ���� �����
    # 3. ��������� �� �߰��� ���� for���� ���� 1000*1000 = 1,000,000 �� ���� �����ε� ���� �� ����
    for i in range(n):
        for j in range(i, n): # i~n���� �� �����ؾ� ������ �ٸ� ģ���� ������ ����.
            if arr[i] != arr[j]: # ������ ���԰� ���� ������ ���� X
                count += 1
    
    print(count)
    

    
    



