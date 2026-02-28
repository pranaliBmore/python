''' 
Immutability is a property of an object whose state cannot be modified after it is created. 
In Python, immutability is often associated with certain data types, such as strings, tuples, and frozensets. 
These types cannot be changed after they are created, which can help prevent unintended side effects and make code easier to reason about.

'''
selfish = '01234567'
        # 01234567
# 
selfish = selfish + '8'

print(selfish)