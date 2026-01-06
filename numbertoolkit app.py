
 
while True:
    print("\n--- Number Toolkit ---")
    print("1. Check Prime")
    print("2. Reverse Number")
    print("3. Sum of Digits")
    print("4. Factorial")
    print("5. Palindrome Check")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        n= int(input("enter the number"))
        if n < 2:
            print("not prime number")
            
    else:   
          prime = True
          for i in range(2,n):
            if n % i ==0:
              prime == False
              break
          if prime:
            print("prime number")
          else:
            print("not prime number")
        
        
                
            
        
        
            


    
    