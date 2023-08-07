
import random
import math

gameChoice = "Y"
numberOfGuesses = 8
welcomeText=['\n\n--------------------Guessing game--------------------\n\n',
             'Welcome to the guessing game!',
             'You have 8 tries to guess the number.',
             'After 5 wrong tries, you will be provided with a hint.',
             'Good Luck!']

class err(Exception):
    pass

for i in range(len(welcomeText)):
    print(welcomeText[i].center(len(welcomeText[0])-4))

def hint(choice,N,upperLimit):
    if(choice.upper()=="Y"):
        x = random.randint(0,1)
        if (x==0):
            if(N>upperLimit/2):
                print("\nHint : The number is more than",math.floor(upperLimit/2))
            else:
                print("\nHint : The number is less than",math.floor(upperLimit/2))
        else:
            if(N%2==0):
                print("\nHint : The number is even")
            else:
                print("\nHint : The number is odd")

def calcScore(score,numberOfGuesses):
    calculatedScore = (1-(score/numberOfGuesses))*10
    return round(calculatedScore,1)


while(gameChoice.upper() == "Y"):
    
    while True:
        try:
            upperLimit = int(input("\nEnter the upper limit of the number you want to guess : "))
            break
        except ValueError: 
            print("Enter numbers only")

    N = random.randint(1,upperLimit)
    win=False
    for i in range (numberOfGuesses):
        
        while True:
            try:
                userGuess = int(input("\nEnter your guess : "))                
                break
            except ValueError: 
                print("Enter numbers only")
        score = i
        
        if(userGuess==N):
            print("\nYou win!!!")
            win=True
            # score=i
            break

        print('\nWrong guess')
        if(i!=(numberOfGuesses-1)):
            print('\nYou have %i tries left'%(numberOfGuesses-(i+1)))

        if(i==4):
            
            while True:
                try:
                    choice = input("\nDo you require a hint? (Y/N) : ")
                    if(choice.upper()!='Y' and choice.upper()!='N'):
                        raise err
                    break
                except err: 
                    print("Invalid choice")
            hint(choice,N,upperLimit)
            
        
    if(win==False):      
        print("You have used up all your guesses")
 

    print("Your score : ", calcScore(score,numberOfGuesses-1))
        
    
    while True:
        try:
            gameChoice = input("\nDo you want to try again? (Y/N) : ")
            if(gameChoice.upper()!='Y' and gameChoice.upper()!='N'):
                raise err
            break
        except err: 
            print("Invalid choice")
    
print("\n\n--------------------Thank You for playing--------------------")