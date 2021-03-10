# Python has 4 main built-in containers for storing multiple bits of data. These 4 types can store any other data type, including more containers.
# We access values in containers using brackets: [ and ]

print('=== Data Types')

# Tuples are read-only containers created using parentheses ( and ).
print('Tuples:')
a_tuple = ('some tuple', 123, 56.0, True, False, 123, 'hello')

# Access an item in a tuple
print(a_tuple[0])
print(a_tuple[2])

# Tuples support two additional methods. count() and index().
# count() tells you how many times an item appears in a tuple.
print(a_tuple.count(56.0))
print(a_tuple.count(123))
print(a_tuple.count('a value that does not exist'))

# index() tells you where in the tuple an item appears. The index starts at 0.
print(a_tuple.index('hello'))
print(a_tuple.index('some tuple'))

# What happens if you try to find out the index for an item that does not exist in the tuple?

# What happens if we try to change a value at a specific index? e.g. a_tuple[0] = 123


# Lists are similar to tuples but they can be changed (they are "mutable"), and have additional methods.
print('=== Lists')

print('TODO: Add examples.')
