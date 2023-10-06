class UserInfo:
	firstName="anuj"
	lastName="sharma"
	age=23
	
	def displayName(self):
		print(self.firstName,self.lastName)

ankur = UserInfo()
print(ankur.firstName)		# anuj
print(ankur.lastName)		#sharma
print(ankur.age)		    #23
ankur.displayName()         #anuj sharma

# here is the issue that the values are fixed for all the objects 
# so we need to update the values but it will consume more time and space

# constructor

class UserInfo2 :
	country = "India"   # class variable

	def __init__(self,fn,ln,age) -> None:
		self.firstname=fn
		self.lastname=ln
		self.age=age

	def displayFullName(self):
		print(self.firstname,self.lastname)
		
# now we can make as many as objects without having fixed values

palash = UserInfo2("palash","sharma",28)

print(palash.firstname)   # palash 
print(palash.lastname)    # sharma
print(palash.age)         # 28
print(palash.country)             # India it will remain same for all objects
palash.displayFullName()    # palash sharma



pankaj = UserInfo2("pankaj","bhardwaj",30)
print(pankaj.firstname)   # pankaj
print(pankaj.lastname)    # sharma
print(pankaj.age)         # 30
print(pankaj.country)     #India
pankaj.displayFullName()   # pankaj bhardwaj


# classmethod

class StudentInfo:
	#class variable
	standard="12th"

	@classmethod
	def changeStandard(a,newStandard):
		StudentInfo.standard=newStandard
		
    # instance variable
	def __init__(self,mat,eng,eco,acc,bs):
		self.mathsMarks=mat
		self.engMarks=eng
		self.ecoMarks=eco
		self.accMarks=acc
		self.businessmarks=bs
    
	#instance method
	def totalMarks(self):
		print(sum([self.mathsMarks , self.engMarks , self.ecoMarks,self.accMarks,self.businessmarks]))

Priyank = StudentInfo(80,70,88,90,84)

print(Priyank.standard)             # 12th
print(Priyank.mathsMarks)           # 80
print(Priyank.businessmarks)        # 84
Priyank.totalMarks()                 # 412

StudentInfo.changeStandard("11")    # updating class variable 
print(Priyank.standard)             # automatically updated on its object

