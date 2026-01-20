# Fundamental Data Types 

int 
float 
bool
str
list 
tuple
set
dict

# classes -> custom types

# Specialized Data Types

# Numbers
# int 
# float

print( 2 + 4 )
print( 2 - 4 )
print( 2 / 4 )
print( 2 * 4 )


# Checking the type of the result

print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))  # 0.5 is float
print(type(9 + 1.9)) # int + float = float


print(2 ** 3) # exponentiation
print(5 // 4) # floor division
print(6 % 4) # modulus

# math functions
# https://docs.python.org/3/library/math.html

print(round(3.1))
print(abs(-20))

# Strings
print(type("Hi there!"))

# long strings using triple quotes
long_string = '''
WOW
O O
---
'''
print(long_string)

# String concatenation
first_name = "Pranali"
last_name = "More"
full_name = first_name + " " + last_name
print(full_name)
