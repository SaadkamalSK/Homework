### Task 1: Python Classes
#1a. Define a class named Student with the following attributes: student_id, student_name, and class_name. Use the __init__ method to initialize these attributes.

# class student():
#     def __init__(self, student_id: int, student_name: str, class_name: str):
#         self.id=student_id
#         self.studentname=student_name
#         self.classname=class_name

#1b. Create an instance of the Student class named student with the following details: ‘V12’ as student_id, ‘Frank Gibson’ as student_name, and ‘V’ as class_name.
# class student():
#     def __init__(self, student_id, student_name: str, class_name: str):
#         self.id=student_id
#         self.studentname=student_name
#         self.classname=class_name
# student1=student("V12","Frank Gibson","V")

#1c. Print the dictionary representation of the student object using the following method: ``` __dict__ ```
# class student():
#     def __init__(self, student_id, student_name: str, class_name: str):
#         self.id=student_id
#         self.studentname=student_name
#         self.classname=class_name
# print(student.__dict__)

#2a. Import the math module: This module provides access to mathematical functions defined by the C standard
# import math

#2b. Define a class named Circle: This class will have two methods: calculate_circle_area and calculate_circle_perimeter These should include the correct calculations

# import math
# from math import pi
# class circle():
#     def calculate_circle_area(x):
#         return pi*x**2
#     def calculate_circle_perimeter(y):
#         return pi*2*y

#2c. Create an instance of the Circle class: Prompt the user to input the radius of the circle, then create an instance of the Circle class with this radius.

# import math
# from math import pi
# class circle():
#     def calculate_circle_area(self, x: float):
#         return pi*x**2
#     def calculate_circle_perimeter(self, y: float):
#         return pi*2*y
    
# circleradius=circle()
# circleradius_value=float(input("Input the radius of the circle: "))
# print(f"Circle area is {circleradius.calculate_circle_area(circleradius_value):.2f} and Circle perimeter is: {circleradius.calculate_circle_perimeter(circleradius_value):.2f}")

##### Constructors and Destructors
#3a. Create a class Person with a constructor that initializes two attributes: name and age. Also, define a destructor that prints a message with the Person name attribute when an object of this class is destroyed.

# class person():
#     def __init__(self, name: str, age: int):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print(f"{self.name} object has been destroyed")

#3b. Create a Person object from 3a and then delete the object using the del command.
# class person():
#     def __init__(self, name: str, age: int):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print(f"({self.name} {self.age}) as an object has been destroyed")
    
# object=person("Saad", 24)
# print(object.name, object.age)


### Task 2: Inheritance and Polymorphism

#1a. Create a class Animal with a method eat that prints “Eating…”. Then create a class Dog that inherits from Animal and has a method bark that prints “Barking…”.

# class animal():
#     def eat(self):
#         print("Esting...")
# class dog(animal):
#     def bark(self):
#         print("Barking...")

# 1b. Create an object of the Dog class. Call the eat method from the Animal class Call the bark method from the Dog class

# class animal():
#     def eat(self):
#         print("Eating...")
# class dog(animal):
#     def bark(self):
#         print("Barking...")

# object=dog()
# object.eat()
# object.bark()

#2a. Create a class Person with a constructor that initializes an attribute name.
# class person():
#     def __init__(self, name: str):
#         self.name=name

#2b. Create a class Employee that inherits from Person and also has an attribute id.

# class person():
#     def __init__(self, name: str):
#         self.name=name
# class employee(person):
#     def __init__(self, name: str, id):
#         super().__init__(name)
#         self.id=id

#2c. Create an object of the Employee class.

# class person():
#     def __init__(self, name: str):
#         self.name=name
# class employee(person):
#     def __init__(self, name: str, id):
#         super().__init__(name)
#         self.id=id
# object=employee("Saad",1)

#2d. Print the name and id of the employee.

# class person():
#     def __init__(self, name: str):
#         self.name=name
# class employee(person):
#     def __init__(self, name: str, id):
#         super().__init__(name)
#         self.id=id
# employee1=employee("Saad",1)
# print(f"Employee Name: {employee1.name} and ID is: {employee1.id}")


