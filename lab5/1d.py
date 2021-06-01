m = int(input("Enter m: "))
n = int(input("Enter n: "))

mat1 = []
mat2 = []
for i in range(m):
    a = list(map(int,input("\nEnter the numbers in row " + str(i+1) + ": ").strip().split()))[:n]
    mat1.append(a)
print(mat1)
for i in range(m):
    a = list(map(int,input("\nEnter the numbers in row " + str(i+1) + ": ").strip().split()))[:n]
    mat2.append(a)
print(mat2)

result = [[mat1[i][j] + mat2[i][j]  for j in range(m)] for i in range(n)]
print("\nResult: ")
print(result)