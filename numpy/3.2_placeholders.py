import numpy as np

# PLACEHOLDERS

#1. zeros
# we can make array in which all elements are 0

#zeroes in 1d array
arr1=np.zeros([4])
print(arr1)    #[0. 0. 0. 0.]

# zeroes in 2d array
arr2=np.zeros([4,3])
print(arr2)      #[[0. 0. 0.] [0. 0. 0.][0. 0. 0.][0. 0. 0.]]

#2. ones

arr3=np.ones([5])
print(arr3)        #[1. 1. 1. 1. 1.]

arr4=np.ones([2,2])
print(arr4)  #[[1. 1.] [1. 1.]]

print(arr4[0][0])  #1

a12=100
b12=a12
c12=b12

b12=120
print(a12,b12,c12)

#3. eye

#will give 1 in diagonal

arr4= np.eye(4)
print(arr4)

# [[1. 0. 0. 0.]       
#  [0. 1. 0. 0.]       
#  [0. 0. 1. 0.]       
#  [0. 0. 0. 1.]]

#4. diag

arr5=np.diag([12,14,16,18])
print(arr5)

# [[12  0  0  0]       
#  [ 0 14  0  0]       
#  [ 0  0 16  0]       
#  [ 0  0  0 18]]