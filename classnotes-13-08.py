#def - func initialisation

#class syntax
# class class_name:



class MyClass:
    def show(self, x): #self signifies invoking of an object #x is the parameter
        print(x)


p1.show() #p1 is obj of MyClass class
p2 = MyClass() #p2 is obj of MyClass class
p2.show("Hello") 

#constructor initialises the  obj of a class







#implementation of constructor

class MyClass1:
    def __init__(self): #constructor init is used
        self.x = 0
    def show(self):
        print(self.x)

ob1 = MyClass1() #obj of MyClass1 class
ob1.show() #invoking show method of MyClass1 class


#default constructor can't initialise obj

#to initialise obj custom constructor needs to be made


