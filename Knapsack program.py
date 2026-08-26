def knapsack_bottom_up(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(weights, profits, n, capacity, dp):
    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n - 1] <= capacity:
        dp[n][capacity] = max(
            profits[n - 1] + knapsack_top_down(
                weights, profits, n - 1,
                capacity - weights[n - 1], dp
            ),
            knapsack_top_down(
                weights, profits, n - 1,
                capacity, dp
            )
        )
    else:
        dp[n][capacity] = knapsack_top_down(
            weights, profits, n - 1, capacity, dp
        )

    return dp[n][capacity]


weights = [4, 5, 1]
profits = [1, 2, 3]
capacity = 4

n = len(weights)

bottom_up_result = knapsack_bottom_up(weights, profits, capacity)

dp = [[-1] * (capacity + 1) for _ in range(n + 1)]
top_down_result = knapsack_top_down(weights, profits, n, capacity, dp)

print("Bottom-Up Maximum Profit:", bottom_up_result)
print("Top-Down Maximum Profit:", top_down_result)