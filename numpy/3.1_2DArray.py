import numpy as num

# 2D Array creation

#1. using list

l1 =[[1,3,5,7],[2,4,6,8]]

array1 = num.array(l1)
print(array1)    #[[1 3 5 7][2 4 6 8]]

print(array1.ndim)    #2 
print(array1.size)    #8
print(array1.shape)   #(2,4)

#2. using arange  + reshape

array2 = num.arange(10,30,2)
print(array2)                 #[10 12 14 16 18 20 22 24 26 28]

print(array2.ndim)    #1
print(array2.shape)   #(10,)
print(array2.size)    #10

array3 = array2.reshape(2,5)
print(array3)   #[[10 12 14 16 18][20 22 24 26 28]]
print(array3.shape)   #(2,5)
print(array3.size)    #(10)
print(array3.ndim)    #2


# we can reshape again

array4= array3.reshape(1,10)
print(array4)     #[[10 12 14 16 18 20 22 24 26 28]]

#checking type and dtype
print(type(array4))    #<class 'numpy.ndarray'>
print(array4.dtype)    #int32



# 3. linspace + reshape

array5=num.linspace(2,16,8)
print(array5)    #[ 2.  4.  6.  8. 10. 12. 14. 16.]

array6= array5.reshape(4,2)
print(array6)
print(array6.ndim)   #2
print(array6.shape)  #(4,2)
print(array6.size)   # 8
print(array6.dtype)    #float64 


# row vector = it means only rows
# coloumn vector = it means only coloums