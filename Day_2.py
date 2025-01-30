# Day_2 ##  Check the armstrong number 
def find_armstrong(number):
    str_1=str(number)
    len_1=len(str_1)
    sum=0
    for char in str_1:
        sum+=int(char)**len_1
    return sum
number=int(input("Enter the number : "))
result=find_armstrong(number)
if result==number:
    print("It is armstrong number")
else:
    print("It is not armstrong number")
print(result)