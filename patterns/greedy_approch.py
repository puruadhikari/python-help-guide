"""
What is a Greedy Approach?
A greedy approach to a problem means you make the best decision you can at each step,
hoping that these locally optimal choices lead to a globally optimal solution. Instead of trying every possible combination,
you always pick the "greedy" option that seems best at the moment.

Simple Example: The Coin Change Problem
Imagine you want to make 68 cents using the fewest number of coins. Let’s say you have these coin denominations:
"""

amount = 68
coins = [1,5,10,25]  # Coin denominations in cents

#first coins sort it from higher to lower
coins.sort(reverse=True)
result = []
for coin in coins:
    while amount >= coin:
        amount -= coin
        result.append(coin)

print(result)
