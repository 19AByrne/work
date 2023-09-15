##exercise 1
MyFloatValue = (9.82)
print(type(MyFloatValue))
MyFloatValue == (MyFloatValue//1)
MyFloatValue = int(MyFloatValue)
print(type(MyFloatValue))
MyFloatValue = str(MyFloatValue)
print(type(MyFloatValue))

Test = ('test')
Test = int(Test)
"""
Traceback (most recent call last):
  File "<string>", line 10, in <module>
ValueError: invalid literal for int() with base 10: 'test'
"""

