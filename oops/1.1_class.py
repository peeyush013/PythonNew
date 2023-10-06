# class 

class Laptop:
	#properties 
	brand="hp"
	ram=12
	cpu=7.0

	#methods
	def windows(self):
		print("support windows")

	def linux(self):
		print("dont support linux")	

inspiron = Laptop()   # we can make as many as objects

# class variable can be accessible without creatin object on class
print(Laptop.brand)
print(Laptop.cpu)
print(inspiron.brand)
print(inspiron.cpu)

inspiron.windows()
inspiron.linux()


# we can make as many as objects from a class

pavallion = Laptop()

print(pavallion.brand)
print(pavallion.linux())


