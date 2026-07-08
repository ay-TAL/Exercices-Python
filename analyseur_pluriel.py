exceptions = {"souris": "singulier", "bus": "singulier", "choix": "singulier", "prix": "singulier"}

termine = ('s','x') 

def mots(word):
 
 word = word.lower()
 
 if word in exceptions:
   return('ce mot est au singulier')
 else:
    if word.endswith(termine):
     return('ce mot est au pluriel')
    else:
     return('ce mot est au singulier')
  
resultat = mots(input('quelle est le mot: '))

print(resultat)
