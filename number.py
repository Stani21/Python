# Calculate the multiplication and sum of two numbers
# getting 2 input from users
# f-string was used to string formatting
print("the multiplication and sum of two numbers")
a=int(input("Enter the value : "))
b=int(input("Enter another value : "))
c=a+b
d=a*b   
print(f"The addition of two numbers {a} and {b} are {c}")
print(f"The multiplication of two numbers {a} and {b} are {d}")


#Calculating the Area and Perimeter of a Rectangle
#hint:Area of a rectangle: a*b,Perimeter of a rectangle: 2*(a +b)
#getting user input
print("Calculating the Area and Perimeter of a Rectangle")
a=int(input("Enter the first variable: "))
b=int(input("Enter the second variable: "))
Area_of_rectangle=a*b
perimeter_of_a_rectangle=2*(a+b)
print(f"The area of the rectangle be {Area_of_rectangle}")
print(f"The perimeter of a rectangle be {perimeter_of_a_rectangle}")



#BODMAS rule - brackets,order,division,multiplication,addition and subtraction 
print("Moving towards BODMAS")
a=int(input("Enter the first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: "))
e=(a+b)*c/d
print("Result value =",e)


#Testing if a number is even or odd
#if the number is even it the remainder will be zero
print("Testing if a number is even or odd")
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")




