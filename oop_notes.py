'''

Attributes exercises

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

2. Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

Combination exercise

10. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)
မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။


################################################################################################

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။


################################################

attributes(variable/data, method)

class   --->  Laptop
data    --->  serial_no, color
method  --->  on(), off()


################################################

class Laptop:
    def __init__(self, serial_no):
        self.serial_no = serial_no
        self.color = "white"

    def on(self):
        pass

    def off(self):
        pass


Mg Mg' book

laptop.color

################################################

2.  Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  NetworkCard
data    --->  speed
method  --->  download()

################################################

class NetworkCard:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print(f"download with {self.speed}.")

################################################

n1 = NetworkCard("10 Mbps")
n2 = NetworkCard("100 Mbps")
n1.download()
n2.download()

################################################

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  DialUp
data    --->  speed = 9600bit/s
method  --->  download()

################################################

class DialUp:
    def __init__(self):
        self.speed = "9600 bit/s"

    def download(self):
        print(f"download with {self.speed}.")


n1 = DialUp()
n1.download()

################################################

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  ADSL
data    --->  speed = 2000000 bit/s (2 Mbit/s)
method  --->  download()

################################################

class ADSL:
    def __init__(self):
        self.speed = "2000000 bit/s (2 Mbit/s)"

    def download(self):
        print(f"download with {self.speed}.")


n1 = ADSL()
n1.download()

################################################

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  Ethernet
data    --->  speed = 10Mbit/s
method  --->  download()

################################################

class Ethernet2006:
    def __init__(self):
        self.speed = "10Mbit/s"

    def download(self):
        print(f"download with {self.speed}.")


n1 = Ethernet2006()
n1.download()

################################################

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  Ethernet2014
data    --->  speed = 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်)
method  --->  download()

################################################

class Ethernet2014:
    def __init__(self):
        self.speed = "peed = 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်)"

    def download(self):
        print(f"download with {self.speed}.")


n1 = Ethernet2014()
n1.download()

################################################

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

################################################

class   --->  Car
data    --->  VIN, tires, engine
method  --->

################################################

class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine

################################################

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

################################################

class   --->  Tire
data    --->  size, pressure = 0 ( psi )
method  --->  pump(p)

################################################

def pump(p):
    print(f"pump to {p}psi.")

################################################

class Tire:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


t1 = Tire(15)
print(t1.__dict__)

t1.pump(20)
print(t1.__dict__)

################################################

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

################################################

class   --->  Engine
data    --->  fuel_type, state = "off"
method  --->  on(), off()

################################################

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")

################################################

e1 = Engine("Petrol")
e2 = Engine("Diesel")

e1.on()
e2.on()

e1.off()
e2.off()

################################################

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            self.state = "on"
            print(f"{self.fuel_type} Engine On.")
        else:
            print("already on")

    def off(self):
        if self.state == "on":
            self.state = "off"
            print(f"{self.fuel_type} Engine Off.")
        else:
            print("already off")


e1 = Engine("Petrol")
e2 = Engine("Diesel")

e1.on()
e1.on()
e1.on()

################################################

Combination exercise

10. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။

ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။


################################################

class   --->  Car
data    --->  VIN, tires, engine
method  --->

################################################

class Tire:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")


class Brake:
    def __init__(self, t):
        self.type = t

    def brake(self):
        print(f"Brake with {self.type} brake system.")


class Car:
    def __init__(self, VIN, tires, engine, brake):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine
        self.brake = brake


# မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
# ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
city_car = Car("001A", Tire(15), Engine("petrol"), Brake("ABS"))

# ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။
city_car.tires.pump(3)
city_car.engine.on()
city_car.brake.brake()

################################################

car1 = Car(Tire(), Engine(), Brake())
print(car1.__dict__)

car1 = Car(Tire(), Engine(), Brake())
print(car1.__dict__)

car1 = Car(Tire(), Engine(), Brake())
print(car1.__dict__)

print(Car.n)

################################################

class Tire:
    def __init__(self, size=15):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


class Engine:
    def __init__(self, fuel_type="petrol"):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")


class Brake:
    def __init__(self, t="ABS"):
        self.type = t

    def brake(self):
        print(f"Brake with {self.type} brake system.")


class Car:
    n = 0

    def __init__(self, tires, engine, brake):
        Car.n += 1
        self.VIN = f"BMW_{Car.n:0>4}"
        self.tires = tires
        self.engine = engine
        self.brake = brake

    def __repr__(self):
        return f"{self.VIN}"


cars = []
for _ in range(15):
    cars.append(Car(Tire(), Engine(), Brake()))

print(cars[-1].VIN)

print(Car.n)

################################################


class Tire:
    def __init__(self, size=15):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


class Engine:
    def __init__(self, fuel_type="petrol"):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")


class Brake:
    def __init__(self, t="ABS"):
        self.type = t

    def brake(self):
        print(f"Brake with {self.type} brake system.")


class Car:
    n = 0
    wheels = 4
    brand = "BMW"  # Toyota

    def __init__(self, tires, engine, brake):
        self.VIN = Car.cal_serial()
        self.tires = tires
        self.engine = engine
        self.brake = brake

    def __repr__(self):
        return f"{self.VIN}"

    @classmethod
    def cal_serial(cls):
        cls.n += 1
        return f"BMW_{cls.n:0>4}"

    
cars = []
for _ in range(15):
    cars.append(Car(Tire(), Engine(), Brake()))

print(cars[-1].VIN)

print(Car.n)

################################################################################################

obj data.1

class Human:
    def __init__(self, id, name, age):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.id = id
        self.name = name
        self.age = age

#################################################

obj data.2 (common data, data of all obj)

class Human:
    head = 1
    hand = 2
    leg = 2

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

#################################################

program quality (10 millions obj)

if 10 bytes and 1 sec,
- size ( 600 millions bytes, 300  millions bytes + 3 bytes)
- time ( 60 millions sec , 30 millions sec +  3 sec )
- flexibility (10 millions, 1)


##################################################################################################

#################################################

OOP (object-oriented programming)


# class, object, label
# function, methods

A. Object and Label
1. A label is not an object.
2. A label can store an address.
3. Some function & method can produce a new object.  ( produce < create )  ( 1 + 2 )
4. An obj can have multiple labels.
5. A label can change various address.
6. An obj can have multiple data and multiple functions.
7. An object is a combination of data and methods.

################################################

1. A label is not an object.
2. A label can store an address.

# list object 1 , address 1
# label  --->  x, y, z

x = ["apple", "banana"]
y = x
z = y

x.append("orange")
y.append("mangoes")
print(x)
print(y)

################################################

3. Some function & method can create a new object.

# int object 3, float object 1

x = 1  # int object.1
y = 2  # int object.2
z = x + y  # int object.3  ( add magic method create new int obj )

a = x / y  # float object.1  ( truediv magic method create new float obj )

print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))
print(hex(id(a)))

################################################

4. An obj can have multiple labels.

x = int()  # int obj.1  ---> x, b
y = list()  # list obj.1  ---> y, c
z = dict()  # dict obj.1  ---> z, a
a = z  # copy ---> address of dict obj.1
b = x
c = y

print("x =", hex(id(x)))
print("y =", hex(id(y)))
print("z =", hex(id(z)))
print("a =", hex(id(a)))
print("b =", hex(id(b)))
print("c =", hex(id(c)))

################################################

5. A label can change various address.

x = int()  # int obj.1
print(x)
print(hex(id(x)))

x = list()  # list obj.1
print(x)
print(hex(id(x)))

x = dict()  # dict obj.1
print(x)
print(hex(id(x)))

################################################

6. An obj can have multiple data and multiple functions.

1. str             --->   character string + 86 methods
2. int             --->   integer value    + 56 methods
3. 15 data types   --->   about 1000 methods

################################################

7. An object is a combination of attributes and methods.

object
>> attributes + methods

attributes (data)
---> age, name, car_no, wheel, brand, brake_system, mouth

methods (function)
---> walk, speak, brake, bite
---> double_underscore (dunder)(magic), normal, constructor

################################################################################################

B. OOP (object-oriented programming)

1. class
>> blueprint of objects
>> combine data and function

2. obj, instance

################################################

class   ---> Human, Dog, Car, Laptop, Robot
object  ---> mg_mg, dog.1, car_1, laptop_1, robot_1

################################################################################################

C. Creating blueprint

class
name --->  Human
attributes --->  head 1, hand 2, leg 2 (name, age, ID)
methods    --->  say(), write(), walk()

################################################

C. Creating blueprint
C.1. Creating class
C.2. Creating Object
C.3. getting attribute
C.4. using method
C.5. adding or changing new attribute
C.6. checking all attribute
C.7. overriding/creating magic method
C.8. Creating many objects
C.9. Handling many objects



def add(x, y):

C.1. Creating class
class Human:
    def __init__(self, *, name, id):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.name = name
        self.id = id

    def say(self):
        print(f"hello, I am {self.name}.")



class Car:
    def __init__(self, id):
        self.name = "BMW"
        self.id = id

    def __repr__(self):
        return f"BMW-{self.id:0>4}"

    def start(self):
        print(f"{self} is on.")



cars = []
for id in range(1, 1001):
    cars.append(Car(id))


for i in range(1, 1000, 2):
    cars[i].start()

0000
0001

20_000_000
################################################

C.2. Creating Object

mg_mg = Human("Mg Mg")  # human obj 1

################################################

C.3. getting attribute

print(mg_mg.name)

################################################

C.4. using method

mg_mg.say()

################################################

C.5. adding or changing new attribute

mg_mg.age = 20


################################################

C.6. checking all attribute

print(mg_mg.__dict__)

################################################

C.7. overriding/creating magic method

# original method
def __repr__(self):
    return f"<__main__.Human object at {hex(id(self))}>"

# this overrides original method
def __repr__(self):
        return f"Human.{self.name}"

################################################

class Human:
    def __init__(self, n):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.name = n

    def say(self):
        print(f"hello, I am {self.name}.")

    def __repr__(self):
        return f"Human.{self.name}"

################################################

C.8. Creating many objects

humans = []
for i in range(1, 1001):
    humans.append(Human(i))

################################################

C.9. Handling many objects

print(humans)
print(humans[-1])

humans[0].say()
humans[-1].say()

################################################

class Human:
    def __init__(self, n):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.name = n

    def say(self):
        print(f"hello, I am {self.name}.")

    def __repr__(self):
        return f"Human.{self.name}"


humans = []
for i in range(1, 1001):
    humans.append(Human(i))

print(humans)
print(humans[-1])

humans[0].say()
humans[-1].say()

#################################################################################################

to read all magic methods

#################################################################################################

1. class / type / model
   - built-in type ( int, str, list, set, .... )
   - custom-type ( class keyword, type() ) ( creating - )

2. object

3. attributes
   a. variable attribute ( data )
   b. methods attribute ( function )
     - normal method
     - magic method
       - constructor
       - double underscore method, dunder method

#################################################################################################

# custom type
# integer object, int obj, init method, constructor method
# data type, callable type(fun, class), custom type, None type

# custom literal,
# 1 + 2.2 = 3.2
# 1kg + 2.2lb = 2kg
# 2.2lb + 1kg = 4.4lb
# custom type --> Kg, Lb

name = Kg
data = n
function =  add, sub, repr

#################################################

# custom data type

magic method အတွက် exercise ပါ။

#################################################

# step.1 ( draw Kg Type )

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return  self + other

#################################################

# step.2 ( repr )

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return  self + other

    def __repr__(self):
        return f"{self.n} Kg"

#################################################

# step.3 ( +  __add__ )

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return  self + other

    def __repr__(self):
        return f"{self.n} Kg"

#################################################

# step.4 ( Lb )

class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return  self + other

    def __repr__(self):
        return f"{self.n} Lb"

#################################################

# step.5 ( add --> kg , lb )

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __repr__(self):
        return f"{self.n} Lb"

#################################################

# step.6 ( sub --> kg , lb )


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __repr__(self):
        return f"{self.n} Lb"

#################################################

# step.7 ( literal )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


print(1 + 2) # 3
print(1 .Kg + 2.2 .lb) # 2.0 Kg
print(2.2 .lb + 1 .Kg) # 4.4 Lb

#################################################

# check eq (error)
print(1 == 1) # True
print(1 .Kg == 1 .Kg) # False

#################################################

# step.8 ( eq )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        return self.n == other.n

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        return self.n == other.n

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check eq of Kg and Kg( Ok )
print(1 == 1) # True
print(1 .Kg == 1 .Kg) # True

#################################################

# check eq of Kg and Lb( not Ok )
print(1 == 1) # True
print(1 .Kg == 2.2 .lb) # False

#################################################

# step.9 ( eq of Kg and Lb )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        if type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        if type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check eq of Kg and Lb( Ok )
print(1 == 1.0) # True
print(1 .Kg == 2.2 .lb) # True
print(2.2 .lb == 1 .Kg) # True

#################################################

# step.10 (same values should be same object) (cache of kilograms, controlling new obj)

from custom_literals import literal


class Kg:
    _kilograms = {}

    def __new__(cls, n):
        if n in cls._kilograms:
            return cls._kilograms[n]
        kg = super().__new__(cls) # new kg obj from parent
        kg.n = n
        cls._kilograms[n] = kg
        return kg

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        if type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        if type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check id of same value Kg( Ok )
x = 1 # small int
y = 1
print(x is y) # True

a = 1 .Kg
b = 1 .Kg
print(a is b) # True

#################################################

# same value, same obj (same memory address)(same id)
print(hex(id(a)))
print(hex(id(b)))

# 0x10066c830
# 0x10066c830

#################################################

# different values, different objs (True)
a = 1 .Kg
a = 2 .Kg
print(a is b) # False

#################################################

# check immutable ( not Ok )
a = 1 .Kg
b = 1 .Kg
a.n = 2 # mutable
print(a) # 2 Kg
print(b) # 2 Kg

#################################################

# step.11 (immutable value) (control old attr with original setattr) (use parent setattr for new attr)

from custom_literals import literal


class Kg:
    _kilograms = {}

    def __new__(cls, n):
        if n in cls._kilograms:
            return cls._kilograms[n]
        kg = super().__new__(cls) # new kg obj from parent
        kg.n = n
        cls._kilograms[n] = kg
        return kg

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError("Immutable obj")
        super().__setattr__(key, value)

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        if type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        if type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check immutable (Ok)
a = 1 .Kg
b = 1 .Kg
a.n = 2 # AttributeError: Immutable obj
print(a)
print(b)

##################################################################################################

# 1. inheritance  ( tightly coupled ) ( is a relationship ) ( mg mg is a human. )

# super class, base class, parent class
# sub class, derived class, child class
# single, multilevel, multiple, hierarchical, hybrid

'''
#    C     D
#     \   /
#       \/
#        A        # multiple
'''
# 2. composition ( loosely coupled ) ( friendship ) ( has a ) ( mg mg has a head. )
# 3. tightly coupled & loosely coupled
# 4. "is a" relationship & "has a" relationship
# 5. LIFO ( last in first out )

#########################################
'''
#                                    object
#                                  /        \

