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

#Answer 1 ----------------

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


'''Question 3: Create your own Jupyter Notebook for Sets. Reference link:
            https://www.w3schools.com/python/python_sets.asp'''

# Answer 3 -----------------

MuJupyterNotebook = ('https://colab.research.google.com/drive/1L8WJ1ynTfM8WXgcc9XGBlQy5veYVwAAr?usp=sharing')

# ________________________________________________________________________________________________________________________________________

'''Question 4: Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no
            duplicates.
            Input Format:
            The first line contains n-1 numbers with each number separated by a space.
            Output Format:
            Print the missing number
            Example:
            Input:
            1 2 4 6 3 7 8
            Output:
            5
            Explanation:
            In the above list of numbers 5 is missing and hence 5 is the input'''

# Answer 4 -----------------

list1 = input("enter numbers sequence seprated by spaces:")
list2 = []
list3 = []
for elem in list1:
    list2.append(elem.strip())
for x in list2:
    if x == "":
        list2.remove(x)
for y in list2:
    list3.append(int(y))
list3 = sorted(list3)
missing_item = [c for c in range(list3[0], list3[-1]+1) if c not in list3]
print(missing_item)  

# __________________________________________________________________________________________________________________________________

'''Question 5: With a given list L, write a program to print this list L after removing all duplicate values with original order
            reserved.
            Example:
            If the input list is
            12 24 35 24 88 120 155 88 120 155
            Then the output should be
            12 24 35 88 120 155
            Explanation:
            Third, the seventh and ninth element of the list L has been removed because it was already present.
            Input Format:
            In one line take the elements of the list L with each element separated by a space.
            Output Format:
            Print the elements of the modified list in one line with each element separated by a space.
            Example:
            Input:
            12 24 35 24
            Output:
            12 24 35'''

# Answer 5 -------------

list1 = input('Enter any numbers seperated by spaces also some duplicates:')
list2 = [x for x in list1.split(" ")]
list2 = set(list2)
list3 = sorted(list(list2))
for i in list3:
    print(i, end= " ")
# __________________________________________________________________________________________________________________________