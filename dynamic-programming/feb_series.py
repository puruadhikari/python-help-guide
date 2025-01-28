def fib_raw(n):
    if n ==1 or n==2:
        result = 1
    else:
        result = fib_raw(n-1) + fib_raw(n-2)
    return result

print(fib_raw(8))

def fib_with_memoize(n,memo):
    if memo[n]:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fib_with_memoize(n-1,memo)+ fib_with_memoize(n-2,memo)
    memo[n] = result
    return result

n = 8
mem_parameter = [None] * (n+1)

print(fib_with_memoize(n,mem_parameter))

def fib_bottom_up(n):
    if n==1 or n==2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] =1
    bottom_up[2] =1

    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

print(fib_bottom_up(10000))