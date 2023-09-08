## OS MODULE
## inbuilt in python , no need to install

# but we have to import
import os

## getting help 

# help os  (manual pages)  # help dir

# checking the current location

# current working directory of exisiting dir

os.getcwd() #C:\Users\user\Desktop\pythonNewBatch

# changin the directory
#os.chdir(r'D:\New folder')   # stem cannot find the file specified: 'D:\\New folder'

# making a new directory
#os.mkdir("demo2")  # will create folder in current working folder

# changin the dir to required one
#os.chdir(r"D:\New folder\demo2")

# we use r to avoid double slash

# creating dir using for loop
# for i in range(2,11):
#     os.mkdir(f"Emp{i}")

#deletion of directory    
#os.rmdir('Emp10/')	

# deleting dir using for loop
# for i in range(2,11):
#     os.rmdir(f"Emp{i}")


#os.listdir(r'D:\New folder\demo2')
# it will make list of all directory


