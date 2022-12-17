def exchange(n):
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin_type in coin_types:
        mod, n = divmod(n, coin_type)
        count += mod
    return count
