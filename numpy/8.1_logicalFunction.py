import numpy as np


# logical function

# any
# all
# will return boolean value

# any means any non zero value present or not 

a1 = np.array([1,2,3,4,0])
a2 = np.array([1,2,3,4,5])
a3 = np.array([0,0,0,0,0])
a4 = np.array([0,0,0,0,1])

print(np.any(a1))  #True
print(np.any(a2))  # True
print(np.any(a3))  # False
print(np.any(a4))   # True

# all means all elements are non zeroes

print(np.all(a1))  # false
print(np.all(a2))  #true
print(np.all(a3))  # false
print(np.all(a4))   #false

# can do element wise operation

print(a1>=a2) #[ True  True  True  True False] 
print(np.any(a2>a1))  #True
print(np.all(a2>a1))  #False



