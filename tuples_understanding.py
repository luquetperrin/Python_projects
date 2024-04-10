# Basics of tuples in python
#  tuples are identical to lists in all respects, except two. 
# They are immutable and are defined by enclosing the elements 
# in parentheses instead of square brackets.

tuple1 = (12, 6, -8, 'Perrin', False, 12, 6, 98)

tuple2 = (45, 67, 90, 201, 245, 600)

#tuple3 = (tuple1, tuple2)

#print(tuple3)

#print(tuple3[1])
#print(len(tuple3))

# Tuple concatenation
tuple3 = tuple1 + tuple2
print(tuple3)

# Using of "count" within a tuple
print(tuple3.count(12))

# Conversion of a list into a tuple
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(list1))

# Conversion of a tuple into in a list
print(list(tuple1))

tuple5 = (10,)*5
print(tuple5)
