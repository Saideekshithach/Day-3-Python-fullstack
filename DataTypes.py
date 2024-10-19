Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Datatypes
a=4
type(a)
<class 'int'>
b=6.8
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="code"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
f=3+9j
type(f)
<class 'complex'>
g=4j+3
type(g)
<class 'complex'>
5j
5j
h=8j
type(h)
<class 'complex'>
g=0j
type(g)
<class 'complex'>
g=4+5i
SyntaxError: invalid decimal literal
x=True
type(x)
<class 'bool'>
y=False
type(y)
<class 'bool'>
#DataType conversion
int(6)
6
int(5.6)
5
int("hi")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#float
float(5+8j)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(5+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(7)
7.0
float(8.9)
8.9
float("hello")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(True)
1.0
float(False)
0.0
#str
str(7)
'7'
str(8.9)
'8.9'
str("python")
'python'
str(True)
'True'
str(False)
'False'
str(4+9j)
'(4+9j)'
a='b'
type(a)
<class 'str'>
#complex
complex(1)
(1+0j)
>>> comples(5.6)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    comples(5.6)
NameError: name 'comples' is not defined. Did you mean: 'complex'?
>>> complex(5.6)
(5.6+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(3)
True
>>> bool(6.5)
True
>>> bool("code")
True
>>> bool(5+6j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> #int
>>> int(True)
1
>>> int(False)
0
