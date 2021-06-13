Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> print('30 days 30 hour challenge')
30 days 30 hour challenge
>>> Hours = "thirty"
>>> print(Hours)
thirty
>>> Days = "Thirty days"
>>> print(Days[1])
h
>>> Challenge="I will win"
>>> print(Challenge[7:10])
win
>>> print(len(Challenge))
10
>>> print(Challenge.lower())
i will win
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+b
>>> print(c)
30 Days30 hours
>>> text = "Thirty days and Thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> y="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
>>> print(y.capitalize())
Don't trouble trouble until trouble troubles you
>>> print(y.find(D))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(y.find(D))
NameError: name 'D' is not defined
>>> print(y.find("UNTIL"))
22
>>> print(y.isalpha())
False
>>> print(y.isnum())
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(y.isnum())
AttributeError: 'str' object has no attribute 'isnum'
>>> print(y.isalnum())
False
>>> 