#                       live obj               unlived obj

#
#                    /            \

#            human                    animals

#         /          \

#     male              female  C


#    /  \                      \
# mg mg  aung aung               ma ma

'''
# super class  of mg mg ---> male, human, live obj, obj
# super class of ma ma  ---> female, human, live obj, obj

# super class of live obj ---> obj
# sub class of live obj ---> human, animals, male, female

#########################################

# 1. create class A
# 2. B and C are sub/child/derived classes of A.
# 3. D and E are sub/child/derived classes of B.
# 4. F AND G are sub/child/derived classes of C.

# 5. Z is sub class of D, E , F, G.
'''

#                          A
#
#                    /           \
#
#                 B                 C
#
#              /     \            /     \
#
#            D         E       F          G
#
#             \        \       /          /
#
#
#                          Z
#
'''
#################################################

11. Read and draw
# 1. create class A
# 2. B and C are sub/child/derived classes of A.
# 3. D and E are sub/child/derived classes of B.
# 4. F AND G are sub/child/derived classes of C.
# 5. Z is sub class of D, E , F, G.
'''
#                          A

#                    /           \

#                B                 C

#            /     \            /     \

#          D         E         F          G

#             \        \       /        /


#                          Z

'''
################################################

12.
I, J, K သည် A ၏ sub class ဖြစ်သည်။
X သည် I ၏ sub class ဖြစ်သည်။
Y သည် J ၏ sub class ဖြစ်သည်။
Z သည် K ၏ sub class ဖြစ်သည်။

ပုံဆွဲပါ။
class တည်ဆောက်ပါ။
'''
#         A
#      / /  \
#   I   J    K
#  /   /      \
# X   Y        Z
'''

class A:
    pass

class I(A):
    pass
class J(A):
    pass
class K(A):
    pass

class X(I):
    pass

class Y(J):
    pass

class Z(K):
    pass

#################################################

13.  အောက်ပါပုံအတိုင်း class တည်ဆောက်ပါ။
'''
# ................  .Fruit

