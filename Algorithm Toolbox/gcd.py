def gcd(a,b):
    if a>b:
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    else:
        if a==0:
            return b
        else:
            return gcd(a,b%a)

if __name__=="__main__":
    a = int(input())
    b = int(input())
    print(gcd(a,b))
