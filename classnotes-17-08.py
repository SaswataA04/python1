#inheritance
class superclass:
    def display(self):
        print("super")

class sub(super):
    def show(self):
        print("sub")
obj1 = sub() #obj of sub class
obj1.display() #calling method of super class
obj1.show() #calling method of sub class 
 

#casestudy
#create a class transport  with a method getval() to initialise the varibale type of transport . define a method showval() to display the type of variable . create a subclass bus with th method input_val to initialise the variable seat_number , & source , destination .and
#define a method display() to show all the variables of bus 

class Transport:
    def getval(self):
        """Initialize transport type via user input"""
        self.type_of_transport = input("Enter type of transport: ")
    
    def showval(self):
        """Display transport type"""
        print(f"Type of Transport: {self.type_of_transport}")


class Bus(Transport):
    def input_val(self):
        """Initialize bus variables via user input"""
        super().getval()  
        self.seat_number = int(input("Enter seat number: "))
        self.source = input("Enter source: ")
        self.destination = input("Enter destination: ")
    
    def display(self):
        """Display all bus information"""
        print(" Bus Details")
        self.showval()  
        print(f"Seat Number: {self.seat_number}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        #print("-" * 20)


bus = Bus()
bus.input_val()
bus.display()



#inheritance with constructor
class Student:
    def __init__(self, roll , name):
        self.roll = roll
        self.name = name

class ug_student(Student):
    def __init__(self, roll, name, proj):
        super().__init__(roll, name)
        self.proj = proj

    def show(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Project: {self.proj}")  

    obj1 = ug_student(101, "John", "AI Project")
    obj1.show()  

    #first we call the parent class constructor using super() to initialize roll and name, then we initialize proj in the child class constructor. The show method displays all the attributes of the ug_student object.          







#initialise the variable of class transport and bus with constructor 


class Transport:

    def __init__(self, transport_type):
        self.transport_type = transport_type

    def showval(self):
        print("Type of Transport:", self.transport_type)


class Bus(Transport):

    def __init__(self, transport_type, seat_number, source, destination):
        
        super().__init__(transport_type)

        self.seat_number = seat_number
        self.source = source
        self.destination = destination

    def display(self):
        self.showval()
        print("Seat Number:", self.seat_number)
        print("Source:", self.source)
        print("Destination:", self.destination)


b1 = Bus("Bus", 50, "Kolkata", "Durgapur")

b1.display()





#polymorphism

#static = method overloading
#  n dynamic polymorphism = method overriding

class book:
    def __init__(self, title):
        self.title = title
    def show(self):
        print("Book title:", self.title)

class edition(book):
    def __init__(self, title, edition):
        super().__init__(title)
        self.edition = edition
    def show(self):
        super().show()  # Call the show method of the parent class insttead of child class to display the title
        print("Edition:", self.edition)

obj1 = edition("Python Programming", "2nd Edition")
obj1.show()  # This will call the show method of the edition class, demonstrating method overriding.

obj2 = book("Data Structures")
obj2.show()  # This will call the show method of the book class, demonstrating method overloading.









##create a class transport with variabes type . create 2 child classes boat nd bus with variable capacity , src , destn & bus has seat_no , src , destn . 
# initialise all the variables of all the classes with constructor . define show() method in transport class to show type of transport . 
# define show() in boat class to display the records of boat and define another show method in bus class to display the attributes of bus .
# create 2 objects if boat class and 2 objects of bus class  


class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Boat(Transport):
    def __init__(self, type, capacity, src, destn):
        super().__init__(type)
        self.capacity = capacity
        self.src = src
        self.destn = destn

    def show(self):
        print("Boat Details")
        print("Type:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.src)
        print("Destination:", self.destn)
        print()


class Bus(Transport):
    def __init__(self, type, capacity, seat_no, src, destn):
        super().__init__(type)
        self.capacity = capacity
        self.seat_no = seat_no
        self.src = src
        self.destn = destn

    def show(self):
        print("Bus Details")
        print("Type:", self.type)
        print("Capacity:", self.capacity)
        print("Seat Number:", self.seat_no)
        print("Source:", self.src)
        print("Destination:", self.destn)
        print()


boat1 = Boat("Water Transport", 50, "Kolkata", "Haldia")
boat2 = Boat("Water Transport", 80, "Kolkata", "Sundarbans")

bus1 = Bus("Road Transport", 40, 15, "Kolkata", "Durgapur")
bus2 = Bus("Road Transport", 50, 25, "Kolkata", "Siliguri")

boat1.show()
boat2.show()
bus1.show()
bus2.show()
