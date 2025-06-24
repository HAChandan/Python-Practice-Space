# Python Classes and Objects

'''
A class is a user-defined blueprint or prototype from which objects are created. 
Classes provide a means of bundling data and functionality together. Creating a 
new class creates a new type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by their class) for modifying their state.

To understand the need for creating a class and object in Python let’s consider an example, 
let’s say you wanted to track the number of dogs that may have different attributes like breed 
and age. If a list is used, the first element could be the dog’s breed while the second element 
could represent its age. Let’s suppose there are 100 different dogs, then how would you know which 
element is supposed to be which? What if you wanted to add other properties to these dogs? 
This lacks organization and it’s the exact need for classes.

Syntax: Class Definition

class ClassName:
    # Statement
Syntax: Object Definition

obj = ClassName()
print(obj.atrr)

The class creates a user-defined data structure, which holds its own data members and member functions, 
which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

Some points on Python class:

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute

'''

# Creating a Python Class

'''
Here, the class keyword indicates that you are creating a class followed by the name of the 
class (Dog in this case).
'''
class Dog:
    sound = "bark"

# Object of Python Class

'''
An Object is an instance of a Class. A class is like a blueprint while an instance is a copy 
of the class with actual values. It’s not an idea anymore, it’s an actual dog, like a dog of 
breed pug who’s seven years old. You can have many dogs to create many different instances, 
but without the class as a guide, you would be lost, not knowing what information is required.

An object consists of:

State/Attributes: It is represented by the attributes of an object. It also reflects the properties of an object.
Example : Breed, Age, Color

Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Example : Bark, Sleep, Eat

Identity: It gives a unique name to an object and enables one object to interact with other objects.
Example : Name of the Dog - Raki, Jimmy


Declaring Claas Objects (Also called instantiating a class)
When an object of a class is created, the class is said to be instantiated. 
All the instances share the attributes and the behavior of the class. But the values of 
those attributes, i.e. the state are unique for each object. A single class may have any number of instances.

'''

# Example of Python Class and object

'''
Creating an object in Python involves instantiating a class to create a new instance of that class. 
This process is also referred to as object instantiation.

'''

# Python3 program to
# demonstrate instantiating
# a class
class Dog:
 
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
 
# Driver code
# Object instantiation
Rodger = Dog()
 
# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()


# Output:

'''
mammal
I'm a mammal
I'm a dog
'''

'''
In the above example, an object is created which is basically a dog named Rodger. 
This class only has two class attributes that tell us that Rodger is a dog and a mammal.

Explanation :

In this example, we are creating a Dog class and we have created two class variables attr1 and attr2. 
We have created a method named fun() which returns the string “I’m a, {attr1}” and I’m a, {attr2}. 
We have created an object of the Dog class and we are printing at the attr1 of the object. Finally, 
we are calling the fun() function.

Self Parameter
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted 
by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about. 
'''


class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
 
    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+".")
 
 
obj = GFG("John", "GeeksForGeeks")
obj.show()

'''
The Self Parameter does not call it to be Self, You can use any other name instead of it. 
Here we change the self to the word someone and the output will be the same.
'''

class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company
 
    def show(somename):
        print("Hello my name is " + somename.name +
              " and I work in "+somename.company+".")
 
 
obj = GFG("John", "GeeksForGeeks")
obj.show()

# Output: Output for both of the codes will be the same.
# Hello my name is John and I work in GeeksForGeeks.

'''
Explanation:

In this example, we are creating a GFG class and we have created the name, 
and company instance variables in the constructor. We have created a method named say_hi() 
which returns the string “Hello my name is ” + {name} +” and I work in “+{company}+”.”.We have 
created a person class object and we passing the name John and Company GeeksForGeeks to the instance 
variable. Finally, we are calling the show() of the class.

'''

# Pass Statement

'''
The program’s execution is unaffected by the pass statement’s inaction. It merely 
permits the program to skip past that section of the code without doing anything. 
It is frequently employed when the syntactic constraints of Python demand a valid 
statement but no useful code must be executed.
'''

class MyClass:
    pass


# __init__() method

'''
__init__() method
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing 
the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) 
that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do with your object.
'''
# Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()


# Output: 

# Hello, my name is Nikhil

'''
Explanation:

In this example, we are creating a Person class and we have created a name instance 
variable in the constructor. We have created a method named as say_hi() which returns 
the string “Hello, my name is {name}”.We have created a person class object and we pass 
the name Nikhil to the instance variable. Finally, we are calling the say_hi() of the class.
'''

# __str__() method

'''
Python has a particular method called __str__(). that is used to define how a class 
object should be represented as a string. It is often used to give an object a 
human-readable textual representation, which is helpful for logging, debugging, or 
showing users object information. When a class object is used to create a string using 
the built-in functions print() and str(), the __str__() function is automatically used. 
You can alter how objects of a class are represented in strings by defining the __str__() method.

'''


class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
 
    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."
 
 
my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)

# Output:

# My name is John and I work in GeeksForGeeks.

