# Built-in functions and methods in Python

'''str()
int()
print()'''
 
greet = 'Hellooooo'
print(greet[:])
# Output: Hellooooo

print(greet[0:len(greet)])
# Output: Hellooooo

# functions are reusable pieces of code that perform a specific task. They can take input, process it, and return an output.
# Methods are functions that are associated with a specific data type or object. They are called on an instance of the object and can modify the object or return a value based on the object's state.

quote = "to be or not to be"

print(quote.upper())
# Output: TO BE OR NOT TO BE

print(quote.capitalize())
# Output : To be or not be

print(quote.find('be'))
# Output : 3

print(quote.replace('be', 'me'))
# Output : to me or not to me

