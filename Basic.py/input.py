#getting input from user
#input() - default function
#name - variable
name=input("Enter your name: ")
print(name)


#getting input from user as integer of float
#int-converting to number(Type casting)
sur_name=int(input("Enter the number: "))
print(sur_name)


import getpass
#getpass will help to secure your information not to display on screen
password =getpass.getpass("Enter a string: ")
print("password Entered")
#store u r input in password variable display the print statement