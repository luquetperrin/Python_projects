"""
Sets in Python are unordered collections of unique elements. 
This means that each element in a set must be unique, 
and the order of elements is not guaranteed. 
Sets are implemented using a hash table structure, 
which allows for efficient membership testing and 
elimination of duplicate elements.
"""

# Here are some key points about sets and how to use them:
"""
1. Creating Sets: Sets can be created using curly braces {} or the set() constructor. 
Elements are separated by commas within curly braces.
my_set = {1, 2, 3, 4, 5}
my_set.add(99). This will add "99" to my_set varaible.
my_set.remove(2). This will remove "2" from my_set variable
my_set.pop(). "pop" will remove any random item in my_set and return that item.

2. Unique Elements: Sets automatically eliminate duplicate elements. 
When you create a set from a list or tuple, duplicate elements are removed.

3. Membership Testing: You can quickly check if an element is present in a set using the in operator.
if 3 in my_set:
    print("3 is present in the set")

4. Set Operations: Sets support various operations like 
union, intersection, difference, and symmetric difference.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2  # or set1.union(set2)

# Intersection
intersection_set = set1 & set2  # or set1.intersection(set2)

# Difference
difference_set = set1 - set2  # or set1.difference(set2)

# Symmetric Difference
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)

5. Mutable vs. Immutable: Sets are mutable, 
meaning you can modify them after creation. 
However, the elements of a set must be immutable. 
Sets themselves are mutable, but 
their elements must be immutable.

6. When to Use Sets: Sets are useful when you need to perform operations 
like finding unique elements, membership testing, 
or set operations like union, intersection, etc. 
They are particularly efficient for membership testing 
and removing duplicates from a collection.

7. Differences from Tuples and Lists:
    a.Sets are unordered collections, while lists and tuples maintain order.
    b.Sets contain unique elements, while lists and tuples can contain duplicate elements.
    c.Sets are mutable, while tuples are immutable. Lists are mutable like sets.
"""

# Here are some exercises to practice using sets:

"""
1. Create a set of your favorite colors and print them.
2. Check if a given number is present in a set of prime numbers.
3. Find the intersection of two sets containing students who play different sports.
4. Remove duplicates from a list using a set.
5. Perform set operations like union, intersection, etc., on two sets of your choice.
"""