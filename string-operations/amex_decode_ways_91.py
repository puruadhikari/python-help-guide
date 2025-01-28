def numDecodings(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)

    dp[0] = 1  # Empty string
    dp[1] = 1 if s[0] != '0' else 0  # First character

    for i in range(2, n + 1):
        # Single digit decode (s[i-1])
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Double digit decode (s[i-2:i])
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# Example Usage:
s = "11106"
print(numDecodings(s))  # Output: 2
