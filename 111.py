

# 1 vlad 5 2 heelo 5
  
class Human:

    age : int

    def __init__(self, age):
        self.age = age

    def sayHello(self):
        print("hello i am " + str(self.age) + " years old")

    def die(self):
        print("i am died. My age is " + str(self.age))


h1 = Human(10)
h2 = Human(22)
h1.sayHello()
h1.sayHello()
h1.sayHello()
h2.sayHello()
h1.die()