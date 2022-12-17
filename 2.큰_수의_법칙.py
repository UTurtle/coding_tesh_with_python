def biggger_rule(n, m, k, numbers):
    numbers.sort()
    count_k = 0
    answer = 0
    for i in range(m):
        if count_k >= k:
            answer += numbers[-2]
            count_k = 0
            continue
        answer += numbers[-1]
        count_k += 1
    return answer

result = biggger_rule(5, 8, 3, [2,4,5,4,6])
print(result)
