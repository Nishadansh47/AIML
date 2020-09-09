# --------------------------------------------------------------DAY 5 | 4th September 2020---------------------------------------------------------------------------

'''Question 1 : Write a Python program to find the first 20 non-even prime natural numbers.'''
# Answer 1 ------------------
prime = []
for num in range(1,100):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           if num%2!=0:
               prime.append(num)
           if len(prime)>20:
            break
print(prime)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 2 : Write a Python program to implement 15 functions of string.'''
#Answer 2 --------------------------
#Method             	       Description
# 1.capitalize()	           Converts the first character to upper case
txt = "hello my name is anshul nishad ."

x = txt.capitalize()

print (x)
# -----------------------------------

# 2.center()	               Returns a centered string
txt1 = "Nishad"

x1 = txt1.center(20)

print(x1)
# -------------------------------------

#3.count()                     Returns the number of times a specified value occurs in a string
txt2 = "hello my name is anshul nishad ."

x2 = txt2.count("h")

print(x2)
# ------------------------------------------

# 4.endswith()	               Returns true if the string ends with the specified value

txt3 = "hello my name is anshul nishad ."

x3 = txt3.endswith(".")

print(x3)
# --------------------------------

# 5. find()	                   Searches the string for a specified value and returns the position of where it was found

txt4 = "hello my name is anshul nishad ."

x4 = txt4.find("nishad")

print(x4)
# -------------------------------------

# 6. format()	               Formats specified values in a string

txt5 ="hello my name is {FirstName} nishad ."
print(txt5.format(FirstName = 'anshul'))
# -------------------------------------------

# 7. index()	               Searches the string for a specified value and returns the position of where it was found

txt6 = "Hello, welcome to my world."

x6 = txt6.index("welcome")

print(x6)
# --------------------------

# 8. isalpha()	               Returns True if all characters in the string are in the alphabet

txt7 = "CompanyX"

x7 = txt7.isalpha()

print(x7)
# --------------------------------

# 9. islower()	               Returns True if all characters in the string are lower case

txt8 = "hello world!"

x8 = txt8.islower()

print(x8)
# --------------------------------------

# 10. join()	                   Joins the elements of an iterable to the end of the string

myTuple = ("John", "Peter", "Vicky")

x9 = " ".join(myTuple)

print(x9)
# ----------------------------------------

# 11. lower()	               Converts a string into lower case

txt10 = "Hello my FRIENDS"

x10 = txt10.lower()

print(x10)
# ---------------------------------

# 12. lstrip()	               Returns a left trim version of the string

txt11 = "     banana     "

x11 = txt11.lstrip()

print(x11)
# ---------------------------------------

# 13. rstrip()    	           Returns a right trim version of the string

txt12 = "     banana     "

x12 = txt12.rstrip()

print(x12)
# ----------------------------------------

# 14. replace()	               Returns a string where a specified value is replaced with a specified value

txt13 = "I like bananas"

x13 = txt13.replace("bananas", "apples")

print(x13)
# -----------------------------

# 15. upper()	               Converts a string into upper case

txt14 = "Hello my friends"

x14 = txt14.upper()

print(x14)
# -------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 3: Write a Python program to check if the given string is a Palindrome or Anagram or None of them. Display
            the message accordingly to the user.'''
# Answer 3 --------------------

input1=input("check if it is palindrome or anagram: ")


if input1==input1[::-1]:
    print("This is Palindrome")
    
else:
    input2=input("check if it is anagram: ")
    if sorted(input1)==sorted(input2):
        print("This is anagram")
    else:
        print("None of them")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Question 4: Write a Python's user-defined function that removes all the additional characters from the string and
            convert it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle @AIML Trainer",
            then the output be "drdarshaningleaimltrainer".'''
        
# Answer 4 --------------------

test_str="Dr. Darshan Ingle @AIML Trainer"
result_str=""

for i in test_str:
    if i.isalnum():
        result_str+=i

print(result_str.lower())

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------