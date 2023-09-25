import numpy as np

# Indexing with 1D array


a1=np.arange(1,11)
print(a1)            #[ 1  2  3  4  5  6  7  8  9 10]

print (a1[0])  #1
print (a1[-1])   #10 # welcomes negative indexing 
print( a1[8]) #9
#print (a1[20])  will give error



# slicing in 1D array 
# does not considered the last value
# returns array
a2 = np.arange(2,21,2)
print(a2)    #[ 2  4  6  8 10 12 14 16 18 20]

x1=a2[2:6]  # will print from 2nd to 5th index
print(x1)   #[ 6  8 10 12]
print(a2)   # old array will remains same

x2=a2[:]  #[ 2 4  6  8 10 12 14 16 18 20]
x3=a2[1:]  #[ 4  6  8 10 12 14 16 18 20]   # if remains blank count till end
x4=a2[:4]  # [2 4 6 8] # if remains blank it counts from0 index

print(x2,x3,x4)


# slicing in 2D array

a3= np.arange(3,30,3).reshape(3,3)

print(a3)

# [[ 3  6  9]
#  [12 15 18]
#  [21 24 27]]

# we want element 3,6,12,15

x5=a3[0:2,0:2]  # last elemnt not included
print(x5)

# we want 12 15 24 27   ?

x6= a3[1:3,1:3:]
print(x6)

# we want last row
a3[-1]

# slicing with face masking

a5=np.arange(1,13,2)
print(a5)    #[1 3 5 7 9 11]

x6= a5>5
print(x6 ) #[False False False  True  True  True]

#x7 = (a5-3==0) or (a5-2==0)
# print(x7)  will give error

x8 = (a5 - 3 ==0) | (a5-5==0)   # we use | instead of or
print(x8)   #[False  True True False False False]


# with 2D array 

a6= np.arange(1,13).reshape(3,4)
print(a6)

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

x9 = a6%2 ==0
print(x9)


# homework
score = np.random.randint(10,100,15).reshape(5,3)
print(score)  # will give different result everytime due to randit
# [[59 72 34]
#  [33 67 88]
#  [42 82 22]
#  [25 10 51]
#  [15 22 42]]

mask1 = score > 50
mask2 = score < 35

result1=score[mask1 | mask2]
print(result1)   #[60 28 89 70 59 18 76 88 53 26 85 68 31]


1. # slice the array to get below name
s = np.array([['Priya', 'Rohit', 'Aryan'], ['Neha', 'Avni', 'Akash'],['Arjun', 'Riya', 'Devanshi']])

# ([['Priya', 'Rohit', 'Aryan'],
#   ['Neha', 'Avni', 'Akash'],
#   ['Arjun', 'Riya', 'Devanshi']])

# 1. 'Priya', 'Rohit', 'Aryan'
# 2. 'Riya','Devanshi'
# 3. 'Neha', 'Avni', 'Akash' 'Arjun', 'Riya', 'Devanshi'
# 4. 'Avni'
# 5. 'Neha'

#1 
result2= s[:1,0:]
print(result2)

result3 = s[2:3,1:3]
print(result3)

result4=s[1:,:]
print(result4)

result5=s[1:2,1:2]
print(result5)

result6= s[1:2,:1]
print(result6)