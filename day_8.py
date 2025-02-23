#You are given a list of integers. Write a python function that returns a new list where each element is
#  the square of the corresponding element in the input list. Output: [1, 4, 9, 16], n=[-1,-2,3,4]

#  1st Method
a=[]
n=[-1,-2,3,4]
for i in n:
    sqr=i**2
    a.append(sqr)
print(a)


#  2nd Method
def find_sqr(n):
        return [i**2 for i in n]
n=[-1,-2,3,4]
result=find_sqr(n)
print(result)


#  3rd Method
a=[]
def find_sqr(n):
    for i in n:
        sqr=i**2
        a.append(sqr)
    print(a)
n=[-1,-2,-3,4]
find_sqr(n)