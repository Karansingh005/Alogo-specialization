def fibo(n):
    a = 0
    b = 1
    c = a + b
    if n <= 1:
        return n
    for i in range(2,n):
        a = b
        b = c
        c = a + b
    return c

def fibo_sum(n,m):
    a = fibo(n)
    b = fibo(n+1)
    c = a + b
    sum_fibo = (a + b + c) % 10
    if m==n:
        return fibo(n) % 10
    elif m-n==1:
        return (a+b)%10
    for i in range(n+2,m):
        a = b
        b = c 
        c = a + b
        sum_fibo = (sum_fibo + c)%10
    return sum_fibo

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibo_sum(n,m))
