def fibo(n):
    a = 0
    b = 1
    c = a + b
    sum_fibo = 2
    if n <= 1:
        return n
    for i in range(2,n):
        a = b
        b = c
        c = a + b
        sum_fibo = (sum_fibo + c*c)%10
          
    return sum_fibo 

if __name__ == "__main__":
    n = int(input())
    print(fibo(n))