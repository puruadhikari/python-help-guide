"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
"""

def kids_with_greatest_candies(candies,extra_candies):
    max_candies = max(candies)
    result = []
    for num_candies in candies:
        if num_candies+extra_candies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    return result

candies = [2,3,5,1,3]
extraCandies = 3

print(kids_with_greatest_candies(candies,extraCandies))