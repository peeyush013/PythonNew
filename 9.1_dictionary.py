# Dictionary --> dont store elements by index , no duplicate keys

studentInfo= {
"firstName": "Ankur",
"lastName":"Deswal",
"age":27
}

#print(studentInfo[1])  will give error 

# crud

# retriving the value

e1=studentInfo["firstName"]
print(e1)  # Ankur

#
e2=studentInfo.get("firstName")
print(e2)   #Ankur

# we cannot use dot notation , only bracket notation

print(studentInfo["age"]) #27

# updating the value

studentInfo["age"] = 28
print(studentInfo["age"]) 

#
e3= studentInfo.update({"age":30})
print(e3)

# deleting the values

x=studentInfo.pop("age")
print(x)  #28
print(studentInfo)   # will give new dictionary

print(len(studentInfo))  #2




studentInfo2 = {
	"firstName": "palash",
	"lastName" : "sharma",
	"firstName":"jitu"  # will update the newest same attribute
}
print(studentInfo2)


# for loop on dictionary

for keys in studentInfo2:
	print(keys,studentInfo2[keys])


vehicle = {
    "color":"red",
    "regNo":123,
    "city":"pune"
}

# getting the properties
for x in vehicle.keys():
	print(x)

# getting the values
for y in vehicle.values():
	print(y)	

# getting keys and values

for x,y in vehicle.items():
	print(x,y)



#
d1 ={
	"a":1,
	"b":2,
	"c":3
}
d2 = d1

d2.update({"a":4})
print(d2)   #{'a': 4, 'b': 2, 'c': 3}
print(d1)   #{'a': 4, 'b': 2, 'c': 3}

# will remain same no new memory created

d3=d1.copy()

d3.popitem()  # will remove random element
print(d3)   #{'a': 4, 'b': 2}  new memory created
print(d1)   #{'a': 4, 'b': 2, 'c': 3}  