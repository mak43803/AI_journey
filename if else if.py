   
#  Python If–Else Practice Questions
# Q1.

# Take a number from the user.
# If the number is greater than or equal to 100, print "Big number",
# otherwise print "Small number".

# Q2.

# Take age from the user.
# If age is 18 or more, print "Eligible to vote",
# otherwise print "Not eligible".

# Q3.

# Take a number from the user.
# If the number is even, print "Even number",
# otherwise print "Odd number".

# Q4.

# Take marks from the user and print grade:

# 90 and above → A

# 80–89 → B

# 70–79 → C

# else → Fail

# Q5.

# Take temperature from the user:

# Above 30 → "Hot"

# 15–30 → "Normal"

# Below 15 → "Cold"

# Q6.

# Take three numbers from the user.
# Print the largest number.

# Q7.

# Take a year from the user.
# Check if it is a leap year.

# Q8.

# Take salary from the user.
# If salary is more than 50,000 → bonus = 10%
# otherwise → bonus = 5%
# Print total salary.

# Q9.

# Create a simple login system:
# Take username and password.
# If username is "admin" and password is "1234",
# print "Login successful",
# otherwise print "Invalid credentials".

# Q10.

# Take a number from the user.
# If the number is divisible by both 5 and 11, print "Yes",
# otherwise print "No".


num= int(input("enter the number"))

if num % 2 == 0:
    print("even number")
else:
    print("odd number")


age = int(input("enter the age"))

if age >= 18:
     print("you are eligiable")
else:
    print("uh are not eligiable")


num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

if num1 > num2:
    print(" greater number", num1)
else:
    print("greater number",num1)


marks = int(input("enter the marks"))

if marks >= 40:
    print("pass")
else:
    print("fail")

temp = int(input("enter the temperature"))
if temp >= 30:
    print("hot")
elif 15 <= temp <= 30:
    print("normal")
else:
    print("cold")

marks = int(input("enter the marks"))

if marks >= 90:
    print("a")
elif marks >= 80:
    print("b")
elif marks >= 70:
    print("c")
else:
    print("fail")        

hour = int(input("enter the hour"))

if 5 <= hour <= 11:
    print("good morning")
elif 12 <= hour <= 16:
    print("good afternoon")
elif 17 <= hour <= 20: 
    print("good evening")
else:
    print("good night")        

num = int(input("enter the number"))

if num > 0:
    if num % 2==0:
        print("postive even number ")
    else:
        print("postive odd number")
else:
    print("not positive")


e = int(input("enter the age"))

if age > 18:
    user= input("do uh have a license (yes/no)")
    ag

marks = int(input("enter the maks"))

if marks > 33:
    if marks > 75:
        print("distinction")
    else:
        print("pass")
else:
    print("fail")
        
        
marks = int(input("enter the marks"))

if marks >= 60:
    income  = int(input("check family income less than 20000"))
    
    if income <= 20000:
     print("scholarship approved")    
      
    else:
     print("income to high")
else:
    print("not eligiable")
    
marks = int(input("enter the marks"))

if marks >= 33:
    if marks >= 80:
        print(" grade A")
    elif marks >= 60:
        print("B")
 
    else:
        print("grade C")
else:
        print("if marks are less than 33 fail")


temprature = int(input("enter the temprature"))

if temprature > 0:
    if temprature > 30:
        print("hot")
    else:
        print("normal")
else:
    print("freezing")        

balance = int(input(" enter the account balance"))
withdraw = int(input("enter the withdraw amount"))

if balance > 0:
    if balance <= withdraw:
        print("transaction sucessfull")
    else:
        print(" insufficent balance")
else:
      print("no money in account")

num = int(input("enter the number"))

if num > 10:
    if num < 50:
        print("between 10 and 50")
    else:
        print("greatear than 50")
else:
    print("10 or below")

units = int(input("enter the units "))

if units <= 0:
    print("invalid")
elif units <100:
    bills = units * 5
    print("total bill:",bills)
elif units < 200:
    bills = units * 7
    print("total bill:",bills)
elif units <300:
    bills = units *10
    print("total bill:",bills)

elif units < 400:
    bills = units * 15
    print("total bill:",bills)
else:
    print("total bill")


weight = int(input("enter the weight"))
distance = int(input("enter the distance km"))

if weight <= 0 or distance <=0:
        print("invald")
elif distance <= 50:
    if weight <=1:
        print("shipping cost 50")
    elif weight <=5:
        print("shipping cost 100")
    else:
        print("shipping cost 200")
else:    
        
     if weight<=1:
                print("80 shipping cost")
     elif weight <=5:
                print("shipping cost 150")
        
     else:
             print("print shopping cost 300")

age = int(input("enter the age")) 
day = input("enter the day (e.g ,sunday )".lower())

if age < 5:
    price = 0
    
elif age <12:
    price = 100
    
elif age <59:
    price = 200
    
else: 
    price = 150
    
if day == "sunday":
    price += 50
if price == 0:
        print("free")
else:
    print("ticket price", price)


speed = int(input("enter internet speed "))

if speed < 0:
        print("invalid")
if speed <10:
    print("basics")
elif  speed <50 :
    print("standard")
else:
    print("premium")
    
marks = int(input("enter the marks"))
attendence = int(input("enter the attendence"))

if marks <33:
    print("fail")
elif marks >= 33 and attendence  <75:
    print("not eligible")
else:
    print("passs")
    

