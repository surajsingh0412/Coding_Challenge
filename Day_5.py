#####  Star Patern Using loop
n1=int(input("Enter the row number : "))
n2=int(input("Enter the column number : "))
for i in range(1,n1+1):
    for j in range(1,n2+1):
        print("*", end=" ")
    print()

## 
row=int(input("Enter the row number : "))
for i in range(1,row+1):
    print("*"*i)