'''
Explanation:

In this example, We are creating a class named GFG.In the class, we are creating two instance 
variables name and company. In the __str__() method we are returning the name instance variable 
and company instance variable. Finally, we are creating the object of GFG class and we are 
calling the __str__() method.

'''

# Class and Instance Variables

'''
Instance variables are for data, unique to each instance and class variables are for 
attributes and methods shared by all instances of the class. Instance variables are 
variables whose value is assigned inside a constructor or method with self whereas 
class variables are variables whose value is assigned in the class.

'''
# Defining instance variables using a constructor. 

# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)



# Output:

'''
Rodger details:
Rodger is a dog
Breed:  Pug
Color:  brown
Buzo details:
Buzo is a dog
Breed:  Bulldog
Color:  black
Accessing class variable using class name
dog
'''

'''
Explanation:

A class named Dog is defined with a class variable animal set to the string “dog”. 
Class variables are shared by all objects of a class and can be accessed using the class name. 
Dog class has two instance variables breed and color. Later we are creating two objects of the 
Dog class and we are printing the value of both objects with a class variable named animal.

'''

# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed):

		# Instance Variable
		self.breed = breed

	# Adds an instance variable
	def setColor(self, color):
		self.color = color

	# Retrieves instance variable
	def getColor(self):
		return self.color



# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())

# Output:

# brown


'''
Explanation:

In this example, We have defined a class named Dog and we have created 
a class variable animal. We have created an instance variable breed in the 
constructor. The class Dog consists of two methods setColor and getColor, 
they are used for creating and initializing an instance variable and retrieving 
the value of the instance variable. We have made an object of the Dog class and 
we have set the instance variable value to brown and we are printing the value in the terminal.
'''

# Constructors in Python

'''
Prerequisites: Object-Oriented Programming in Python, Object-Oriented Programming in Python | Set 2 
Constructors are generally used for instantiating an object. The task of constructors is to 
initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor and is always called when an object is created.
Syntax of constructor declaration : 

def __init__(self):
    # body of the constructor
Types of constructors : 

default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. 
Its definition has only one argument which is a reference to the instance being constructed.
parameterized constructor: constructor with parameters is known as parameterized constructor. 
The parameterized constructor takes its first argument as a reference to the instance being 
constructed known as self and the rest of the arguments are provided by the programmer.

'''

# Example of default constructor :


class GeekforGeeks:
 
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"
 
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
 
 
# creating object of the class
obj = GeekforGeeks()
 
# calling the instance method using the object obj
obj.print_Geek()


# Output:
# GeekforGeeks

# Example of the parameterized constructor :

class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()


# Output

'''
First number = 1000
Second number = 2000
Addition of two numbers = 3000
First number = 10
Second number = 20
Addition of two numbers = 30
'''


# Example:

class MyClass:
	def __init__(self, name=None):
		if name is None:
			print("Default constructor called")
		else:
			self.name = name
			print("Parameterized constructor called with name", self.name)
	
	def method(self):
		if hasattr(self, 'name'):
			print("Method called with name", self.name)
		else:
			print("Method called without a name")

# Create an object of the class using the default constructor
obj1 = MyClass()

# Call a method of the class
obj1.method()

# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")

# Call a method of the class
obj2.method()


# Output

'''
Default constructor called
Method called without a name
Parameterized constructor called with name John
Method called with name John
'''

# Explanation:

'''
Explanation:
In this example, we define a class MyClass with both a default constructor and a parameterized constructor. 
The default constructor checks whether a parameter has been passed in or not, and prints a message to the 
console accordingly. The parameterized constructor takes in a single parameter name and sets the name 
attribute of the object to the value of that parameter.

We also define a method method() that checks whether the object has a name attribute or not, and prints 
a message to the console accordingly.

We create two objects of the class MyClass using both types of constructors. First, we create an 
object using the default constructor, which prints the message “Default constructor called” to the console. 
We then call the method() method on this object, which prints the message “Method called without a name” 
to the console.

Next, we create an object using the parameterized constructor, passing in the name “John”. The constructor 
is called automatically, and the message “Parameterized constructor called with name John” is printed to the 
console. We then call the method() method on this object, which prints the message “Method called with name John” 
to the console.

Overall, this example shows how both types of constructors can be implemented in a single class in Python.'''


# Advantages of using constructors in Python:

'''

Initialization of objects: Constructors are used to initialize the objects of a class. 
They allow you to set default values for attributes or properties, and also allow you to initialize 
the object with custom data.
Easy to implement: Constructors are easy to implement in Python, and can be defined using the __init__() method.

Better readability: Constructors improve the readability of the code by making it clear what values are being 
initialized and how they are being initialized.
Encapsulation: Constructors can be used to enforce encapsulation, by ensuring that the object’s attributes 
are initialized correctly and in a controlled manner.
Disadvantages of using constructors in Python:

Overloading not supported: Unlike other object-oriented languages, Python does not support method overloading. 
This means that you cannot have multiple constructors with different parameters in a single class.
Limited functionality: Constructors in Python are limited in their functionality compared to constructors 
in other programming languages. For example, Python does not have constructors with access modifiers like 
public, private or protected.
Constructors may be unnecessary: In some cases, constructors may not be necessary, as the default values of 
attributes may be sufficient. In these cases, using a constructor may add unnecessary complexity to the code.
Overall, constructors in Python can be useful for initializing objects and enforcing encapsulation. However, 
they may not always be necessary and are limited in their functionality compared to constructors in other 
programming languages.
'''

