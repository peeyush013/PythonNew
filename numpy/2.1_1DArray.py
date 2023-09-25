import numpy as num

# 1D Array

l1=[1,2,3,4,5,6,7,8,9]

#converting list in ndarray

a1=num.array(l1)
print(a1,len(a1),type(a1))          #[1 2 3 4 5 6 7 8 9] , 9 , 'numpy.ndarray'>

# shape 
# will return the length and dimension in a tuple

x1=a1.shape   
print(x1,type(x1),len(x1))   #(9,) <class 'tuple'>  #len 1
#size 
# wil return the length or number of elements

x2=a1.size
print(x2,type(x2))   #9   ,int

# ndim 
# will return the dimensions of array

print(a1.ndim)                #1

# 1D array creation

#1. by passing a list 
#2. using arange() method

# arange is similar to range 

x3=num.arange(1,20,2)   # will not include last element
print(x3)          #[ 1  3  5  7  9 11 13 15 17 19] 

print(x3.ndim)    #1 
print(x3.shape)   #(10,)
print(x3.size)    #10




#3. using linspace
# last element of range is included
# linspace is same as arange but here we can give toatl number of elements

x4=num.linspace(1,8,4)
print(x4)                #[1. 3.33333333 5.66666667 8. ]
print(x4.ndim)   #1
print(x4.size)   #4
print(x4.shape)  #(4,)

