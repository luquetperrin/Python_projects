"""Importing All Functions in a Module"""
#from fibo import *

#fib(200)
#result = fib2(200)
#print(result)

"""Using as to Give a Module an Alias"""
#import fibo as f

#f.fib(100)
#result = f.fib2(100)
#print(result)

"""Using as to Give a Function an Alias"""
#from fibo import fib2 as fi

#result = fi(100)
#print(result)

"""Importing Specific Functions"""
from fibo import fib

fib(100)

"""
For efficiency reasons, each module is only imported once per interpreter session. 
Therefore, if you change your modules, you must restart the interpreter – or, if 
it’s just one module you want to test interactively, use importlib.reload(), 
e.g. import importlib; importlib.reload(modulename).
"""
