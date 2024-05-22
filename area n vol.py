Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\abhin\OneDrive\Desktop\arpit py\cls 11\area n vol.py
>>> l=[1,2,3,5]
>>> 
...  
>>> l1=l
>>> l[1]=2
>>> print(l1)
[1, 2, 3, 5]
>>> l[1]=9
>>> print(l1)
[1, 9, 3, 5]
\
>>> l1=l.copy()
>>> print
<built-in function print>
>>> print(l1)
[1, 9, 3, 5]
>>> l.insert(2,183)
>>> print(l)
[1, 9, 183, 3, 5]
print(l.extend)
<built-in method extend of list object at 0x0000020E4097EB80>
print(l.extend(l1))
None
print(l)
[1, 9, 183, 3, 5, 1, 9, 3, 5]
