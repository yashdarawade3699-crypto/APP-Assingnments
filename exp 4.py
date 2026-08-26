def fibonacci_memo(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci_memo(n - 1, dp) + fibonacci_memo(n - 2, dp)

    return dp[n]


def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Enter n: "))

dp = [-1] * (n + 1)

memo_result = fibonacci_memo(n, dp)
tabulation_result = fibonacci_tabulation(n)

print("Fibonacci using Memoization:", memo_result)
print("Fibonacci using Tabulation:", tabulation_result)