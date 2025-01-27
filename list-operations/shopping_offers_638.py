"""
In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers,
and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, and an integer array needs
where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces
 of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the s
pecial offers. You are not allowed to buy more items than you want, even if that would lower the overall price.
You could use any of the special offers as many times as you want.

Example 1:

Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
"""


def calculate_total_cost(list_price, offer, required):
    # Extract the components of the offer
    offer_quantity = offer[:-1]
    offer_price = offer[-1]

    total_cost = 0

    # Find the maximum number of times the offer can be applied
    offer_count = float('inf')  # Start with a very large number
    for i in range(len(list_price)):
        offer_count = min(offer_count, required[i] // offer_quantity[i])

    # Update the required items after using the offer
    for i in range(len(list_price)):
        required[i] -= offer_count * offer_quantity[i]
    print(required)
    # Calculate the cost for the items covered by the offer
    total_cost += offer_count * offer_price

    # Add the cost for the remaining items
    for i in range(len(list_price)):
        total_cost += required[i] * list_price[i]

    return total_cost


# Example inputs
list_price = [2, 5]
offer = [3, 1, 5]
required = [3, 2]

# Calculate total cost
total_cost = calculate_total_cost(list_price, offer, required)
print(f"The total cost is: {total_cost}")
