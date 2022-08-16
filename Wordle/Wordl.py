import random

NUM_DIGITS=5
MAX_GUESSES=5


def main():  # sourcery skip: use-fstring-for-formatting
    print('''Wordl. 
By Edwin Arrieta
    
I am thinking of a 5 -digit word. 
Try to guess what it is. Here are some clues:
''' )
    while True: #Main game loop

        secretNum = getSecretNum()
        print('I have tought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses<= MAX_GUESSES:
            guess = ''

            ##while len(guess) != NUM_DIGITS or not guess.isdecimal():
            while len(guess) != NUM_DIGITS:
                print('Guess #{}: '.format(numGuesses))
                guess=input('> ')

            clues = getClues(guess, secretNum)
            print (clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses>MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))


        print('Do you want to play again?(yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('thanks for playing')

def getSecretNum():
    words=[] 
    with open("holamundo.txt", "r") as tf:
        lines = tf.read().split(',')
    
    for line in lines:
        words.append(str(line))

    ##words = ['mapas', 'casas', 'palas', 'paras', 'habas', 'balas', 'power', 'bolas']
    select = random.choice(words)
    
    ##secretNum = ''
    ##for i in range(NUM_DIGITS):
        ##secretNum += str(select)
    return select


def getClues(guess, secretNum):
    
    if guess == secretNum:
        return 'Congratulations! You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append(' - ' + chr(9632))
        elif guess[i] in secretNum:
            clues.append(' - ' + chr(9633))
        elif guess[i] not in secretNum:
            clues.append('- NA')
        
    ##if len(clues)== 0:
      ##  return 'Bagels '
    ##else:  
      ##  clues.sort()

    return ''.join(clues)

if __name__ == '__main__':
    main()




