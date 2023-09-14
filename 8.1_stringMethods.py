# capitalize
# capitalize the first alphabet and uncapitalize the other

name="peeyushSHARMA"
a1=name.capitalize()

print(name)                     #peeyushSHARMA
print(a1)                       #Peeyushshamra

#lower
# will convert and return all elements in lower case
name2="PEEYUSH"
print(name2.lower())       #peeyush 
print(name2)

#upper
name3="pankaj"
print(name3.upper())   #PANKAJ


#strip
# remove the starting and end spaces

name4="     ankur "
x1=name4.strip()
print(x1,len(x1))    #5

# lstrip
name5= " toshi "
x2=name5.lstrip()
print(x2,len(x2))   # toshi ,6

# rstrip
# remove the right hand spaces

name6= " kajal  "
x3 = name6.rstrip()
print(x3,len(x3))    # kajal 6


# split 

# will split at given character and return list

address= "e-2-430-sultanPuri-delhi-110086"
x4=address.split("-")
print(x4,len(x4))              #['e', '2', '430', 'sultanPuri', 'delhi', '110086'] 

# join

# will join a list elements at given character and return string

x5= "/".join(x4)  # we are paasing a list as argument hence its not list method
print(x5,len(x5))  #e/2/430/sultanPuri/delhi/110086 31


# startswith

# returns boolen
# will check the first element 

name7="anujSharma"
x6=name7.startswith("A")
print(x6)                   #FALSE case sensitive

#endswith

x7=name7.endswith("a")
print(x7)                 #true




# find

# will return index value for given character or substring of first occurance
# will return -1 if substring not available

name8 = "krishnakanta"
x8=name8.find("x")
print(x8)           #-1

x9=name8.find("a")
print(x9)           #6 as give first occurane

x10= name8.find("a",7)
print(x10)              #8
# if we paas parameter it will give result after that index

x11= name8.find("a",9,10)
print(x11)                  #-1


# index
#  will return the index value of element same as find 
# will throw error if the element is not present

name9= "shuboto"
x12=name9.index("sh")
print(x12)

#x13=name9.index("x")

#print(x13)               #error



# count
# count the number of elements

name10 ="sanjana"
print(name10.count("a"))              #3

# isalpha()

# will return boolean and check that elemets are alphabets
name11 = "ankush"
print(name11.isalpha())   #true

#isdigit

phoneNumber="9868586848"
print(phoneNumber.isdigit())  #true



# isalnum

# will return true if alphabets or numeric or alphanumeric 
# will return false when there is special case
address3="e2430"
print(address3.isalnum())   #true












