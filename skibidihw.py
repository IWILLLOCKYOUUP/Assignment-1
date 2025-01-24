"""1. Consider the string str=”Global Warming”
Write statements in python to implement the following
a) To display the last four characters.
b) To display the substring starting from index 4 and ending at index 8.
c) To trim the first four characters from the string.
d) To display the starting index for the substring "Wa".
e) To replace all the occurrences of letter "a‟ in the string with "*"""
str="Global Warming"
print(str[10:14])
print(str[4:8])
print(str[0:4])
print(str[7:9])
a=str.replace("a","*")
print(a)

"""2. Give the output of the following statements
str='Honesty is the best policy'
str.replace('o','*')"""
str='Honesty is the best policy'
o=str.replace("o","*")
print(o)

"""3. Write the output of the following :
str= "String Slicing in Python"
a) print(str[13:18])
b) print(str[-2:-4:-2])
c) print(str[12:18:2])
d) print(str[-17:-1:1])
e) print(str[-6:-20:-2])
d) print(str[19:29])
"""
str= "String Slicing in Python"
print(str[13:18]) #g in
print(str[-2:-4:-2]) #o
print(str[12:18:2]) #n n
print(str[-17:-1:1]) #Slicing in Pytho
print(str[-6:-20:-2]) #Pn ncl
print(str[19:29]) #ython

"""4.What would be the output of the following code?
s = 'thinktank'
print(s[5:5])"""
s = 'thinktank'
print(s[5:5]) #empty space

s = 'follow'
print(s[3:8]) #low   

s = 'completed'
print(s[2:5:3]) #m

"""5. Fill the blank with the code that would give the following output."""
s = 'program'
print(s[1:6:2])

s = 'question'
print(s[-1:-8:-2])

"""6.What would be the output of the following code?"""
s = 'doubled'
print(s[1:6][1:3])

"""7. What would be the output of the following code?"""
s = 'coder'
print(s[::])

"""8. Select the correct output of the following String operations"""
str1 = 'Welcome'
print (str1[:6] + ' PYnative')
"""a) Welcome PYnative
b) WelcomPYnative
c) Welcom PYnative
d) WelcomePYnative"""

"""9. Guess the correct output of the following code?"""
str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
"""a)PYn PYnat ive PYnativ vitanYP
b)Yna PYnat tive PYnativ vitanYP
c)Yna PYnat tive PYnativ PYnativ
"""

"""10. Take a string called pineapples by using string slicing to print only apples in the console."""
s= "pineapple"
print(s[4:])
print(s[-5:])