"""
* lists may be modiefied
* tuples are leaner yet not mutable
"""

names = ['Ronnie', 'Mona', 'Jack']

names[2] = 'Fred'
print(names)

names_tuple = ('Ronnie', 'Mona', 'Jack',)

# this will result in an error
names_tuple[2] = 'Fred'