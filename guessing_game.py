
import random
import math
import unittest

gameChoice = "Y"
welcomeText=['\n\n--------------------Guessing game--------------------\n\n',
             'Welcome to the guessing game!',
             'You have 8 tries to guess the number.',
             'After 5 wrong tries, you will be provided with a hint.',
             'Good Luck!']

class TestGuessingGame(unittest.TestCase):

    '''Test case to ensure proper working of calculate score funcion'''
    def test_calcScore(self):
        self.assertEqual(calcScore(0, 8), 10.0)
        self.assertEqual(calcScore(8, 8), 0.0)
        self.assertEqual(calcScore(2, 4), 5)

    '''Test case to ensure proper working of hint funcion'''
    def test_hint(self):
        hints=["The number is more than 5","The number is even"]
        self.assertIn(hint('Y',6,10),hints)
  

'''This class is used for user defined exception so the user only inputs (y,n) as a choice'''
class err(Exception):
    pass

'''Used to display the welcome text in center alignment'''
for i in range(len(welcomeText)):
    print(welcomeText[i].center(len(welcomeText[0])-4))

def hint(choice,N,upperLimit):
    if(choice.upper()=="Y"):
        x = random.randint(0,1)
        if (x==0):
            if(N>upperLimit/2):
                hint = "The number is more than {}".format(math.floor(upperLimit/2))
            else:
                hint = "The number is less than {}".format(math.floor(upperLimit/2))
        else:
            if(N%2==0):
                hint = "The number is even"
            else:
                hint = "The number is odd"
    return hint


def calcScore(score,numberOfGuesses):
    calculatedScore = (1-(score/numberOfGuesses))*10
    return round(calculatedScore,1)


'''Main loop'''
while(gameChoice.upper() == "Y"):
    
    numberOfGuesses = 8

    while True:
        try:
            upperLimit = int(input("\nEnter the upper limit of the number you want to guess : "))
            break
        except ValueError: 
            print("Enter numbers only")

    '''This condition reduces the number of guesses based on the upper bound'''
    if upperLimit < numberOfGuesses:
        numberOfGuesses=math.ceil(upperLimit/2)

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
            
            if(choice.upper()=="Y"):
                print("\nHint :",hint(choice,N,upperLimit))
            
        
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

if __name__ == '__main__':
    unittest.main()