i = 1
while i<5:
    print(i)
    i+=1

i = 1
while i< 10:
    print(i)
    i +=1

i = 2
while i<20:
    print(i)
    i+=2


for i in range ( 1,6):
    print(i)

for i in range (1, 11):
    print( 5* i)

total = 0 
for i in range ( 1, 11):
    total += total = 0 total = 0 total = 0 
for i in range ( 1, 11):
    total += i
    print("sum:" ,total)

i = 1
while i <50:
    print(i)
    i += 1

i = 3
while i <100:
    print(i)
    i +=3
    
    
total = 0

for i in range( 1, 21):
    if i % 2 == 0:
        total += i
print("sum of even numbers" , total)

total = 0

for i in range( 1, 51):
    if i % 2== 1:
        total += i
        print("sum of odd numbers" , total)

total = 0 

for i in range (1 , 10):
    print(i)

total = 0

for i in range (1, 21):
    if i % 2 == 0:
        total += i
        
        print("sum  of even numbers:" ,total)

total =0

for i in range (1, 50):
    if 1 % 2==1:
        total +=i
        
        print("sum of oddd numbers:", total)

num = int(input("enter the number"))

fact = 1
for i in range (1 , num +1):
    fact = fact *i
    
    print("factorial:", fact)
    
    
total = 0

for i in range (1 , 50):
    if i % 3==0 and i % 5==0:
        print(i)

num = 7

for i in range ( 1, 11):
    print(num, "x", i, "=" , num *i)

num = int(input("enter the number"))

if num < 0:
    print("invalid")
else:
    fact =1 
    for i in range (1 , num +1):
     fact *= i
    print ("factorial:", fact)

num = int(input("enter the number"))

if num > 0:
    for i in range (1,11):
        print(num,"x", "=", num *i)
else:
    print("invalid number")

num = int(input("enter the number"))

if num % 2==0:
    
    for i in range (1 , num +1):
    
        if i % 2==0:
            print(i)
            
else:
              
    for i in range (1 , num +1):
    
        if i % 2==0:
            print(i)

num = int(input("enter the number"))

if num < 10 :
    
    fact = 1
    
    for i in range (1,num +1):  
        
        fact = fact* i
        
    print("factorial:", fact)

else:
    total = 0 
     
    for i in range (1,num +1):
        total = total +i
        
        print("sum:", total)


num = int(input("enter the number"))

if num <0:
    print("invalid")
else:
    
    total =0
    for i in range (1 , num +1):
        total +=i
        
        print("sum:", total)
    
    
num = int(input(" enter the number"))

if num >0:
    total = 0
    
    for i in range(1, num+1):
        
        total += i
        print("sum:", total)
        
    else:
        print("invalid")
        
num = int(input(" enter the number"))

if num % 2 == 0:
    print(" even numbers")
    
    for i in range ( 1, num + 1):
        
        if i % 2 == 0:
            
            print(i)
            
    else:
        print("odd number")
        for i in range (1, num +1):
            if i % 2==1:
                print(i)
                
num = int(input(" enter the number"))

if num % 2==0 and  num % 5==0:
    
    total = 0
    
    for i in range ( 1, num +1):
        
        total += i
        
        print("sum of all number:", total)
            
    else:
        count =0
        
        for i in range ( 1, num +1):
            
            if i % 3==0:
                count +=1
                print(" count of nuumber divisible by 3:", count)

n = int(input("enter the number"))

if n % 3==0:
    total = 0
    for i in range (1, n +1):    
      if i % 5==0:    
            total += i   
      print("sum:",total)
    else:
        count = 0
        for i in range (1, n+1):  
            if i % 2==0:  
                count +=1
                print("count:", count)
              
n = int(input("enter the number"))   

if n % 2==0:
  
  fact =1
  for i in range ( 1, n +1):
    
    fact *fact +i
    
    print("factorial:", fact)
    
  else:
    for i in range (1,n+1):
      
      print("sum of digits:")
    
    
i =1
while i <= 5:
  print (i)
  i +=1

n = int(input("enter the number"))
total =0
i = 1
while i <= n :
  total += i
  print ("sum of number",total)
  i +=1

n = int(input("enter the number"))


fact =1
i=1
while i <= n:
  fact *=i
  i+=1
  print("factorial",fact)
  
  
i = 1
while i <=20:
  if i% 13==0:
    break
  print(i)
  i+=1
  

i=1

while i<20:
  if i % 3==0:
    i+=1
    continue
  print(i)
  i+=1
            

  
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        print("Stopped")
        break



for i in range (1, 100):

   if i == 70:
    break
  
   if i % 3==0:
      continue
    
   print(i)


while True:
    num = int(input("Enter a number: "))
    
    if num <0:
      print("invalid")
      continue
    
    elif num == 0:
       print("Stopped")
       break
     
    else:
      print("print the number")


total =0

while True:
  num = int(input("Enter a number: "))
  
  if num == -1:
    break
  
  if num %2==0:
  
   total +=num
  
print("final sum :", total)
    
  
while True:
   num = int(input("Enter a number: "))


   
for i in range(1,100):
  if i % 7==0 and i  %  11==0:
    print("first match:",i)
    break
  
while True:
  password = (input("Enter a password: "))
  
  if password == "python123":
    print("access granted")
    break
  else:
    print("wrong password and try again")

for i in range (1,50):
      
  if i == 37:
      break
  if i % 4==0:
      continue
  print(i)
    
  
while True:
  num = int(input("Enter a number: "))

  for i in range (1,11):
   print(num,"x", i,"=" ,num*i)
  
  maz= input("another table (y/n): ")
  if maz != "y":
    break


  
  
         
               
                
                
                
                
                
            
        