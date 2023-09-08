
##1
# a = 10
# myName= "anuj"

# try:
# 	c=int(input("enter a number"))
# 	print(a/c)

# 	d=(int(input("enter a index")))
# 	print(myName[d])

# except ZeroDivisionError as z:
# 	print(z,"hi please enter a non zero number") #division by zero hi please enter a non zero number

# except IndexError as i :
# 	print(i)	# will not be called 



##2 else
# a = 10
# name2  = "anuj"

# try:
#     b = int(input("ENter a number other than zero"))
#     c = a/b
#     print(c)
#     p = int(input("ENter the index position to be called"))
#     print(name2[p])
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as f:
#     print(f)
# else: #this will get executed only if the code was without any excception
#     print("All codes executed successfully")

##3 finally

# a=10
# name3="anuj"

# try:
# 	c=int(input("enter a non zero number"))  #0
# 	print(a/c)

# 	d=int(input("enter a intex number"))
# 	print(name3[d])

# except ZeroDivisionError as z:
# 	print(z,"enter non zero num") # it will run

# except IndexError as i:
# 	print(i,"enetr valid index")

# else:
# 	print("all codes are good")

# finally:
# 	print("have a nice day")		#have a nice day





## 4 raise 

# raising the custom exception
#raising the user defined exception

# a = int(input("enter an Even number"))
# if a%2!=0:
#     raise Exception("Enter Even numbers only")
# else:
#     print("Entered number is Even")

# ## 5

# a= 10
# b= 12
# c = int(input("enetr a odd number"))

# if c%2 ==1:
# 	print("c is odd number")

# else :
# 	raise Exception ("please enter a valid number")	

## 6

# a = int(input("enter an Even number"))
# def evenNumber ():
# 	if a %2 == 0:
# 		print (" a is even number ")

# 	elif a%2 ==1:
# 		print("a is odd number")	

# 	else :
# 		raise Exception ("enter a even number")	


# evenNumber()


##

x=int(input("give your birth year"))
def age (x):
	currentYear = 2023
	if(x>currentYear):
		raise Exception ("invalid year")
	
	else:
		print(currentYear-x)

try:
	age(x)

except	:
	print("invalid year of birthh")		

finally :
	print("----good night----")	

