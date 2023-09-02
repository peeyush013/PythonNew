# in operator 

fruits =["apple",",mango","grapes"]

print("apple"in fruits)  #True
print("Mango" in fruits)  # False its case sensitive


#
if ("banana" in fruits):
	print("present")

else:
	print("its not part of arrey") #its not part of arrey


# updation of element

print(fruits) #['apple', ',mango', 'grapes']

fruits[2]="banana"
print(fruits)  #['apple', ',mango', 'banana']
print(type(fruits))  #list 

# for loop using range

evenNum =[2,4,6,8]
for i in range(len(evenNum)):
	#print(i) #0123 we will get index
	print(evenNum[i])  #2,4,6,8

countries=["india","indonasia","pakistan","italy","iceland"]	
for i in range(len(countries)):
	if(countries[i][0]!="p"):
		print(countries[i])


# for lopp without range
for i in countries:
	print(i) #india indonasia pakistan italy iceland

for i in countries:
	if(i[0]!="p"):
		print(i) #india indonasia pakistan italy iceland	