### Task 3: Encapsulation

#1a. Create a class Person with two private attributes: name and age. Provide getter and setter methods for these attributes.


# class persom():
#     def __init__(self, name:str, age:int):
#         self.__name=name
#         self.__age=age
#     @property
#     def Name(self):
#         return self.__name
#     @property
#     def Age(self):
#         return self.__age
#     @Name.setter
#     def Name(self, x):
#         self.__name=x
#     @Age.setter
#     def Age(self, y):
#         self.__age=y
        

# 1b. Create an object of the Person class. Get the name and age using the getter methods. Set the name and age using the setter methods. Get the updated name and age

# class person():
#     def __init__(self, name:str, age:int):
#         self.__name=name
#         self.__age=age
#     @property
#     def Name(self):
#         return self.__name
#     @property
#     def Age(self):
#         return self.__age
#     @Name.setter
#     def Name(self, x):
#         self.__name=x
#     @Age.setter
#     def Age(self, y):
#         self.__age=y
# nameandage=person("Saad",24)
# print(nameandage.Name, nameandage.Age)
# nameandage.Name="Alex"
# nameandage.Age=25
# print(nameandage.Name,nameandage.Age)

#2a. Create a class Circle with a private attribute radius. Provide getter and setter methods for this attribute. Also provide a method area that calculates the area of the circle.

# class circle:

#     def __init__(self, radius):
#         self.__radius=radius
#     @property
#     def Radius(self):
#         return self.__radius
#     @Radius.setter
#     def Radius(self,x):
#         self.__radius=x
#     def areofcircle(self, radius):
#         import math
#         from math import pi
#         return self.__radius**self.__radius*pi

#2b. Create an object of the Circle class. Get the radius using the getter method. Calculate and print the area of the circle. Set the radius using the setter method.

# import math
# class circle():
#     def __init__(self, radius: float):
#         self.__radius=radius
#     @property
#     def Radius(self):
#         return self.__radius
#     @Radius.setter
#     def Radius(self,x):
#         self.__radius=x
#     def areofcircle(self):
#         from math import pi
#         return self.__radius**2*pi
# y=input("Whta is the radius of the circle? ")
# areofthecircle=circle(float(y))
# print(f"The area of the circle is : {areofthecircle.areofcircle():.2f}")

#2c. Get the updated radius and calculate the new area.

# import math
# class circle():
#     def __init__(self, radius: float):
#         self.__radius=radius
#     @property
#     def Radius(self):
#         return self.__radius
#     @Radius.setter
#     def Radius(self,value):
#         self.__radius=value
#     def areofcircle(self):
#         from math import pi
#         return self.__radius**2*pi
# y=input("What is the radius of the circle? ")
# areofthecircle=circle(float(y))
# print(f"The area of the circle is : {areofthecircle.areofcircle():.2f}")
# y=input("What is the radius of the second circle? ")
# areofthecircle=circle(float(y))
# print(f"The area of the second circle is : {areofthecircle.areofcircle():.2f}")



### Task 4: Exception Handling
#1. Write a Python program to handle an error that occurs when you try to divide by zero.

# random_numbers=[1,2,3,4,5,6,7,8,9,0]
# for value in random_numbers:
#     try:
#         print(5/value)
#     except ZeroDivisionError:
#         print("ZeroDivisionError")


#2. Write a Python program to handle an error that occurs when you try to convert a string to an integer.
# radom_inputs=[2,3,6,"Alex","Hello"]
# for value in radom_inputs:
#     try:
#         print(int(value))
#     except ValueError:
#         print("Cannot covert a string to an integer")

#3. Write a Python program to handle an error that occurs when you try to open a file that doesn’t exist.
# import csv
# try:
#     file=open("filename.csv","r")
#     content=csv.reader(file)
# except FileNotFoundError:
#     print("Entered file name do not exist!")

#4. Write a Python program that uses a try/except/else block. The else block should run if no exceptions were raised in the try block.

# random_list=[1,4,5,6,"Hello",0,"Name"]
# for value in random_list:
#     try:
#         print(5/int(value))
#     except (ValueError, ZeroDivisionError):
#         print("Invalid entry!")
#     else:
#         print("No exception!")

