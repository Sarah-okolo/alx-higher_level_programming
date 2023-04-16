## [0. Lookup](0-lookup.py)
A function that returns the list of available attributes and methods of an object:

- Prototype: ```def lookup(obj):```
- Returns a list object
- not allowed to import any module

## [1. My list](1-my_list.py)
A class **MyList** that inherits from **list**:

- Public instance method: ```def print_sorted(self):``` 
- Prints the list, but sorted (ascending sort)
- Assumed that all the elements of the list will be of type int
- You are not allowed to import any module

## [2. Exact same object](2-is_same_class.py)
A function that returns **True** if the object is exactly an instance of the specified class ; otherwise **False**.

- Prototype: ```def is_same_class(obj, a_class):```
- Not allowed to import any module

## [3. Same class or inherit from](3-is_kind_of_class.py)
A unction that returns **True** if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise **False**.

- Prototype: ```def is_kind_of_class(obj, a_class):```
- Not allowed to import any module

## [4. Only sub class of](4-inherits_from.py)
A function that returns **True** if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise **False**.

- Prototype: ```def inherits_from(obj, a_class):```
- Not allowed to import any module

## [5. Geometry module](5-base_geometry.py)
An empty class ```BaseGeometry```.

- Not allowed to import any module

## [6. Improve Geometry](6-base_geometry.py)
A class ```BaseGeometry```(based on [5-base_geometry.py](5-base_geometry.py) ).

- Public instance method: ```def area(self):```
- Raises an Exception with the message area() is not implemented
- Not allowed to import any module

## [7. Integer validator](7-base_geometry.py)
A class ```BaseGeometry``` (based on [6-base_geometry.py](6-base_geometry.py) ).

- Public instance method:``` def area(self):``` that raises an Exception with the message area() is not implemented
Public instance method: ```def integer_validator(self, name, value):``` that validates value:
- Assume name is always a string
- If value is not an integer: raise a `TypeError`exception, with the message <name> must be an integer
- If value is less or equal to 0: raise a `ValueError` exception with the message <name> must be greater than 0
- Not allowed to import any module

## [8. Rectangle](8-rectangle.py)
A class Rectangle that inherits from ```BaseGeometry``` ( [7-base_geometry.py](7-base_geometry.py) ).

- Instantiation with width and height: ```def __init__(self, width, height):```
- Width and height is private. No getter or setter
- Width and height is positive integers, validated by integer_validator

## [9. Full rectangle](9-rectangle.py)
 A class Rectangle that inherits from ```BaseGeometry``` ( [7-base_geometry.py](7-base_geometry.py) ). (task based on [8-rectangle.py](8-rectangle.py) )

- Instantiation with width and height: ```def __init__(self, width, height)::```
- Width and height must be private. No getter or setter
- Width and height must be positive integers validated by integer_validator
- The `area()` method must be implemented
- `print()`should print, and `str()` should return, the following rectangle description: [Rectangle] <width>/<height>

## [10. Square #1](10-square.py)
A class Square that inherits from `Rectangle` ( [9-rectangle.py](9-rectangle.py) )

- Instantiation with size: ```def __init__(self, size)::```
- Size must be private. No getter or setter
- Size must be a positive integer, validated by integer_validator
- The `area()` method must be implemented

## [11. Square #2](11-square.py)
A class Square that inherits from `Rectangle` ( [9-rectangle.py](9-rectangle.py) ). (task based on [10-square.py](10-square.py) ).

- Instantiation with size: ```def __init__(self, size)::```
- Size must be private. No getter or setter
- Size must be a positive integer, validated by integer_validator
- The `area()` method must be implemented
- `print()` should print, and `str()` should return, the square description: [Square] <width>/<height>






