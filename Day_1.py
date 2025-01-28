### Palindrom Number Check  use simple way (slicing)
word=input("Enter the character : ")
word=word.lower()
if word==word[::-1]:
    print(f"{word} is palindrom ")
else:
    print(word,"is not palindrom ")


### Palindrom Number Check  using for loop 

def check_palindrom(str):
    rev=""
    for char in str:
        rev=char+rev
    return rev
str=input(f"Enter the character for check palindrom :")
reverse=check_palindrom(str)
if reverse==str:
    print(f"it's palindrom ")
else:
    print("it's not palindrom ")
print(reverse,"it's reverse of given character")

###  Fibonacci series using simple way using while loop
# def fibonacci_series(number):
#     a,b=0,1
#     while a<number:
#         print(a,end=",")
#         a,b=b,a+b
# number=int(input("Enter the number: "))
# result=fibonacci_series(number)


###  Fibonacci series using simple way using while loop with def function
def fibonacci_series(number):
    a,b=0,1
    c=[]
    while a<number:
        c.append(a)
        a,b=b,a+b
    print(c)
number=int(input("Enter the number: "))
result=fibonacci_series(number)
