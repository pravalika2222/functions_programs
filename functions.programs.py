'''doc string : inside a function if we keep anything 3 times double code (or) one single code is called as "doc string"'''
# def a():
#     '''location:Briyani 12pm
#         the time is now 2:00pm
#         we are going to eat now'''
# print(a.__doc__)

"default arg function : yhe function having default values , if we want to change we can change the value"
# def a(room='python',date=2):
#     print('room:',room)
#     print('date:',date)
# a()
# a(date=5)
# a('advance python')

'''addition of two numbers using functions'''
# def a(p,r):
#     b=p+r
#     c=p+r
#     print('sum is',b)
#     print('sum is',c)
# a(1,2)            # first it will be added to both variables
# a(1.2,2.1)        # later it will be added to both variables

'''add return'''
# def sum(p,r):
#     b=p+r
#     return b
# x=sum(2,23)
# print('sum is',x)       # sum is 25
# y=sum(23,2)
# print('sum is',y)       # sum is 25

'''even odd using functions'''
# def p(num):
#     if num%2==0:
#         print(num,'is even')
#     else:
#         print(num,'is odd')
# n=int(input())
# p(n)            # input given 102   so 102 is even
# p(23)           # 23 is odd
# p(2)            # 2 is even

'''filter():function that returns even number from a list'''
# def a(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# b=[int (x) for x in input().split()]
# y=list(filter(a,b))
# print('from the b the a values are:',y)

'''filter():function that returns odd number from a list'''
# def a(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
# b=[int(x) for x in input().split()]
# y=list(filter(a,b))
# print('from the b the a values are:',y)

'''lambda:functions to calculate sum of two numbers'''
# a=lambda x,y,z:x+y+z
# b=lambda x,y,z:x*y*z           # this two are the lambda functions         
# c=a(1,2,3)
# d=b(3,2,1)                   # this two are the lambda function calling
# print('sum=',c)       # 6
# print('mul=',d)       # 6

'''a lambda function thst return bigger number'''
# x=lambda a,b:a if a>b else b
# a,b=[int(z) for z in input().split()]
# print(x(a,b))
# y=[int(x) for x in input().split()]
# print('bigger number is:',max(y))
# print('smaller number:',min(y))

'''a lambda function that returns even numbers from a list'''
# a=[int(x) for x in input().split()]
# b=list(filter(lambda x:(x%2==0),a))
# c=list(filter(lambda x:(x%2!=0),a))
# print(b)
# print(c)

'''lambda map:lambda that return squares'''
# a=[1,2,3,4,5,6]
# b=list(map(lambda x:x**2,a))           # [1, 4, 9, 16, 25, 36]
# c=list(map(lambda x:x+2,a))              #[3, 4, 5, 6, 7,8]
# d=list(map(lambda x:x-2,a))               #[-1, 0, 1, 2, 3, 4]
# print(b)
# print(c)
# print(d)

'''lambda reduce'''
# from functools import*
# a=[1,2,3,4]
# b=reduce(lambda x,y:x,a)
# c=reduce(lambda x,y:y,a)
# d=reduce(lambda x,y:x+y,a)
# e=reduce(lambda x,y:x-y,a)
# print(b)
# print(c)
# print(d)
# print(e)


