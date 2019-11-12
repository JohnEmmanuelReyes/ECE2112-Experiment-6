def getWordGuessed(secretWord, lettersGuessed):
  w=secretWord
  if w.isalpha()==True:
      for letter in secretWord:
            if letter not in lettersGuessed:
              w=w.replace(letter,"_ ")
      return w
  else:
      print("INVALID!!:Input only letters")