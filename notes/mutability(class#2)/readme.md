### Mutable
When value of a variable can be changed over time is called mutable.

Example:
```
x = [1, 2, 3]
print(x) # [1, 2, 3]
print(id(x)) # 139912816421064

x.pop()
print(x) # [1, 2]
print(id(x)) # 139912816421064

```
In this example, x is list in python and its value and memory address is [1, 2, 3] and 139912816421064.But value of this list can be modified [1, 2] and its memory address is not changed 139912816421064.

Some of Python’s mutable data types are: lists, byte arrays, sets, and dictionaries.

### Immutable:
When value of a variable can not be changed over time is called mutable.

Example:
```
1. age = 42
2. print(age) # 42
3. print(id(age)) # 10966208

4. age = 43
5. print(age) # 43
6. print(id(age)) # 10966240

```
In avobe example,variable is initialized with value 42 and its memory address is 10966208. In line 4,we changed the value of 'age' to 43.So, Can't we say that it is mutable as its value is changed?

Actually, the answer is no.If we look closely we can see that the memory address of 'age' variable is changed to 10966240.That means a new variable initialized with the same name!

That's why it is immutable. Some immutable types of python include numeric data types, strings, bytes, frozen sets, and tuples.

### References:
https://towardsdatascience.com/immutable-vs-mutable-data-types-in-python-e8a9a6fcfbdc
