# array methods 

#1 append 

# will add the elemnt in the list
namesOfStudents = ["ankur","anuj","rahul","rohit"]

a1= namesOfStudents.append("sumit")
print(namesOfStudents)   #['ankur', 'anuj', 'rahul', 'rohit', 'sumit']
print(a1) #none  # returns none

#2 pop

# will remove last element if no index given
# if index will given it will remove that element from list

a2=namesOfStudents.pop()
print(namesOfStudents)
print(a2)                        # jasleen returns the element

#3 clear 

# will empty the list

a3=namesOfStudents.clear()
print(namesOfStudents)           #[]
print(a3)                        # none

# reverse()
# will reverse the list

nameOfLanguages =["python","js","java",]
a4=nameOfLanguages.reverse()
print(nameOfLanguages)  #['java', 'js', 'python']
print(a4)               #[none]

# remove ()
# will remove the particular element of list

a5=nameOfLanguages.remove("java")     # we have to give value
print(nameOfLanguages)            #['js', 'python']
print(a5)                         # returns none 


oceans=["artic","atlantic","pacific",'indian']
mahasagar=oceans
oceans[0] = "arctic"

# same memory
print(oceans)               #['arctic', 'atlantic', 'pacific', 'indian']
print(mahasagar)            #['arctic', 'atlantic', 'pacific', 'indian']


#count
# will count hte elements

alpha =["a","b","a","c","a","c"]
a5=alpha.count('a')
print(a5)                 #3

# index 
# will give the index of element 

a6=alpha.index("a")
print(a6)               #0
#will give first occurance if no preference is given

a7= alpha.index("a",1)
print(a7)                #2
# will give the next occuring index which we give in arguments


# extend 
# will extend the list 

num1 =[1,2,3,4,5]
num2 =[6,7,8,9,]

num1.extend(num2)
print(num1)         #[1, 2, 3, 4, 5, 6, 7, 8, 9]

num2.extend([10])   #[6, 7, 8, 9, 10]  we manually can pass list
print(num2)

# sort 
# will arrange alphabatically

listx = ["x","z","y"]
listx.sort()
print(listx)       # ["x","y","z"]


#sum
# for getting sum
scoresTest=[100,30,0,120,90]

# we need to find total scores
totalScore=sum(scoresTest)
print(totalScore)


# for loop in list 

states=["jk","himachal","uttrakhand","punjab"]
for items in states:
	print(items)

# jk
# himachal
# uttrakhand
# punjab
	

# if we want our output in list

# list comprihension

states1=[items for items in states]	
print(states1)               #['jk', 'himachal', 'uttrakhand', 'punjab']

scorest20=[10,30,50,60,20,40]
# we need to double the total scores 
scores2=[i*2 for i in scorest20]
print(scores2)                #[20, 60, 100, 120, 40, 80]