# .......  ...../. .....|......\

#        Apple        Mango       Banana
#      ............/.. .|  ...\
#          မချစ်စု      စိန်တလုံး    တောသရက်
'''
# 1. create class Fruit
# 2. Apple, Mango and Banana are sub/child/derived classes of Fruit.
# 3. မချစ်စု, စိန်တလုံး, တောသရက် are sub/child/derived classes of Mango.

# 1. create class Fruit
class Fruit:
    pass

# 2. Apple, Mango and Banana are sub/child/derived classes of Fruit.
class Apple(Fruit):
    pass

class Mango(Fruit):
    pass

class Banana(Fruit):
    pass


# 3. မချစ်စု, စိန်တလုံး, တောသရက် are sub/child/derived classes of Mango.
class မချစ်စု(Mango):
    pass

class စိန်တလုံး(Mango):
    pass

class တောသရက်(Mango):
    pass

################################################

multiple inheritance exercises

14.
ပန်းသီးနှင့် သစ်တော်သီးသည် သစ်သီးများဖြစ်ကြသည်။
ပန်းသစ်တော်သီးသည် ပန်းသီးနှင့် သစ်တော်သီးနှစ်မျိုးလုံးမှ မျိုးဗီဇများ အမွေဆက်ခံထားသည်။
ထို့ကြောင့် ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။
'''
#     Fruit
#  /        \
# apple     သစ်တော်သီး
#  \        /
#  ပန်းသစ်တော်သီး
'''
class Fruit:
    pass

class Apple(Fruit):
    pass

class သစ်တော်သီး(Fruit):
    pass

class ပန်းသစ်တော်သီး(apple, သစ်တော်သီး):
    pass

################################################

15.
A, B သည် Y ဖြစ်သည်။
C, D, E သည် Z ဖြစ်သည်။
X သည် A, B, C, D, E, F ဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။
'''
#       Y
#     /   \
#    A     B

