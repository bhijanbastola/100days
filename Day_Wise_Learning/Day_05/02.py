#Recurision

#implementing memomization to optimize the recursive fibonacci function
#from functools import cache

#
cache = {0:0, 1:1}
def fib(n):
    if n in cache:
        return cache[n]
    else:

        res=fib(n-1) + fib(n-2)
        cache[n] = res
        return res

print(fib(10))  # Output: 55

#using dictionary to store the values of factorial
m={0:1,1:1}
def factorial(n):
    if n in m:
        return m[n]
    else:
        res = n * factorial(n - 1)
        m[n] = res
        return res

print(factorial(5))  # Output: 120

#using list to store the values of factorial
l=[1,1]
def factorial1(n):
    if n < len(l):
        return l[n]
    else:
        res = n * factorial1(n - 1)
        l.append(res)   
        return res


print(factorial1(5))  