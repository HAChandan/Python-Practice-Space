

mat1_name = "iphone_12"
mat1_price = 50000
mat1_qty = 2
gst = 0.28
mat1_total_cost = mat1_price * mat1_qty * (1+gst)

mat2_name = "Mackbook"
mat2_price = 90000
mat2_qty = 3
mat2_total_cost = mat2_price * mat2_qty * (1+gst)

def total_cost(price, qty):
    gst = 1.28
    return price*qty*gst

print(total_cost(mat1_price, mat1_qty))
print(total_cost(mat2_price, mat2_qty))


class material:
    def total_cost(price, qty):
        gst = 1.28
        return price * qty * gst

mat1 = material
mat1.name = "iphone_12"
mat1.price = 50000
mat1.qty = 2
print(mat1.total_cost(mat1.price, mat1.qty))



class material:
    gst = 1.28
    def __init__(self, name, price, qty):
        assert price >= 0, "Price takes on a positive number"
        assert qty >= 0, "QTY takes on a positive number"
        self.name_x = name
        self.price_x = price
        self.qty_x = qty
        print(f"I just got created by name {name}")
        print(f"I just got created by price {price}")
        print(f"I just got created by qty {qty}")
    def total_cost(self):
        return self.price_x * self.qty_x * material.gst

print(material.gst)
# OBJECT IS AN INSTANCE OF CLASS
# mat1 is an object of class material

mat1 = material("iphone_12", 45000, 2)
print()
mat2 = material("redmi", 15000, 3)
print(mat1.name_x, mat1.price_x, mat1.qty_x, mat1.total_cost())
print(mat2.name_x, mat2.price_x, mat2.qty_x, mat2.total_cost())

print(mat1)
print(mat2)
print(type(material))
print(type(mat1))
print(type(mat2))

l1 = [10, 22, 34, 45]
print(type(l1))

t1 = (42, 65, 78, 77)
print(type(t1))

def addition(a, b):
  c = a + b
  return (c)
print(type(addition))

mat3 = material("oppo", -25000, 5)
print(mat3.name_x, mat3.price_x, mat3.qty_x, mat3.total_cost())



class material:
    gst = 1.28
    def __init__(self, name:str, price:float, qty=0):
        self.name_x = name
        self.price_x = price
        self.qty_x = qty
        print(f"I just got created by name {name}")
        print(f"I just got created by price {price}")
        print(f"I just got created by qty {qty}")
    def total_cost(self):
        return self.price_x * self.qty_x * material.gst

mat3 = material("Mackbook_Air", 80000, 5)
mat4 = material("ipad", 40000, 6)
mat5 = material("Airpod", 18000, 2)



class material:
    all = []
    gst = 1.28
    def __init__(self, name:str, price:float, qty=0):
        self.name_x = name
        self.price_x = price
        self.qty_x = qty
        print(f"I just got created by name {name}")
        print(f"I just got created by price {price}")
        print(f"I just got created by qty {qty}")
        material.all.append(self)
    def total_cost(self):
        return self.price_x * self.qty_x * material.gst

mat3 = material("Mackbook_Air", 80000, 5)
mat4 = material("ipad", 40000, 6)
mat5 = material("Airpod", 18000, 2)
print(material.all)
print()
for i in material.all:
    print(i.name_x,"  ",i.price_x,"  ",i.qty_x,"  ",i.total_cost())


l1 = [10, 22, 34, 45]

t1 = (42, 65, 78, 77)

def addition(a, b):
  c = a + b
  return (c)

print(type(l1))
print(type(t1))
print(type(addition))
print(type(material))
# print(mat3)
# print(type(mat3))



# Inheritance
# Defining the parent class

# Parent class
class Product:
    def __init__(self,code, category, size, wifi, battery, price):
        self.product_code = code
        self.product_category = category
        self.dimension = size
        self.network = wifi
        self.battery = battery
        self.base_price = price
    def config(self):
        print("Product Configuration: \n", self.product_code, self.dimension,
              self.network, self.battery)
    def total_cost(self, qty):
        print("Total price from parent class : \n", self.base_price*qty)

# Child class
class Iphone(Product):
    def __init__(self, code, category, size, wifi, battery, price, margin, color):
        Product.__init__(self, code, category, size, wifi, battery, price)
        self.margin = margin
        self.color = color
    def sales_price(self):
        self.sales_price = self.base_price*(1+self.margin)
        return self.sales_price
    def total_cost(self, qty):
        print("Total price from child class - Iphone : \n", self.base_price*(1+self.margin)*qty)

iphone12_mini = Iphone("MH1202", "Phone", "5X2.5", "5g", "5000mAh", 40000, 0.90, "BLue")
iphone12_mini.config()
print(iphone12_mini.sales_price())
iphone12_mini.total_cost(5)

