#comparision operators 
# two entity ke beech mei comparision operation then output in boolean i.i. true or false 
# < ,> , <= ,>= , != , ==

print (1==1) #True
print (1!=1) #False
print (1!=1) #False





#logical operators 

#and 

# True + True = True
#True + False = False 
#False + False = False 

print (1==1 and 2==2)  
print (1!=1 and 2==2)
print (1!=1 and 2!=2)


# or 

# True + True = True
#True + False = True
#False + False = False 

print (1==1 or 2==2)    #True
print (1!=1 or 2==2)    #True
print (1!=1 or 2!=2)    #False

#not
# true = False 
#false = True

print (not 1==1  ) #False
print (not 1!=1)   #True



# conditional statement 
# 1 input and multiple outcomes 

#example 
# tickets > 0 < 5 => discoutn 5 percent
# tickets > 5 < 10 => discoutn 15 percent
# tickets > 10 < 20 => discoutn 5 percent
# tickets > 20 < 30 => discoutn 5 percent



# if => will run when condition is true 
t= 24
if  (t > 0 and t < 5):
    print ("5 percent discount")
    
if (t>5 and t < 10):
    print("10 percent discount")

if(t>20):
    print("20 percent discount")
    
# all if conditions will be checked and all true conditions will be printed





#elif
# will not run if if condition will get true 
# will stop running if elif condiion get true
# will not check all conditions if it gets true


t= 24
if  (t > 0 and t < 5):
    print ("5 percent discount")
    
elif (t<= 5 ):
    print("10 percent discount")

elif(t<= 20):
    print("20 percent discount")

elif(t<= 30):
    print("30 percent discount")

elif(t<= 40):
    print("40 percent discount")
    


#else 
# will run if if and elif condition become false 

t= 40
if  (t > 0 and t < 5):
    print ("5 percent discount")
    
elif (t<= 5 ):
    print("10 percent discount")

elif(t<= 20):
    print("20 percent discount")

elif(t<= 30):
    print("30 percent discount")

elif(t< 40):
    print("40 percent discount")
    
else :
    print ("ticket limit exceeded")   #ticket limit exceeded
    
	





