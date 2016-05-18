#################################
# In Class Assignment and Homework
#################################

# 1. Write a decorator that prints the runtime of a function

import time


def decorator(input_function):

    def decorated_function():
        print 'decorated_function called'
        start_time = time.time()
        input_function()
        end_time = time.time()
        print "Runtime was %s" % (end_time - start_time)

    return decorated_function


@decorator
def to_be_decorated():
    print '1 to_be_decorated called'
    time.sleep(1)
    print '2 asto_be_decorated called'


to_be_decorated()


# 2. Write a memoized fibonacci calculator

# Credit: http://www.python-course.eu/python3_memoization.php


def memoize(f):

    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # n=3, 2          1
        return fib(n-1) + fib(n-2)


# fib = memoize(fib)

# f = 0 1 1 2 3 5 8 13 21 34 55
# i = 0 1 2 3 4 5 6 7  8  9  10
print(fib(3))
