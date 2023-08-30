x= 10
y= 12
print (x+y)
print (x-y)
print (x/y)
print (x%y)
print (x+x)
# 22
# -2
# 0.8333333333333334
# 10
# 20

print (type(x/y))  # float , any decimal value is float


# we use functions for saving time and code 
def Calculation (x,y):
    return (x+y , x-y , x/y , x*y , x%y)

a=Calculation(10,2)
b=Calculation (10,3)

print(a)  #(12, 8, 5.0, 20, 0)
print(b)  #(13, 7, 3.3333333333333335, 30, 1)

#types
# int             any positive and negative number non decimal
# float           any decimal number
# boolean         true or false
# string            "" string


# types of functions
#function without parameter and without return type 
def example1 ():
    print(10-1)
    print(12-2)
    
example1()	

#function with parameter and without return type 
def example2 (a,b):
    print(a+b)
    print(a-b)
    
example2(1,2)	# we cant use this code 

#function with parameter and with return type 

def example3 (x,y):
    return (x*y)
m = example3(5,4)
print(m) #20
# we can use the code further
print(m*2) #40
