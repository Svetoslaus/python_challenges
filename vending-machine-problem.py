def optimal_number_of_coins(n, coins):
    # Initialize the dp array with maximum values
    dp = [float('inf')] * (n + 1)

    # Base case: 0 coins needed to make change for 0 amount
    dp[0] = 0

    # Loop through all possible amounts from 1 to n
    for amount in range(1, n + 1):
        # Try all available coin denominations
        for coin in coins:
            # If the coin is smaller than or equal to the current amount
            if coin <= amount:
                # Update the minimum number of coins needed
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    # Return the optimal number of coins needed for the given amount
    return dp[n]

# Test the function
amount = 27
coin_denominations = [1, 5, 10, 25]  # Penny, Nickel, Dime, Quarter
result = optimal_number_of_coins(amount, coin_denominations)
print(f"The optimal number of coins required to make change for {amount} cents is: {result}")
