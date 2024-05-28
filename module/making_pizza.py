import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Syntax to import a module:
"""
module_name.function_name()
"""

# Importing Specific Functions
"""
You can also import a specific function from a module. 
Here’s the general syntax for this approach:

***from module_name import function_name***

You can import as many functions as you want from a 
module by separating each function’s name with a comma:

***from module_name import function_0, function_1, function_2***

With this syntax, you don’t need to use the dot notation when you call a
function. Because we’ve explicitly imported the function make_pizza() in the
import statement, we can call it by name when we use the function.

***from pizza import make_pizza as mp***
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

The general syntax for providing an alias is:
***from module_name import function_name as fn***

# Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

The general syntax for this approach is:
***import module_name as mn***

# Importing All Functions in a Module
You can tell Python to import every function 
in a module by using the asterisk (*) operator:

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
***from module_name import ***
"""