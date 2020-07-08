def abc(numbers):
    n = len(numbers)
    max1 = 0
    max2 = 0
    for first in range(n-1):
         max1 = max(max1, numbers[first])
    numbers.remove(max1)
    for second in range(n-1):
         max2 = max(max2, numbers[second])
    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_array = [int(x) for x in input().split()]
    print(abc(input_array)) 



