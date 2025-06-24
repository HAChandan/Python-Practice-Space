'''
Given a Multiline String or a paragraph in text file(.txt extension file)
and reading the file using python file handling and counting the number of
words and repeated words and storing the result in the another file named
result.txt(.txt extension file) 
'''

import operator     # To Sort the dictionary value from heighest to lowest
import re           # Using RegEx to clean the string

'''
Reading the file string1.txt
'''

file = open("string1.txt", "r")
text = file.read()
print(text)
print()

'''
Using sub function in RegEx to remove , and ! in string
'''

text = re.sub(",", "", text)
text = re.sub("!", "", text)
text = text.lower()
print(text)
file.close()

'''
Spliting the String in to words and stored in list using split function
'''

L1 = text.split()
print(L1)
print()

words = {}
'''
Looping Through the list that contain words of a string
and counting the repeated words and stroring the words
and number of count using dictionary using key value pair
'''

for w in L1:
    if w in words:
        words[w] += 1
    else:
        words[w] = 1
print(words)
print()

'''
Sorting the counted words in the descending order
'''

SL1 = sorted(words.items(), key=operator.itemgetter(1), reverse = True)
print(SL1)


'''
Write the counted words into another new file called result.txt
'''

abc = open("result.txt", "w")
n_words = len(L1)
u_words = len(SL1)

abc.write(f"Total Number of words in the file ==> {n_words} \n")
abc.write(f"Total Number of unique words in the file ==> {u_words} \n")
abc.write(f"Unique Words with number of times the words repeating are listed below \n\n")

for n in SL1:
    a = n[0]
    b = n[1]
    abc.write(f"{a} - {b} \n")
abc.close()