def aVeryBigSum(n):
    result = 0
    l = list(map(int, input().split()))
    for i in range(n):
        result += l[i]
    return result
num = int(input())
print(aVeryBigSum(num))    