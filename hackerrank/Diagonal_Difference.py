n = int(input())
matrix = []
prim_Sum = 0
sec_Sum = 0
for i in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

for i  in range(n):
    for j in range(n):
        if i == j:
            prim_Sum += matrix[i][j]
        if i + j == n - 1:
            sec_Sum += matrix[i][j]  
print(abs(prim_Sum - sec_Sum))