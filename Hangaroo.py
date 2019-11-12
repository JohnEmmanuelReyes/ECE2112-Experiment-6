def isWordGuessed(secretWord, lettersGuessed):
    x=True
    for let in secretWord:
        if let not in lettersGuessed:
          x=False
    return x

def getWordGuessed(secretWord, lettersGuessed):
  w=secretWord
  if w.isalpha()==True:
      for letter in secretWord:
            if letter not in lettersGuessed:
              w=w.replace(letter,"_ ")
      return w
  else:
      print("INVALID!!:Input only letters")
      
import string
def getAvailableLetters(lettersGuessed):
   lg=[sl.lower() for sl in lettersGuessed]
   lc = string.ascii_lowercase
   for b in string.ascii_lowercase:
        if b in str(lg):
            lc = lc.replace(b,'')            
   return lc

def Hangaroo(secretWord):
    secretWord = secretWord.lower()  
    lettersGuessed = ['']
    wrong = 0
    print('LET"S PLAY HANGAROO')
    print('Instruction:Guess the missing letter to solve the word.')
    print('!!!!KEEP THE KANGAROO ALIVE!!!!')
    while not isWordGuessed(secretWord, lettersGuessed):
        print('\n Wrong Letter: ', wrong,'\n Missing letters: \n', getWordGuessed(secretWord, lettersGuessed))
        guess = input('Guess the word, insert letter: ')
        guessInLowerCase = guess.lower()
        if guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            if guessInLowerCase not in secretWord:
                wrong += 1
                if wrong == 4:
                    return print('YOU FAILED, TRY AGAIN')
        else:
            print('You already guessed that letter. Try again!')
    return print('Secret Word:', getWordGuessed(secretWord, lettersGuessed),'   YOU WIN!')