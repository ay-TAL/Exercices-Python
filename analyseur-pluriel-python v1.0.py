exceptions = {"souris": "singulier", "bus": "singulier", "choix": "singulier", "prix": "singulier"}

termine = ('s','x') 

def mots(word):
 if word in exceptions:
   return('ce mot est au singulier')
 else:
    if word.endswith(ter):
     return('ce mot est au pluriel')
    else:
     return('ce mot est au singulier')
  
res = mots(input('quelle est le mot: '))

print(res)
