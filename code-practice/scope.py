"""
http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html

the part of a program where a variable is accessible its scope, and the duration for which the variable exists its lifetime.
"""





def my_function():
    a = 0
    nonlocal a
    # print(a)
    a = 3
    print(a)


my_function()

print(a)
