# array methods 

#1 append 

# will add the elemnt in the list
namesOfStudents = ["ankur","anuj","rahul","rohit"]

a1= namesOfStudents.append("jasleen")
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