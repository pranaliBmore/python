# Formatted String Examples

name = "Pranali"
age = 18

# Using concatenation
print('Hello ' + name +' You are ' + str(age) + ' years old \n')

# Using the f string method
print(f'\nHello {name}. You are {age} years old.\n')

# Using format() method
print('\nHello {}. You are {} years old.\n'.format('Pranali', 18))

print('\nHelllo {}. You are {} years old.\n'.format(name, age))

# Using positional arguments in format() method
print('\nHello {1}. You are {0} years old.\n'.format(name, age))

# Using keyword arguments in format() method
print('\nHello {new_name}. You are {age} years old.\n'.format(new_name='Pratiksha', age=25))