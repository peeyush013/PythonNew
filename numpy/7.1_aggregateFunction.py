import numpy as np

# aggregate functions 

a1 = np. arange(0,50,5).reshape(2,5)
print(a1)

#[[ 0  5 10 15 20]
#  [25 30 35 40 45]]

# sum

a2 =np.sum(a1)
print (a2)     #225

a3 =np.sum(a1,axis=1)
print (a3) # [ 50 175]
a4 =np.sum(a1,axis=0)
print (a4) # [25 35 45 55 65]

# min # max # median

a5 = np.min(a1,axis=1)
a6= np.max(a1,axis=0)
print(a5)  #[ 0 25]
print(a6)  #[25 30 35 40 45]

#median
a7=np.median(a1,axis=1)
print(a7) #[10. 35.]

a8= np.count_nonzero(a1)
print(a8)  #9
