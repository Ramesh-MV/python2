Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'hello'
>>> s.endswith('e')
False
>>> s.endswith('o')
True
>>> s.expandtabs
<built-in method expandtabs of str object at 0x026DC4A0>
>>> s.find('o')
4
>>> s.find('x')
-1
>>> s.format()
'hello'
>>> s.index('o')
4
>>> s.index('x')

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.index('x')
ValueError: substring not found
>>> 
>>> s.isalnum()
True
>>> s.isalpha()
True
>>> s = 'hello12'
>>> s.isalpha()
False
>>> s.isdigit()
False
>>> s = '123'
>>> s.isdigit()
True
>>> s.islower()
False
>>> s
'123'
>>> s = 'hello'
>>> s.islower()
True
>>> s.isupper()
False
>>> s.upper()
'HELLO'
>>> 
>>> 
>>> 
>>> x = klj

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x = klj
NameError: name 'klj' is not defined
>>> 
>>> 
>>> 
>>> s = 'hello this is sekhar'
>>> 
>>> 
>>> l = [1,2,3,'hello','ji']
>>> s = 'hello'
>>> s.isspace()
False
>>> s.istitle()
False
>>> s.title()
'Hello'
>>> s = 'hello this is sekhar'
>>> s.title()
'Hello This Is Sekhar'
>>> s = 'hello'
>>> r = '@'
>>> r.join(s)
'h@e@l@l@o'
>>> r = 'mam'
>>> r.join(s)
'hmamemamlmamlmamo'
>>> r.join('hello')
'hmamemamlmamlmamo'
>>> 
>>> 
>>> 
>>> s = 'hi'
>>> s1='ji'
>>> s.join(s1)
'jhii'
>>> s.join('hello')
'hhiehilhilhio'
>>> s = list('yello')
>>> s
['y', 'e', 'l', 'l', 'o']
>>> s[0]='H'
>>> s
['H', 'e', 'l', 'l', 'o']
>>> ','.join(s)
'H,e,l,l,o'
>>> ''.join(s)
'Hello'
>>> s = 'hello'
>>> s.strip()
'hello'
>>> s = '         hello            '
>>> s.strip()
'hello'
>>> s.lstrip()
'hello            '
>>> s.rstrip()
'         hello'
>>> s.partition('h')
('         ', 'h', 'ello            ')
>>> s = 'hello'
>>> s.partition('h')
('', 'h', 'ello')
>>> s.rstrip()
KeyboardInterrupt
>>> s.replace('hello','sekhar')
'sekhar'
>>> s
'hello'
>>> s.zfill(10)
'00000hello'
>>> s = '123'
>>> int(s)
123
>>> 
