import sys

def gcd(a,b):
    if a > b:
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    else:
        if a == 0:
            return b
        else:
            return gcd(a,b%a)

def lcm(a,b):
    return int((a*b)/gcd(a,b))
    
if __name__ == "__main__":
    a,b = map(int, input().split())
    print(lcm(a,b))