#6. Write a Python program to handle an error that occurs when you try to convert a string to an integer. Use a finally block to print a message regardless of whether an exception was raised.

# random_list=[1,4,5,6,"Hello",0,"Name"]
# for value in random_list:
#     try:
#         print(5/int(value))
#     except (ValueError, ZeroDivisionError):
#         print("Invalid entry!")
#     finally:
#         print("Entry stored")


### Task 5: Functional Programming

#1a. Write a lambda function that takes two numbers and returns their sum. ``` sum = lambda x, y: x + y ```
# sum=lambda x,y: x+y

#1b. Print the result.
# sum=lambda x,y: x+y
# print(sum(1,1))

#2a. Write a lambda function that takes a string and returns its length.
#2c. Print the result.
# lenght=lambda x: len(x)
# print(lenght("Hello"))

#3a. Use the map function and a lambda function to square all numbers in a list. ``` numbers = [1, 2, 3, 4, 5] ```
#3b. Convert the map object to a list and print it.
# numbers = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x**2, numbers)))

#4a. Use the filter function and a lambda function to remove all odd numbers from a list. ``` numbers = [1, 2, 3, 4, 5] ```
#4b. Convert the filter object to a list and print it.
# numbers = [1, 2, 3, 4, 5]
# print(list(filter(lambda x: x%2!=0,numbers)))


#5a. Use the reduce function and a lambda function to find the product of all numbers in a list. ``` from functools import reduce numbers = [1, 2, 3, 4, 5] ```
#5b. Print the product
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# print(reduce(lambda y, x: y*x, numbers))

#6a. Use the map function and a lambda function to convert all strings in a list to uppercase. ``` strings = ['hello', 'world'] ```
#6b. Convert the map object to a list and print it.
# strings = ['hello', 'world']
# print(list(map(lambda x: x.upper(),strings)))


#7a. Use the filter function and a lambda function to remove all strings from a list that have length less than 5. ``` ['hello', 'hi', 'world', 'cat'] ```
#7b. Convert the filter object to a list and print it.
# my_list=['hello', 'hi', 'world', 'cat']
# print(list(filter(lambda x: len(x)>=5,my_list)))

#8a. Use the reduce function and a lambda function to concatenate all strings in a list. ``` from functools import reduce strings = ['hello', ' ', 'world'] ```
#8b. Print the concatenated string.
# from functools import reduce
# strings = ['hello', ' ', 'world']
# print(reduce(lambda x,y: x+y, strings))

#9a. Use the map function and a lambda function to calculate the length of all strings in a list. ``` ['hello', 'world'] ```
#9b. Convert the map object to a list and print it.
# mylist=['hello', 'world']
# print(list(map(lambda x: len(x),mylist)))


#10a. Use the filter function and a lambda function to remove all strings from a list that do not start with the letter ‘h’. ``` ['hello', 'hi', 'world', 'cat'] ```
# 10b. Convert the filter object to a list and print it.
# mylist=['hello', 'hi', 'world', 'cat']
# print(list(filter(lambda x: x[0]!="h" ,mylist)))


### Task 6: List Comprehension
#1. Create a list of squares for all numbers from 1 to 5. Print the result.
# print([x for x in range(1,6)])

#2. Create a list of all even numbers from 1 to 10. Print the result. Note: this will contain a conditional(if) using and require some research into the modulus % operator.
# print([x for x in range(1,11) if x%2==0])

#3. Create a list of all uppercase characters in a string. ``` string = Hello World ``` Print the result. Note: This will contain a conditional(if) using .isupper() function.
# string = "Hello World"
# print([x for x in list(string) if x.isupper()])


#4. Create a list of lengths of all words in a sentence. Print the result. ``` sentence = Hello world this is a test ``` Note: Can utilise .split()

# sentence = "Hello world this is a test"
# print([len(x) for x in sentence.split(" ")])


#5. Create a list of all numbers from 1 to 10 that are divisible by either 2 or 5. Print the result. Note: can utilise the modulus % operator, and two conditionals 'if' and 'or'.
# print([x for x in range (1,11) if x%2==0 or x%5==0])










