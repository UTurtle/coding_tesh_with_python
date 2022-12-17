def exchange(n):
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin_type in coin_types:
        mod, n = divmod(n, coin_type)
        count += mod
    return count

result = exchange(1270)
print(result)

# 푸는데 걸린 시간 5분
