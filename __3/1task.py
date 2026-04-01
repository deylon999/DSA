def max_subarray(arr):
    dp = [0]*len(arr)
    dp[0] = arr[0]

    for i in range(1, len(arr)):
        dp[i] = max(dp[i-1]+arr[i], arr[i])

    max_sum = max(dp)
    end = dp.index(max_sum)

    start = end
    while start > 0 and dp[start] == dp[start-1] + arr[start]:
        start -= 1

    return max_sum, arr[start:end+1] 

print(max_subarray([12, -5, 7, 9, -14, 3, 8]))