# Destructors in Python

'''
Constructors in Python
Destructors are called when an object gets destroyed. In Python, destructors are not needed as 
much as in C++ because Python has a garbage collector that handles memory management automatically. 
The __del__() method is a known as a destructor method in Python. It is called when all references 
to the object have been deleted i.e when an object is garbage collected. 
Syntax of destructor declaration : 
 

def __del__(self):
  # body of destructor
Note : A reference to objects is also deleted when the object goes out of reference or when the program ends. 
Example 1 : Here is the simple example of destructor. By using del keyword we deleted the all references of 
object ‘obj’, therefore destructor invoked automatically.
'''

# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj

# Output
# Employee created.
# Destructor called, Employee deleted.

'''
Note : The destructor was called after the program ended or when all the references to object are deleted 
i.e when the reference count becomes zero, not when object went out of scope.
Example 2: This example gives the explanation of above-mentioned note. Here, notice that the destructor 
is called after the ‘Program End…’ printed.
'''

# Python program to illustrate destructor

class Employee:

	# Initializing
	def __init__(self):
		print('Employee created')

	# Calling destructor
	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

# Output

'''

Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called'''

# Example 3: Now, consider the following example :

# Python program to illustrate destructor
  
class A:
    def __init__(self, bb):
        self.b = bb
  
class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("Do or die")
  
def fun():
    b = B()
  
fun()

# Output
# Do or die

'''
In this example when the function fun() is called, it creates an instance of class B which passes itself 
to class A, which then sets a reference to class B and resulting in a circular reference.
Generally, Python’s garbage collector which is used to detect these types of cyclic references would 
remove it but in this example the use of custom destructor marks this item as “uncollectable”. 
Simply, it doesn’t know the order in which to destroy the objects, so it leaves them. Therefore, 
if your instances are involved in circular references they will live in memory for as long as the application run.

NOTE : The problem mentioned in example 3 is resolved in newer versions of python, but it still exists in 
version < 3.4 .

'''

# Example: Destruction in recursion

'''
In Python, you can define a destructor for a class using the __del__() method. 
This method is called automatically when the object is about to be destroyed by 
the garbage collector. Here’s an example of how to use a destructor in a recursive function:
'''

class RecursiveFunction:
	def __init__(self, n):
		self.n = n
		print("Recursive function initialized with n =", n)

	def run(self, n=None):
		if n is None:
			n = self.n
		if n <= 0:
			return
		print("Running recursive function with n =", n)
		self.run(n-1)

	def __del__(self):
		print("Recursive function object destroyed")

# Create an object of the class
obj = RecursiveFunction(5)

# Call the recursive function
obj.run()

# Destroy the object
del obj

# Output

'''

('Recursive function initialized with n =', 5)
('Running recursive function with n =', 5)
('Running recursive function with n =', 4)
('Running recursive function with n =', 3)
('Running recursive function with n =', 2)
('Running recursive function with n =', 1)
Recursive function object destroyed'''


'''
In this example, we define a class RecursiveFunction with an __init__() method that takes in a parameter n. 
This parameter is stored as an attribute of the object.

We also define a run() method that takes in an optional parameter n. If n is not provided, it defaults 
to the value of self.n. The run() method runs a recursive function that prints a message to the console 
and calls itself with n-1.


We define a destructor using the __del__() method, which simply prints a message to the console indicating 
that the object has been destroyed.

We create an object of the class RecursiveFunction with n set to 5, and call the run() method. This runs 
the recursive function, printing a message to the console for each call.

Finally, we destroy the object using the del statement. This triggers the destructor, which prints a message 
to the console indicating that the object has been destroyed.

Note that in this example, the recursive function will continue running until n reaches 0. When n is 0, the 
function will return and the object will be destroyed by the garbage collector. The destructor will then 
be called automatically.

'''

# Advantages of using destructors in Python:

'''
Automatic cleanup: Destructors provide automatic cleanup of resources used by an object when 
it is no longer needed. This can be especially useful in cases where resources are limited, 
or where failure to clean up can lead to memory leaks or other issues.
Consistent behavior: Destructors ensure that an object is properly cleaned up, regardless of 
how it is used or when it is destroyed. This helps to ensure consistent behavior and can help to 
prevent bugs and other issues.
Easy to use: Destructors are easy to implement in Python, and can be defined using the __del__() method.
Supports object-oriented programming: Destructors are an important feature of object-oriented programming, 
and can be used to enforce encapsulation and other principles of object-oriented design.
Helps with debugging: Destructors can be useful for debugging, as they can be used to trace the lifecycle 
of an object and determine when it is being destroyed.
Overall, destructors are an important feature of Python and can help to ensure that objects are properly 
cleaned up and resources are not wasted. They are easy to use and can be useful for enforcing encapsulation 
and other principles of object-oriented design.

'''

