x= 100
y= 50
z= 120

if (x>y and x>z):
	print("x is greatest")

elif (y>x and y>z):
	print("y is greatest")

else :
	print("z is greatest")	  # z is greatest



a = 10
b=5
c =2 

if(a>b):
	if(a>c):
		print("a is greatest")     #a is greatest

		

elif (b>a):
	if(b>c):
	    print("b is greatest")
	

else:
		print("c is  greatest")	



# ternary operstor 

rohit = 19
mohit = 22

if(rohit>mohit):
	print("rohit is elder")
else:
	print("mohit is elder")	

print("mohit is elder")	if (mohit>rohit) else print("rohit is elder")   #mohit is elder


#
kunal = 17
kushi = 18
kusum = 19

votingAge =18 

if(kunal>=votingAge):
	print("kunal can vote")

else :
	print("kunal can't vote")	

if(kushi>=votingAge):
	print("kushi can vote")

else :
	print(" kushi can't vote")

if(kusum>=votingAge):
	print("kusum can vote")

else :
	print(" kusum can't vote")


# here the problem arises that we have to write if else many times which lengthen the code	