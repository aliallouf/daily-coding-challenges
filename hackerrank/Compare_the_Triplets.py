#!/bin/python3
def compareTriplets(a, b):
    alice_Score = 0
    bob_Score = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_Score += 1
        elif a[i] == b[i]:
            alice_Score += 0
            bob_Score += 0    
        else:
            bob_Score += 1    
    return alice_Score, bob_Score

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = compareTriplets(arr1, arr2)
print(result[0], result[1])