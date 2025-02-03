## Factorial number using Recursion 

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the value : "))
result=factorial(n)
print(result)

### It is best case for factorial 
def factorial(n):
    if n<0:
        return "Please give positive number ."
    fact=1
    for i in range(1,n+1):
        fact*=i
    return result
n=int(input("Enter the number : "))
result=factorial(n)
print(result)