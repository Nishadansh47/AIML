# ---------------------------------------------------------------Assignment Day 4 | 3rd September 2020 -----------------------------------------------------------------------

'''Question 1 - Research on whether addition, subtraction, multiplication, division, floor division, and modulo operations
                 be performed on complex numbers. Based on your study, implement a Python program to demonstrate
                 these operations.'''

# Answer 1 --------------------
Addition = (4+3j)+(3-7j)
Subtract = (4+3j)-(3-7j)
Multiply = (4+3j)*(3-7j)
Division = (4+3j)/(3-7j)
# FloorDivision = complex(4,3)//complex(3,-7)   #(Here i commented this line of code because in python we can't take floor of complex number in such simple way,
                                                 #it throws a Type Error , we can take floor of complex numbers by using advance methods like conjugate.)
# Modulo = (4+3j)%(3-7j)  #same as above we also cant mod complex numbers without using advance functions or metbhods


print("Addition of two complex numbers : ",Addition)
print("Subtraction of two complex numbers : ",Subtract)
print("Multiplication of two complex numbers : ",Multiply)
print("Division of two complex numbers : ",Division)
# print("Floor Division of two complex numbers : ",FloorDivision)
# print("Modulo of two complex numbers : ",Modulo)

# --------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 2-Research on range() functions and its parameters. Create a markdown cell and write in your own words
              (no copy-paste from google please) what you understand about it. Implement a small program of your
              choice on the same.'''

# Answer 2 --------------------
# Range func(range()) predominantly used for 'for' loops and sometimes with while loops. It returns a sequence of numbers and is immutable (whose value is fixed).
# The range function takes one or at most three arguments, namely the start and a stop value along with a step size.    
# Range func has 3 parameters (Start arguement,stop arguement,step arguement)
# Since the range() function only stores the start, stop, and step values so the range() function can be represented in three different ways
#    >range(stop_value) : This by default considers the starting point as zero.
#    >range(start_value, stop_value) : This generates the sequence based on the start and stop value.
#    >range(start_value, stop_value, step_size): It generates the sequence by incrementing the start value using the step size until it reaches the stop value.
# EXAMPLE----
for i in range(5): #here 5 which bydefault is a stop arg.
    print(i)

for j in range (1,11): #Here 1 is start arg and 11 is stop arg
    print(j)

for k in range(0,12,3): #Here 0 is start arg, 12 is stop arg and 3 is step arg
    print(k)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 3 - Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print
                their multiplication result else print their division result.'''

a = input('Please Enter 1st Number: ')
a = int(a)
b = input('Please Enter 2nd Number: ')
b = int(b)
c = (a-b)

if c>=25:
    d = a*b
    print(f'As the subtraction result of a and b is greater then 25,so i give multiplication of a and b which is: {d}')
else:
    print(f'substraction of a and b is : {c}')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 4: Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as
               "square of that number minus 2".'''
# Answer 4----------------------
l = [2,3,4,5,6,7,8,9,10,12,13,11]
for i in l:
    if i%2==0 :
        print ((i**2)-2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 5:Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number
              is divided 2.'''

# Answer 5 ------------------

l1 = list(range(1,16))
for i in l1:
    if i>7 and i%2==0:
        print(i)