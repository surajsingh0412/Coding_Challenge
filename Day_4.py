# number=int(input("Enter the number for write table : "))
# for i in range(1,11):
#     print(f"{number} X {i} = {number*i}")


# num=int(input("Enter the number for write table : "))
# mul=1
# while mul<11:
#     print(f"{num} X {mul} = {num*mul}")
#     mul+=1

### Table make using function and for loop                 =====
def find_table(number):
    table= ""
    for i in range(1,11):
        table += f"{number}X{i} = {number*i},"
    return table
number=int(input("Enter the number : "))
result=find_table(number)
print(result)
