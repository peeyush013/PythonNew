import numpy as np

# broadcasting 

#         [10,20,30,40]                            [1],-> ->  will stretch rightwards
#         will stretch downwards                  [2],-> ->
#                                                 [3] -> ->
#                                                 [4]-> ->


# rules 
# arrangements of elements of coloum of first array = arrangement of elemts of coloumn of second

a1 = np.array([10,20,30,40]) #list  =  1D Array 
a2 = np.array([[1],[2],[3],[4]]) #list of list = 2D array

a3 = a1+a2
print(a3)
# [[11 21 31 41]
#  [12 22 32 42]
#  [13 23 33 43]
#  [14 24 34 44]]


# rows are 1 axis or h split , coloums are 0 axis or v split

a4=np.split(a3,4)
print(a4)

# [array([[11, 21, 31, 41]]), array([[12, 22, 32, 42]]), array([[13, 23, 33, 43]]), array([[14, 24, 34, 44]])]
# default split is 0 axis or h split or coloumn split

a5 = np. split (a3,4,axis=1)
print(a5)

# [array([[11],
#        [12],
#        [13],
#        [14]]), array([[21],
#        [22],
#        [23],
#        [24]]), array([[31],
#        [32],
#        [33],
#        [34]]), array([[41],
#        [42],
#        [43],
#        [44]])]


# hsplit
a6=np.hsplit(a3,4)
print(a6)
# [array([[11],
#        [12],
#        [13],
#        [14]]), array([[21],
#        [22],
#        [23],
#        [24]]), array([[31],
#        [32],
#        [33],
#        [34]]), array([[41],
#        [42],
#        [43],
#        [44]])]

a7=np.vsplit(a3,4)
print(a7)
#[array([[11, 21, 31, 41]]), array([[12, 22, 32, 42]]), array([[13, 23, 33, 43]]), array([[14, 24, 34, 44]])]



