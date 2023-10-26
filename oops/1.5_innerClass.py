


# # program 2
# class Person:
#     def  __init__(self,fn,ln,dd,mm,yy):
#         self.firstName = fn
#         self.lastName = ln
#         self.db = self.DOB(dd,mm,yy)

#     class DOB:
#         def __init__(self,dd,mm,yy):
#             self.dt = dd
#             self.mn = mm
#             self.yy = yy

#         def displayDate(self):
#             print(self.dt,self.mn,self.yy)

# amol = Person("amol","rao",12,34,1990)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.db)   #<__main__.Person.DOB object at 0x00000150B403BC40>
# print(amol.db.dt)  # we can iterate to dt
# e = amol.db

# print(e.dt)
# print(e.mn)
# print(e.yy)
# e.displayDate()

# # program3
# class Person:
#     def __init__(self,name):
#         self.fullName = name

#     def displayName(self):
#         print(self.fullName)

#     class DOB:
#         def __init__(self):
#             self.dd = 12
#             self.mm = 7
#             self.yy = 1990

#         def displayDate(self):
#             print(self.dd,self.mm,self.yy)

#         class Display:
#                 greet = "hello"

# chinmay = Person("chinmay deshpande")
# chinmay.displayName()

# q1  = Person("amol rao").DOB()
# print(q1.yy)
# print(q1.mm)
# print(q1.dd)
# q1.displayDate()


# q2  = Person("ram dani").DOB().Display()
# print(q2.greet)




class Marksheet:
	def __init__(self,mat,eng,phy,ioc,oc,bio) :
		self.maths=mat
		self.english=eng
		self.science=self.Science1(phy,ioc,oc,bio)

	def displayTotalMarks(self):
		print(self.english + self.maths)

	class Science1:
		def __init__(self,phy,bio,oc,ioc) :
			self.physics=phy
			self.chemistry=self.Chemistry1(oc,ioc)
			self.biology=bio	

		def scienceMarks(self):
			print(self.physics+self.chemistry+self.biology)	

		class Chemistry1:
			def __init__(self,oc,ioc) :
					self.organicChemistry=oc
					self.inorganicChemistry=ioc


asma = Marksheet(80,70,20,18,25,19)
print(asma.science.chemistry.inorganicChemistry)   #19

asma.displayTotalMarks()   #150

ameen = Marksheet.Science1(100,99,50,40)
print(ameen.chemistry.inorganicChemistry)      #40
#ameen.maths   cannot accesable as its made on sub or inner class