import random
i = 0
def password_function():
    upper = [chr(x) for x in range(65,91)]  #chr() is used to convert ascii values to alphabets and symbols
    lower = [chr(x) for x in range(97,122)]
    digits = [str(x) for x in range(0,10)]
    symbols = [chr(x) for x in range(32,48)]
   
    password = upper + lower + digits + symbols 
    output = "".join(random.sample(password,16))
    print(output)
    

print("Welcome to Password Generator")
n= int(input('Select a number to print number of passwords:'))
while i<n:
    i+=1
    password_function()









