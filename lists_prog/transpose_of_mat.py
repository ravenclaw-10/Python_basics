#program to print the transpose of the given matrix

rows=int(input("Enter the no. of rows of matrix:"))
columns=int(input("Enter the no. of columns of matrix:"))
matrix1=[]
print("Enter matrix element row wise:")
for i in range(0,rows):
    row1=[]
    for j in range(0,columns):
        elem=int(input())
        row1.append(elem)
    matrix1.append(row1)
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix1[j][i] ,end="")
    print()    