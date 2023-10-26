# # static method 
# # cannot 

# class Employee:
#     def __init__(self,fullName,age,salary):
#         self.fullName = fullName
#         self.age = age
#         self.salary = salary
#     def displayInfo(self):
#         print(self.fullName)
#         print(self.age)
#         print(self.salary)

# class EmployeeInfo:
#     @staticmethod
#     def displayInfo(e):
#         print(e.salary)
#         print(e.fullName)
#         print(e.age)

# abhisha = Employee("abhisha","34",salary=1000)
# abhisha.displayInfo()
# EmployeeInfo.displayInfo(abhisha)

# # program 3
# class PersonR:
#     # class variable
#     country = "India"
#     counter = 0
#     # setting instance variable via object
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#         PersonR.counter = PersonR.counter + 1

#     def displayName(self):
#         print(self.firstName+self.lastName)

#     @classmethod
#     def updateCountry(cls,cntry):
#         cls.country = cntry

#     @staticmethod
#     def countObj():
#         return PersonR.counter

# sarika = PersonR("sarika","pansare")
# print(sarika.firstName)
# print(sarika.lastName)
# PersonR.countObj()
# PersonR.updateCountry("nepal")



class Student:
	standard="10th"
	section="b"
	counter=0
	def __init__(self,fn,ln,rn) -> None:
		self.firstName=fn
		self.lastName=ln
		self.rollNumber=rn
	def displayName(self):
		print(self.firstName,self.lastName)	

	def changeStandard(self,newStandard):
		self.standard=newStandard	

	@classmethod
	def changeSection(cls,sec):
		cls.section=sec
	@staticmethod
	def countObject():
		return Student.counter()	


jugal =Student("jugal","sharma",20)

print(jugal.firstName)    #jugal
print(jugal.lastName)     #sharma
print(jugal.rollNumber)   #20
print(jugal.standard)     #10th
print(jugal.section)      #b    
print(jugal.counter)      #0
jugal.displayName()       # jugal sharma
#jugal.changeSection()  # cannot call on object
#jugal.countObject()


Student.changeSection("c")
print(jugal.section)       #c , it will change on class and object and also on new objects 

komal = Student("komal","sharma",19)
print(komal.section)       #c

#Student.changeStandard()  instance object cant callable on class

komal.changeStandard("12th")
print(komal.standard)         #12th it will change only for specific object
print(jugal.standard)         #10th

#now
Student.countObject()
print(Student.counter)
print(komal.counter)

