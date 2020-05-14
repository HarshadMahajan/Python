mat=[]
result=False
krow = 0; lcol = 0
row=int(input("Enter the Rows count :"))
column=int(input("Enter the columns count :"))

for i in range(row):
    mat1=[]
    for j in range(column):
        mat1.append(int(input("Enter the values for matrix :"+str(i)+" "+str(j)+" ")))
    print()
    mat.append(mat1)
for i in range(row):
    for j in range(column):
        print(mat[i][j], end=" ")
    print()

while (krow < row and lcol < column):
    
         
     # Print the first row from
     # the remaining rows  
    for i in range(lcol, column) : 
        print(mat[krow][i], end = " ") 
          
    krow += 1

    # Print the last column from 
    # the remaining columns  
    for i in range(krow, row) : 
        print(mat[i][column - 1], end = " ") 
          
    column -= 1

    # Print the last row from 
    # the remaining rows  
    if ( krow < row) : 
          
        for i in range(column - 1, (lcol - 1), -1) : 
            print(mat[row - 1][i], end = " ") 
          
        row -= 1
      
    # Print the first column from 
    # the remaining columns  
    if (lcol < column) : 
        for i in range(row - 1, krow - 1, -1) : 
            print(mat[i][lcol], end = " ") 
          
        lcol += 1


