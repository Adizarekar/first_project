Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
math.sqrt(16)
4.0
math.pow(2,5)
32.0
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.floor(2.3)
2
math.ceil(2.345)
3
math.ceil(2.567)
3
import calendar
cal = calendar.month(2023,01)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
cal = calendar.month(2023,1)
print(cal)
    January 2023
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

calendar.isleap(2023)
False


dir(calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_get_default_locale', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']



f= open("F://Education//DS_Roadmap//first_project//book.txt","r")
s= f.read()
>>> s
'{"tom": {"name": "tom", "address": "asd,dfg,NY", "phone": 4636483479}, "bob": {"name": "bob", "address": "wder,rtyt, paris", "phone": 9876543987}}'
>>> import json
>>> book = json.loads(s)
>>> book
{'tom': {'name': 'tom', 'address': 'asd,dfg,NY', 'phone': 4636483479}, 'bob': {'name': 'bob', 'address': 'wder,rtyt, paris', 'phone': 9876543987}}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> book['bob']
{'name': 'bob', 'address': 'wder,rtyt, paris', 'phone': 9876543987}
>>> book['bob']['phone']
9876543987
>>> 
>>> for i in book:
...     print(book[i])
... 
...     
{'name': 'tom', 'address': 'asd,dfg,NY', 'phone': 4636483479}
{'name': 'bob', 'address': 'wder,rtyt, paris', 'phone': 9876543987}
>>> 
>>> 
>>> for i in book:
...     print(i)
... 
...     
tom
bob
>>>  book['bob']['phone']
...  
SyntaxError: unexpected indent
>>> 
>>> 
>>> __name__
'__main__'