print()
# Child class
class Airpod(Product):
    gst = 1.18
    def __init__(self, code, category, size, wifi, battery, price, margin, color):
        Product.__init__(self, code, category, size, wifi, battery, price)
        self.margin = margin
        self.color = color
    def sales_price(self):
        self.sales_price = self.base_price*(1+self.margin)
        return self.sales_price
    def total_cost(self, qty):
        print("Total price from child class - Airpod : \n", self.base_price*(1+self.margin)*qty*Airpod.gst)

Airpod_pro = Airpod("MH1205", "earPhone", "2X0.5", "NA", "1000mAh", 10000, 0.5, "Black")
Airpod_pro.config()
print(Airpod_pro.sales_price())
Airpod_pro.total_cost(10)



# Few More Examples on inheritance and polymorphism

# Parent
class auto:
    def __init__(self, type, fuel, payload):
        self.type = type
        self.fuel = fuel
        self.payload = payload
    def config(self):
        print("Vehical Configuration is : \n", self.type, self.fuel, self.payload)


# Child1
class lalamovers(auto):
    def __init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km):
        auto.__init__(self, type, fuel, payload)
        self.mileage = mileage
        self.GClearanec = ground_clearance
        self.Charges = charges_per_km
    def rate_calculator(self, kms):
        print("rate calculated for lalamovars_child1")
        if kms <= 3:
            return 3*self.Charges+10
        else:
            return kms*self.Charges

# Child2
class Hulalamovers(auto):
    def __init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km, charges_per_hour):
        auto.__init__(self, type, fuel, payload)
        self.mileage = mileage
        self.GClearanec = ground_clearance
        self.Charges = charges_per_km
        self.hourly_charges = charges_per_hour

    def rate_calculator(self, kms):
        print("rate calculated for lalamovars_child2")
        if kms <= 3:
            return 3*self.Charges
        else:
            return kms * self.Charges

    def hourly_rate_calculator(self, hrs):
        if hrs <= 2:
            return 2 * self.hourly_charges
        else:
            return hrs * self.hourly_charges

# GrandChild
class lalamover_sons(lalamovers):
    def __init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km, range):
        lalamovers.__init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km)
        self.range = range

    def rate_calculator(self, kms):
        print("rate calculated for lalamover_sons_GrandChild")
        if kms <= 3:
            return 3 * self.Charges
        else:
            return kms * self.Charges

    def helper_charges(self, helper, hrs):
        return helper*hrs*50


# Great Grand Child
class lala_grandsons(lalamover_sons, Hulalamovers):
    def __init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km, range, charges_per_hour, intercity):
        lalamover_sons.__init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km, range)
        Hulalamovers.__init__(self, type, fuel, payload, mileage, ground_clearance, charges_per_km, charges_per_hour)
        self.intercity = intercity
    def rates_intercity(self):
        if self.intercity <= 100:
            return 900
        else:
            return 400 * self.intercity*12

LM_VHC_01 = lalamovers("2-Strokes", "Petrol", 400, 23, "18Incs", 12)
LMS_VHC_01 = lalamover_sons("4-Strokes", "LPG", 400, 22, "18Incs", 15, 200)
HLM_VHC_01 = Hulalamovers("4-Strokes", "CNG", 350, 20, "18Incs", 18, 120)
LGS_VHC_01 = lala_grandsons("EV", "electric-chargeable", 240, 300, "18Incs", 18, 240, 12, 250)

# method config inherited from parent class auto in child object of class lalamovers

LM_VHC_01.config()

# Polymorphism for method rate_calculator between child and grand child
print(LM_VHC_01.rate_calculator(10))
print(LMS_VHC_01.rate_calculator(10))

# Example for multi inheritance child class inheriting from 2 parent class

print(LGS_VHC_01.rate_calculator(20))
print(LGS_VHC_01.hourly_rate_calculator(4))
print(LGS_VHC_01.helper_charges(2, 4))
print(Hulalamovers.rate_calculator(LGS_VHC_01, 20))

LGS_VHC_01.config()

# global and private variable "_" private "__" strongly private
# print(LGS_VHC_01.payload)



# Public Variable

class student():
    school = "Prime Intuit"
    def __init__(self, name, age):
        self.name = name
        self.age = age

std = student("Abhi", 25)
print(std.school)
print(std.age)
std.age = 20
print(std.age)




# Protected Variable

class student():
    _school = "Prime Intuit"
    def __init__(self, name, age):
        self._name = name
        self._age = age

std = student("Abhi", 25)
print(std._school)
print(std._name)
print(std._age)
std._age = 20
print(std._age)



# Private Variable

# Not excess method
class student():
    __school = "Prime Intuit"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

std = student("Abhi", 25)
print(std.__school)
print(std.__age)
std._age = 20
print(std.__age)




# Excess Method
class student():
    __school = "Prime Intuit"
    def __init__(self, name, age):
        self._name = name
        self._age = age

std = student("Abhi", 25)
print(std._student__school)

std._student__school = "Capital School"
print(std._student__school)

print(std._age._student__school)
# std.age = 20
# print(std._age)



