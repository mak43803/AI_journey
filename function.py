# def greet (name):
#     print("hello", name)
    
# def add(a, b):
#     return a + b
# print(add(10 , 20))

# def print_number(n):
    
#     i =1
#     while i<n:
#         print(i)
#         i+=1
# print_number(10)


# def add(a, b):
#     return a + b

# result = add(5, 7)
# print(result)


# def mazzu (n):
    
#   for i in range (1,n+1):
      
#     if i % 2==0:
        
#       print(i)
# mazzu (10)
  
# def count_function (n):
    
#     for i in range (1, n+1):
        
#         print (i)
    
# count_function(10)
    

while True:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /, %, **, //): ")
    b = float(input("Enter second number: "))

    
    again = input("Do you want to calculate again? (y/n): ").lower()
    if again != "y":
        print("Calculator closed.")
        break
2
    