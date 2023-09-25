import numpy as np

#   LIST VS NUMPY

list1 =[2,4,6,8,10]

# we need to square for all the elements

#1   for loop
for items in list1:
	print(items*items)

# from this we get square but it will not come in list


#2   list comprehension

l1=[items**2 for items in list1]   #x**2 = x*x
print(l1)                            #[4, 16, 36, 64, 100]



list2=[1,3,5,7,9]
print(list1)
print(type(list1))# <class 'list'>

# converting list in to ndarray

arr1=np.array(list2)
print(arr1,type(arr1))            #[1 3 5 7 9] <class 'numpy.ndarray'>

# now , performing action on each elements

print(arr1**2)   # [ 1  9 25 49 81]


# why numpy

# 1. can perform elementwise operations
# 2. faster than list operations       
# its faster because its written in c language