#
#        Z
#     /  |  \
#    C   D    E

#
# A   B   C   D   E  F
# \  \  \   /  /  /
#   \ \  \ /  /  /
#         X

#
#   Y          Z
# /   \     /  /  \
# A    B   C   D   E   F
#  \   \  \   /  /   /
#   \   \  \ /  /  /
#    \   \ \ / / /
#     \   \ \ ///
#
#           X

'''
class Y:
    pass

class Z:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class F:
    pass

class X(A, B, C, D, E, F):
    pass

################################################

#################################################


inheritance

1. single

    A
    |
    B

class B(A):
    pass


2. multiple
'''
#    A     B
#     \   /
#       C
'''
class C(A, B):
    pass


3. multilevel

    A
    |
    B
    |
    C

class C(B):
    passs


4. hierarchical
'''

#       Y
#     /   \
#    A     B

'''
  
class A(Y):
    pass

  
class B(Y):
    pass
    
    
5. hybrid
'''
#     A
#     |
#     B      C
#      \   /
#        X    multiple + multilevel (hybrid)
'''

class X(B, C):
    pass        
        
'''
#
#   Y          Z               hierarchical
# /   \     /  /  \
# A    B   C   D   E   F       single
#  \   \  \   /  /   /
#   \   \  \ /  /  /
#    \   \ \ / / /
#     \   \\ ///
#
#           X    multiple + multilevel (hybrid)


