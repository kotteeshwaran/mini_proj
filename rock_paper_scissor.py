import random 

i =0

name = input("Enter you name:")
print('\n')

print("Welcome {}, to play Stone, Paper and Scissor game\n".format(name))

while True:

    print("\nEnter choice \n1.Stone \n2.Paper \n3.Scissor")

    choice = int(input("\nEnter the choice:"))

    if choice == 1:
        choice_name = 'Stone'
    elif choice == 2:
        choice_name='Paper'
    elif choice == 3:
        choice_name='Scissor'

    computer_choice = random.randint(1,3)
    
    if computer_choice == 1:
        computer_choice_name='Stone'
    elif computer_choice == 2:
        computer_choice_name='Paper'
    elif computer_choice == 3:
        computer_choice_name='Scissor'
    
    print("\nThe computer\'s choice is :{}".format(computer_choice_name))

    print('{} vs {}\n'.format(choice_name,computer_choice_name))

    if (choice ==1 and computer_choice ==3) or (choice == 2 and computer_choice == 1) or (choice ==3 and computer_choice==2):
        print("{} wins".format(name))
    
    if (computer_choice == 1 and choice ==3) or (computer_choice == 2 and choice==1) or (computer_choice==3 and choice==2):
        print("Computer wins")
    if (choice ==1 and computer_choice ==1) or (choice==2 and computer_choice ==2) or (choice == 3 and computer_choice == 3):
        print("Tie")
    
    value=input('Do you want to continue press Y/N:')
   
    if value == 'n' or value == 'N':
        break


    


    