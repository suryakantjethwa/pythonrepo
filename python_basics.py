# creates a tuple which is immutable
tup = ('Geeks', 'For', 'Geeks')
print(tup)


# define a set and its elements
myset = set(["Geeks", "For", "Geeks"])
#as set doesn't have duplicate elements so, 1 geeks will not be 

print('myset ===>' , myset)



#User input
#name = input("Enter your name: ")
#print("hello", name)
 
# Python program to illustrate
# selection statement
  


num1 = 34
if(num1>12):
   print("Num1 is good")
elif(num1>35):
   print("Num2 is not gooooo....")
else:
   print("Num2 is great")


# functions
def hello():
  print("hello")
  print("hello again")


hello()




# function with main
def getInteger():
   result = int(input("Enter integer: "))
   return result
  
def Main():
   print("Started")
   # calling the getInteger function and 
   # storing its returned value in the output variable
   output = getInteger()    
   print(output)
  
# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
   Main()
  

# Python program to illustrate
# a simple for loop
  
for step in range(5):   
   print(step)