#  single        ->   A    B   C   D   E
#  multiple      ->   X
#  multilevel    ->   X
#  hierarchical  ->   Y, Z
#  hybrid        ->   X

#     A
#     |
#     B      C
#      \   /
#        X    multiple + multilevel (hybrid)

'''
##################################################################################################


Composition Vs Inheritance


                               Car         ("BMW")(brake)
                          Gas      Diesel
                          
"is a"
Gas engine car is a car.
Diesel engine car is a car.

Inheritance("is a")(tightly couple)
- code reuse
- tight



class Car:
    name = "BMW"

    def brake(self):
        print("Brake")


class GasEngineCar(Car):
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngineCar(Car):
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


my_car = GasEngineCar(4)
my_car.start()
print()

my_car2 = DieselEngineCar(2)
my_car2.start()
print()

#################################################

                                      ... Engine
                                   /
                               Car      
                                     ... Brake
                          
"has a"
Car has an engine.
Car has a brake.

Composition("has a")(loosely couple)
- flexibility
- ! reuse


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


class ABSBrake:
    def brake(self):
        print("safty break with ABS system.")


class Car:
    def __init__(self, engine, brake_system):
        self.engine = engine  # composition / has a / cas has an engine
        self.brake_system = brake_system  # car has a brake

# 4 hp gas engine car
car1 = Car(engine=GasEngine(4), brake_system=ABSBrake())

# 2hp d
car2 = Car(engine=DieselEngine(2), brake_system=ABSBrake())

print(car2.__dict__)
car2.engine = GasEngine(4)
print(car2.__dict__)


#################################################

Composition and Inheritance

class Engine:
    def __init__(self, horse_power):
        self.hp = horse_power


class GasEngine(Engine):
    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine(Engine):
    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


class ABSBrake:
    def brake(self):
        print("safty break with ABS system.")


class Car:
    def __init__(self, engine, brake_system):
        self.engine = engine  # composition / has a / cas has an engine
        self.brake_system = brake_system  # car has a brake

# 4 hp gas engine car
car1 = Car(engine=GasEngine(4), brake_system=ABSBrake())
car1.engine.start()
# 2hp d
car2 = Car(engine=DieselEngine(2), brake_system=ABSBrake())

print(car2.__dict__)
car2.engine = GasEngine(4)
print(car2.__dict__)

##################################################################################################

Knowledge section

##################################################################################################

common attributes

self.head = 1
self.hand = 2
self.leg = 2
self.gender = "male"
self.country = "Myanmar"
self.id = id
self.name = name
self.age = age

                      Human           (h, h, l, c)2 construct()
                     /      |
               Male(m)1     Female(fm)
                 /             |
      obj(id, n, a)          obj(id, n, a)


      x1.country(MRO --> 0, 1, 2 (obj, cls, parent)
      x1.id
      x1.m( --> obj, cls)

class Male:
    def __init__(self, id, name, age):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.gender = "male"
        self.country = "Myanmar"
        self.id = id
        self.name = name
        self.age = age


class Female:
    def __init__(self, id, name, age):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.gender = "female"
        self.country = "Myanmar"
        self.id = id
        self.name = name
        self.age = age

#################################################

class Male(Human):
    head = 1
    hand = 2
    leg = 2
    country = "Myanmar"
    gender = "male"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Female(Human):
    head = 1
    hand = 2
    leg = 2
    country = "Myanmar"
    gender = "female"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

#################################################

class Human:
    head = 1
    hand = 2
    leg = 2
    country = "Myanmar"


class Male(Human):
    gender = "male"
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Female(Human):
    gender = "female"
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

#################################################

class Human:
    head = 1
    hand = 2
    leg = 2
    country = "Myanmar"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Male(Human):
    gender = "male"


class Female(Human):
    gender = "female"

#################################################

x1 = Male("9/WTN(N)123456", "Mg Mg", 30)
x2 = Male("9/WTN(N)123457", "Mg Ba", 29)
x3 = Male("9/WTN(N)123458", "Mg Mya", 28)


y1 = Female("9/WTN(N)123456", "Ma Ma", 30)
y2 = Female("9/WTN(N)123457", "Hla Hla", 29)
y3 = Female("9/WTN(N)123458", "Ma Mya", 28)

print(x1, y1)

##################################################################################################


     X      Y

        Z


inheritance

common attributes ---> inheritance (X, Y)
normal attributes ---> constructor methods

def __init__(self):
    X.__init__(self)
    Y.__init__(self)

def __init__(self):
    self.size = "big"
    self.color = "white"
    self.taste = "sweet"



class X:
    def __init__(self):
        self.size = "big"
        self.color = "white"


class Y:
    def __init__(self):
        self.taste = "sweet"


class Z(X, Y):
    def __init__(self):
        X.__init__(self)
        Y.__init__(self)

a = X()
b = Y()
c = Z()
print(a.__dict__) # apple
print(b.__dict__) # pear
print(c.__dict__) # apple + pear

##################################################################################################

OOP  ---> object ( variable, methods )

Object-Oriented Programming -->  obj  -->  attributes(data, function)
--> unlimited features ( eg. Kg features (data -> n, function -> +, -, repr )

class Weight:
    function 50
    
class Kg(Weight):
   function 70 (40(inheritance) + 30)

Major OOP Concepts
# 1. polymorphism  ( many forms ) 
# 2. inheritance ( code reuse ) 
     - parent ?  ( common )  (
     - features 3 --> Male, Female, Human
     
                  
                        Human
                        /   |
                   Male     Female
                   
    --> Car, Motor Car, Electric Car
    
                    Car
                  /     |
            Motor Car   Electric Car
    
    --> ( new feature - Vehicle )
    
                   Vehicle
                     |
                    Car
                  /     |
            Motor Car   Electric Car
                   
                   
#################################################################################################

Read and write all methods
class methods, static methods, dynamic methods, object methods, common methods, ...

#################################################################################################

class Rectangle:
    def __init__(self, length, width, height):
        self.name = "Rectangle"
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return self.length * self.width

    def volume(self):
        return self.length * self.width * self.height


r1 = Rectangle(10, 5, 6)  # 1 + 4
r2 = Rectangle(10, 5, 6)  # 1 + 4
r3 = Rectangle(10, 5, 6)  # 1 + 4

# 15 ---> 450 bytes

Rectangle.code = "AA"

print(r1.name)
print(r2.name)
print(r3.name)

r1.name = "rectangle"
r2.name = "rectangle"
r3.name = "rectangle"

print(r1.name)
print(r2.name)
print(r3.name)


class Rectangle:
    name = "Rectangle"  # commom data, data of all obj, class data
    def __init__(self, length, width, height):
        self.length = length   # obj data
        self.width = width
        self.height = height

    def area(self):
        return self.length * self.width

    def volume(self):
        return self.length * self.width * self.height

# 1 + 4 + 4 + 4
r1 = Rectangle(10, 5, 6)  # 1 + 4
r2 = Rectangle(10, 5, 6)  # 1 + 4
r3 = Rectangle(10, 5, 6)  # 1 + 4

# 15 ---> 450 bytes

Rectangle.name = "rectangle"

print(r1.name)
print(r2.name)
print(r3.name)


class Rectangle:
    name = "Rectangle"  # 1
    n = 0

    def __init__(self, length, width, height):
        self.length = length  # obj data
        self.width = width
        self.height = height

    def area(self):
        return self.length * self.width

    def volume(self):
        return self.length * self.width * self.height



r1 = Rectangle(10, 5, 6)  # 1 + 3
r2 = Rectangle(10, 5, 6)  # 1 + 3
r3 = Rectangle(10, 5, 6)  # 1 + 3

# 15 ---> 450 bytes
# 12 ---> 360 bytes
# 90 bytes

print(r1.name)
print(r2.name)
print(r3.name)

Rectangle.name = "rectangle"

print(r1.name)
print(r2.name)
print(r3.name)

#print(Rectangle.__dict__)



class   --->  Rectangle
data    --->  length, width, height, name = "Rectangle",

method  --->  area(), volume()

1. object, class, normal  (self, other, cls

def f(x, y):

"""

class Rectangle:
    name = "Rectangle"  # class data
    n = 0               # class data

    def __init__(self, length, width, height):  # obj method
        Rectangle.n += 1
        self.serial = Rectangle.f(Rectangle.n)
        self.length = length  # obj data
        self.width = width    # obj data
        self.height = height  # obj data

    def area(self):  # obj method
        return self.length * self.width

    def volume(self):  # obj method
        return self.length * self.width * self.height

    @classmethod
    def f1(cls):
        print("abc", cls.n)

    @staticmethod
    def f(n):
        return f"Rectangle_{n:0>4}"


r1 = Rectangle(10, 5, 6)  # 1 + 3
r2 = Rectangle(10, 6, 6)  # 1 + 3
r3 = Rectangle(10, 7, 6)  # 1 + 3

#r1.area()
#Rectangle.f1()


'''




# MRO
# diamond problem
# inheritance

















