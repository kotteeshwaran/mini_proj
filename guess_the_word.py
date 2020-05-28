import random
from collections import Counter

with open('C:/Users/dkott/Documents/Python/PROJECTS/list_words.txt','r') as file:

    myword= file.read().splitlines()

words=random.choice(myword)
print(words)
flag = 0
char =''

letterguessed=''
chance=13
correct = 0
print("Find the fruit")
print()
for dash in myword:         #it is used to print the dashes 
    print("-",end='')
print()
try:
    while chance!=0 and flag==0:
        print()
        chance-=1
    
        try:
            guess = str(input('Enter a charcter:'))
        except:
            print("Enter only letter")
            continue
    
    #validation of guess
        if not guess.isalpha():
            print("Enter only Letter")
            continue

        elif len(guess)>1:
            print("Enter a single character")
            continue

        elif guess in letterguessed:
            print("Already guessed letter")
            continue
    
    
        if guess in words:
            value = words.count(guess)
            for _ in range(value):
                letterguessed+=guess

        for char in words:
                       
            if char in letterguessed and (Counter(letterguessed) != Counter(words)): 
                print(char, end = ' ') 
                correct += 1

            elif Counter(letterguessed) == Counter(words):
                print("Congragulations")
                print("The word is:{}".format(words))
                flag=1
                break
                break
            else:
                print('-',end='')

    if chance<=0 and (Counter(letterguessed)!=Counter(words)):
        print('Your chances are over')
        print("The Word is {}".format(words))

except KeyboardInterrupt: 
    exit() 








  
   
   





