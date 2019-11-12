import string
def getAvailableLetters(lettersGuessed):
   lg=[sl.lower() for sl in lettersGuessed]
   lc = string.ascii_lowercase
   for b in string.ascii_lowercase:
        if b in str(lg):
            lc = lc.replace(b,'')            
   return lc