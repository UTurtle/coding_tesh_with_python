# 커리큘럼 

import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
indegree = [0]*(v+1)
time = [0]*(v+1)

# 입력을 받을 때, 충분히 문제를 숙지하고 입력 부분을 최대한 정규화 하여 받음
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # i의 time
    for x in data[1:-1]:
        graph[x].append(i) # i가 x를 필요로 하는 것이므로 x -> i 로 연결 (x에 연결된 i의 indegree == 0 이되면 i로 이동 가능)
        indegree[i] += 1 # i들이 x가 필요한 갯수 만큼 +1

# print(graph)
# print(indegree)
# print(time)
       
def solution():
    q = deque([])
    total_time = time[:] # time 복사
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        # print(q)
        now = q.popleft() # queue 사용시 보통은 leftpop()
        
        for to in graph[now]:
            # 제일 큰 total_time 구하기
            total_time[to] = max(total_time[to], total_time[now] + time[to])
            indegree[to] -= 1
            
            if indegree[to] == 0:
                q.append(to)
                
    for i in range(1, v+1):
        print(total_time[i])
        
solution()
