def isWordGuessed(secretWord, lettersGuessed):
    x=True
    for let in secretWord:
        if let not in lettersGuessed:
          x=False
    return x