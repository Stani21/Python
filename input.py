#getting input from user
#input() - default function
#name - variable
#print-output function
print("Enter your name")
name=input("Enter your name: ")
print(name)


#getting input from user as integer of float
#int-converting to number(Type casting)
print("Enter a number")
sur_name=int(input("Enter the number: "))
print(sur_name)


import getpass
#getpass will help to secure your information not to display on screen
password =getpass.getpass("Enter a string: ")
print("password Entered")
#store u r input in password variable display the print statement

#this function is used to format the string the place where it should need to replace by {}
print("This is about format function")
first_name=input("Enter your first name: ")
last_name =input("Enter your last name: ")
print("Hello {} and your last name is {} is that correct?".format(first_name,last_name))


#1. Print String
# Statement:
# =========
# Write a Python program to print the following string in a specific format (see the output).

# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 

# Output :
# Twinkle, twinkle, little star,
#     How I wonder what you are! 
#         Up above the world so high,
#         Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#     How I wonder what you a

print("""Twinkle, twinkle, little star,
        How I wonder what you are! 
        Up above the world so high,
         Like a diamond in the sky.  
     Twinkle, twinkle, little star, 
         How I wonder what you a""")

#DOCUMENTATION___STRING