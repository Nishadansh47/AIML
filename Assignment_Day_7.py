# --------------------------------------------Assignment Day 7 | 8th September 2020-------------------------------------------------------

'''Question 1: Write a program to copy the contents of one file to another using a for loop.Do not use built-in copy function'''

# Answer 1 ------------------

# with open("input.txt", "r") as f:     
#     with open("output.txt", "a") as f1:
#         for line in f:
#             f1.write(line)

# ____________________________________________________________________________________________________________________________________________

'''Question 2: Write a Python program to find maximum and minimum values in the dictionary. Do not use built-in min
            and max functions.'''

# Answer 2 ------------

dic = {'a': 23, 'b': 16, 'c':52 , 'd': 14, 'e':5 }
lst = []
for y in dic.values():
    lst.append(y)

lst = sorted(lst)
print(f'The Minimum value of dictionary is {lst[0]}')
print(f'The Maximum value of dictionary is {lst[-1]}')