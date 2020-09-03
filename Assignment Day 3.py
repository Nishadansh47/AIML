import math      #importing  math module for question number 2

### Question 1 - Write a program to subtract two complex numbers in Python.-----------------------------------

# Answer 1 ---------------------

# Python program to subtract two complex numbers 

def subComplex( z1, z2): 
  '''function that returns a complex number after subracting'''

  return z1-z2 
  
# program code  
z1 = complex(22, 3) 
z2 = complex(10, 2) 
print( "Subtraction is : ", subComplex(z1, z2)) 
# ----------------------------------------------------------------------------------------------------------------

### Question 2- Write a program to find the fourth root of a number.----------------------------------------------
 
# Answer 2 -----------------------
x = 16
fourth_sqrt = x**(1/float(4))
print(fourth_sqrt)
# -----------------------------------------------------------------------------------------------------------------

### Question 3 - Write a program to swap two numbers in Python with the help of a temporary variable.--------------

# Answer 3 ----------

a = 10
b = 20 

temp = a #here temp is the temporary varibale used to swap the values of a and b
a = b
b = temp

print(f'The Value of "a" before swapping is 10 and after swapping is {a}')
print(f'The Value of "b" before swapping is 20 and after swapping is {b}')

# -------------------------------------------------------------------------------------------------------------------

### Question 4 - Write a program to swap two numbers in Python without using a temporary variable.-------------------

# Answer 4 --------------

x = 10
y = 5
   
# Code to swap 'x' and 'y' 
  
# x now becomes 15 
x = x + y   
  
# y becomes 10 
y = x - y  
  
# x becomes 5 
x = x - y   
print(f"Before swapping 'x' is 10 and After Swapping 'x' is {x} and Before Swapping  'y' is 5 and After Swapping 'y' is {y}")

# ------------------------------------------------------------------------------------------------------------------------

### Question 5 - Write a program to convert Fahrenheit to kelvin and celsius both.----------------------------------------

# Answer 5--------

# Fahrenheit to Kelvin & Celsius conversion

# Reading temperature in Celsius
temperature = float(input("Please enter temperature in fahrenheit:"))

# Converting
#Converts Fahrenheit in Celsius
celsius = (temperature - 32) * 5 /9

#Converts Fahrenheit in Kelvin
kelvin = 273.15 + celsius

#Output
print('%0.2f Fahrenheit = %0.3f Celsius.' % (temperature,celsius)) #Output of Fahrenheit to Celsius
print('%0.2f Fahrenheit = %0.3f Kelvin.' % (temperature, kelvin))  #Output of Fahrenheit to Kelvin

### Question 6 - Write a program to demonstrate all the available data types in Python. Hint: Use type() function.---------

#Answer 6 ----------

# So there are 5 main datatypes in Python as described below
  # 1.Numbers
  #   a.Int 
  #   b.Float 
  #   c.Complex
  # 2.Strings
  # 3.List 
  # 4.Tuple 
  # 5.Set 
  # 6.Dictionary

# now code to classify all the datatypes 
l = [1, 2.0 ,(2+2j), "Nishad",[1,2,3],(4,5,6),{7,8,9},{'a':10, 'b':11, 'c':12}]

for i in l:
  print(f'Datatype of {i} is : {type(i)}')
