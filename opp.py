# # car1Name = "Swift"
# # car1variantName = "VXI"
# # car1Mirrors = 2
# # car1Wheels = 4
# # car1Color = "Red"

# # def acc():
# #     print("Car1 is Moving")

# # def brake():
# #     print("Car1 is Stopped")


# # car2Name = "Swift"
# # car2variantName = "VXI"
# # car2Mirrors = 2
# # car2Wheels = 4
# # car2Color = "Red"

# # def acc():
# #     print("Car2 is Moving")

# # def brake():
# #     print("Car2 is Stopped")


# # class
# # Object
# # class Car:
# #     carName = "Swift"
# #     carvariantName = "VXI"
# #     carMirrors = 2
# #     carWheels = 4
# #     carColor = "Red"
# #     # methods
# #     def acc(self):
# #         print(f"{self.carName},{self.carvariantName} is Moving")
# #     def brake(self):
# #         print(f"{self.carName},{self.carvariantName} is Stopped")
# # # Object or Insteance Creation
# # car1 = Car()
# # print(car1.carvariantName)
# # car1.carvariantName = "VDI"
# # print(car1.carvariantName)
# # car2 = Car()
# # car2.carvariantName = "ZDI"
# # print(car2.carvariantName)
# # car1.acc()
# # car2.brake()

# # access specifier
# # private (__) - accessible only within the class
# # protected (_) - accessible within the class and its subclasses
# # public (-) - accessible from anywhere


# # class Marks:
# #     __totalMark = 0
# #     def totalMarks(self,t,e,m,s,ss):
# #         self.__totalMark = t + e + m + s + ss
# #         return self.__totalMark
# #     def percentage(self):
# #         return (self.__totalMark/500)*100

# # s1 = Marks()
# # print(s1.totalMarks(90, 80, 70, 60, 50))  
# # print(s1.percentage())
# # print(s1.__totalMark)  # This will raise an AttributeError because __totalMark is private
# # encapsulation
# class BankAccount:
#     __balance = 5000
#     def deposit(self, amount):
#         self.__balance += amount 
#         # 5000+500 = 5500
#         print(f"Amount deposited: {amount}")
#     def qwithdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient funds")
#         else:
#             self.__balance -= amount
#             print(f"Withdrew {amount}")
#     def addInterest(self, rate):
#         interest = self.__balance * (rate / 100)
#         self.__balance += interest
#         print(f"Added interest: {interest}. New balance: {self.__balance}")
#     def getBalance(self):
#         return self.__balance
# acc1 = BankAccount()
# acc1.deposit(500)
# # acc1.qwithdraw(2000)
# # acc1.addInterest(5) 
# # print(f"Current balance: {acc1.getBalance()}") 
# # acc2 = BankAccount()
# # acc2.deposit(1000)
# # acc2.qwithdraw(3000)   
# # acc2.addInterest(3) 
# # print(f"Current balance: {acc2.getBalance()}")
# # # inheritence
# # single inheritance

# class Father:
#     property = "House"
# class Son(Father):
#     def prints(self):
#         print(Father.property)
#         print(GrandFather.property)
# s = Son()
# s.prints()
# # mutilevel inheritance
# class GrandFather:
#     property = "Land"
# class Father(GrandFather):
#     property = "House"

# class Son(Father):
#     def prints(self):
#         print(Father.property)
#         print(GrandFather.property)

# s = Son()
# s.prints()

# Hyrarchical inheritance
# class School:
#     def schoolName(self):
#         print("ABC School")
# class Student(School):
#     pass
# class Teacher(School):
#     pass
# class Principal(School):
#     pass

# s = Student()
# t = Teacher()
# p = Principal()
# s.schoolName()
# t.schoolName()
# p.schoolName()
# Hybrid inheritance
    # Simple and mutilevel
#     # multilevel and hyrarchiacal
# class School:
#     def schoolName(self):
#         print("School name is ABC")
# class Student(School):
#     pass
# class Teachers(School):
#     pass
# class library(School):
#     pass
# class allPerson(library):
#     pass

# s1 = Student()
# T1 = Teachers()
# a = allPerson()
# a.schoolName()
# multiple inheritance
# class Dad:
#     def Property(self):
#         print("Dad have House")
# class Mom:
#     def Proerties(self):
#         print("Mom have gold and silver")
# class Son(Dad,Mom):
#     pass

# S = Son()
# S.Proerties()
# S.Property()

# # constructor

# class Students:
#     def __init__(self):
#         print("The students are Learning Python Oop")
# s1 =Students()
# # polymorphism
    # Method overloading
# class Calculator:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
    
# calc = Calculator()
# calc.add(10,20,40)
# calc.add(10,20)
# calc.add(10)
    # method overridding
class Payment:
    def pay(self):
        print("Pay The Payment")
class Gpay(Payment):
    def pay(self):
        print("Pay The Payment via Gpay")
class PhonePe(Payment):
     def pay(self):
        print("Pay The Payment via PhonePe")
class Cash(Payment):
     def pay(self):
        print("Pay The Payment via Cash")

G = Gpay()
P = PhonePe()
C = Cash()
Pn = Payment()
G.pay()
P.pay()
C.pay()
Pn.pay()


# abstraction

from abc import ABC,abstractmethod
class Loan(ABC):
    @abstractmethod
    def intrest(self):
        pass
class SBI(Loan):
    def intrest(self):
        print("SBI offered me a loan for 8% Intrest rate")
class HDBC(Loan):
    def intrest(self):
        print("HDBC offered me a loan for 6% Intrest rate")

H =HDBC()
S = SBI()
H.intrest()
S.intrest()
# # composition
class Engine:
    def Start(self):
        print("Engine Starts")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.Start()
        print("Car is moving")
c= Car()
c.drive()

# operator overloading

class Students:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks+other.marks
    
s1 = Students(80)
s2 = Students(70)
print(s1+s2)