# Example-1
class bike:
    def __init__(self):
        print("Object bike  is created")
        self.wheels = 2
        self.engine = "250"
        self.front_suspension = "Telescope"
        self.body_colour = "black"
    def specification(self, color, mirror, crash_guard):
        color_1 = color
        num_mirror = mirror
        color_crash_guard = crash_guard
        print("\nbike specification:\n")
        print("color of the bike is = ", color_1)
        print("mirror of the bike is = ", num_mirror)
        print("crash guard type of the bike is = ", color_crash_guard)
        print("Engine Capacity = ", self.engine)
        print("Outer bike color = ", self.body_colour)

rolex90 = bike()
print(rolex90.wheels)
print(rolex90.engine)
print(rolex90.front_suspension)
print(rolex90.body_colour)
rolex90.specification("red", "convex", "u frame")



# Example-1a
class bike:
    def __init__(self):
        print("Class bike  is created")
        self.wheels = 2
        self.engine = "250"
        self.front_suspension = "Telescope"
        self.body_colour = "black"
    def specification(self, color, mirror, crash_guard):
        self.color_1 = color
        self.num_mirror = mirror
        self.color_crash_guard = crash_guard
        print("\nbike specification:\n")
        print("color of the bike is = ", self.color_1)
        print("mirror of the bike is = ", self.num_mirror)
        print("crash guard type of the bike is = ", self.color_crash_guard)
        print("Engine Capacity = ", self.engine)
        print("Outer bike color = ", self.body_colour)

rolex90 = bike()
rolex90.specification("red", "convex", "u frame")

pulsar = bike()
pulsar.specification("black", "convex2", "c frame")

# Example-2

class hotel_45:
    def __init__(self):
        self.basic_menu = ["rice", "samber", "palya_1", "palya_2","rasam", "curd"]

    def variation(self,*items):
        print(type(items))
        meals = self.basic_menu.copy()
        for i in items:
            meals.append(i)
        print("Your menu includes", meals)
        print("class address : ", id(hotel_45))
        print("Self address : ", id(self))

spl_meals = hotel_45()
spl_meals.variation("chapathi", "sweet", "buttermilk", "dosa")
print("object address : ",id(spl_meals))


nonveg_meals = hotel_45()
nonveg_meals.variation("kabab", "Chicken curry")
print("object address : ", id(nonveg_meals))


# Example-3

class Emp():
    def __init__(self, emp_id, name, dept, dob):
        self.employee_ID = emp_id
        self.employee_name = name
        self.employee_dept = dept
        self.employee_dob = dob
        self.basic = 0
        print("Employee created with ID : ", self.employee_ID, self.employee_name, self.employee_dept, self.employee_dob)
    def salary(self, basic):
        self.basic = basic
        self.hra = basic * 0.25
        self.PF = basic * 0.09
        if basic > 10000:
            self.medical = 1000
        else:
            self.medical = 750
        self.gross_salary = self.basic + self.hra - self.PF - self.medical
        return self.gross_salary

niranjan = Emp( 1094, "Niranjan.K", "IT", "1017")
abc = niranjan.salary(30000)
print(niranjan.employee_ID)
print(niranjan.employee_name)
print(niranjan.employee_dept)
print(niranjan.employee_dob)
print(abc)


print()
class Myclass:
     x = 5

print(Myclass)
print()

print()
class River:
    x = "124 Ft"

Dam = River()
print(Dam.x)

class Person:
    def __init__(self, name, age):
        self.pname = name
        self.page = age

Person1 = Person("Warner", 28)
Person2 = Person("Smith", 25)
Person3 = Person("Starc", 24)
Person4 = Person("Finch", 26)

print()
print("Person1 Name is", Person1.pname)
print("Person1 Age is", Person1.page)

print()
print("Person2 Name is", Person2.pname)
print("Person2 Age is", Person2.page)

print()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def box1(self):
        print("Hello my name is " + self.name + " And my age is " + self.age)

    def box2(self):
        print("Hello my name is " + self.name + " And my age is " + self.age)

Person1 = Person("Warner", "28")
Person2 = Person("Smith", "26")
Person1.box1()
Person2.box2()


print()
print("Person3 Name is", Person3.name)
print("Person3 Age is", Person3.age)

print()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def box1(self):
        print(self.firstname, self.lastname)


Person1 = Person("MS", "Dhoni")
Person1.box1()
print()


print()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def box1(self):
        print(self.firstname, self.lastname)

class Cricketer(Person):
    pass

Person1 = Cricketer("MS", "Dhoni")
Person1.box1()
print()



print()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def box1(self):
        print(self.firstname, self.lastname)

class Cricketer(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


Person1 = Cricketer("MS", "Dhoni")
Person1.box1()
print()



print()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def box1(self):
        print(self.firstname, self.lastname)

class Cricketer(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


Person1 = Cricketer("MS", "Dhoni")
Person1.box1()
print()


