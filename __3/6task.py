coins1 = [1, 5, 10, 25, 50, 100]
coins2 = [1, 4, 6, 9]
amounts = [23, 37, 58, 74, 99, 123]

def greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    result = []
    remaining = amount
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    return result

def dp_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    result = []
    cur = amount
    while cur > 0:
        result.append(parent[cur])
        cur -= parent[cur]
    return result
