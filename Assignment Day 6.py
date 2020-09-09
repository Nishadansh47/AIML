'''Question 1 :
               Assuming that we have some email addresses in the "username@companyname.com" format, please
               write a program to print the company name of a given email address. Both user names and company
               names are composed of letters only.
               Input Format:
               The first line of the input contains an email address.
               Output Format:
               Print the company name in a single line.
               Example;
               Input:
               john@google.com
               Output:
               google. '''

# Answer 1 ----------------

email = input('Enter Your Email in the format of "username@company.com":')
str1 = email.index("@") +1
company = email[str1:(len(email)-4)]
print(company)
# ___________________________________________________________________________________________________________________________________________________________________

'''Question 2 :
            Write a program that accepts a comma-separated sequence of words as input and prints the words in a
            comma-separated sequence after sorting them alphabetically.
            Input Format:
            The first line of input contains words separated by the comma.
            Output Format:
            Print the sorted words separated by the comma.
            Example:
            Input:
            without,hello,bag,world
            Output:
            bag,hello,without,world. '''

# Answer 2 ------------------------------

y = input('Enter coma seperated string(ex-hi,i,am,nishad):').split(',')
y1 = sorted(y)
sorted_str = (",").join(y1)
print(sorted_str)

# _____________________________________________________________________________________________________________________________________________
