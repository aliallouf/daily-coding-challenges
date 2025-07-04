n = int(input())
l = list(map(int, input().split()))
count_evens = 0
count_odds = 0
count_zeros = 0
for i in range(n):
    if l[i] == 0:
        count_zeros += 1
    if l[i] > 0:
        count_evens += 1
    if l[i] < 0:
        count_odds += 1
    
print('{:.6f}'.format((count_evens / n)))
print('{:.6f}'.format((count_odds / n)))
print(round(count_zeros / n, 6))