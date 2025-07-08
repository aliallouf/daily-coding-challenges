def calculate_min_max_sums():

    l = list(map(int, input().split()))

    # Sort the list to easily find min and max and calculate sums
    l.sort()

    # The minimum sum is the sum of the first four elements (smallest four)
    mini_Sum = sum(l[:-1])

    # The maximum sum is the sum of the last four elements (largest four)
    max_Sum = sum(l[1:])

    print(mini_Sum, max_Sum)

if __name__ == '__main__':
    calculate_min_max_sums()
    
"""
#!/bin/python3
l = list(map(int, input().split()))
mini_Sum = 0
max_Sum = 0
max = min = l[0]
for i in range(len(l)):
    if l[i] > max:
        max = l[i]
    if l[i] < min:
        min = l[i]
for i in range(len(l)):
    if l[i] != max:
        mini_Sum += l[i]
    if l[i] != min:
        max_Sum += l[i]    
        
print(mini_Sum, max_Sum)        
                    

"""    