# # there are some exceptions which we need to handle 
# #try:
# #     the code where chances of exception is there
# #     code1
# #     code2
# #except:
# #     msg if the exception occurs

# a = 100
# b = 200
# c = 0

# print(a/b) #0.5
# #print(a/c) # ZeroDivisionError: division by zero


# x=10
# y=20
# z=0
# #rint(y/z)
# print("important line to be printed")  # will not print as above line got exception

# m=2
# n=0

# print(m*2)  #4

# try:
    
#     print(m/n)
    
    
# except:
#     print("there is some error")	# there is some error

# print("its important to be prnted")


# p=10
# q=15
# #c = input("Please enter a number ") #it will take input as string only
# c = int(input("Please enter a number ")) #typecasting

# print(p+q)
# try:
#     print(q/c)
    
# except:
#     print("please enter correct input ")
    
# print("line is important")



# j=20
# k=30
# l=int(input("enter an integer"))

# try:
#     print(k/l)  # if we give input as 0 it will catch divide by zero error error and except line will print
    
# except:
#     print("enter a coorect input ")	
    



# str="exception"
# print (str[1])
# print(str[6])
# print(str[20])    #IndexError: string index out of range

# string="EXCEPTION"


# try:
#     inp=int(input("please enter a number"))
#     print(string[0])
#     print(string[inp])

# except:
#     print("give valid input")



#
# str2="python"

# try:
#     input1=int(input("please enetr a number"))
#     print(str2[input1])

# except Exception as e:
#     print(e)              #string index out of range


# str3="python and javascript"

# try:
#     input2=int(input("please enetr a number"))
#     print(str2[input2])

# except Exception as e:
#     print(e) 


str3="python and sql"

try:
	input3= int(input("please insert a integer"))
	print(str3[input3])  
	
    # string index out of range give number between 0 to 15

except Exception as e:
	print(e,"give number between 0 to 15")








