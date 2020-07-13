def calc_fib(n):
    a = 0
    b = 1
    c = a+b
    if n==0:
        return a
    elif n==1:
        return b
    for i in range(2,n):
        a = b
        b = c
        c = (a + b) % 10
    
    return c 


if __name__ == "__main__":

    n = int(input())
    print(calc_fib(n))