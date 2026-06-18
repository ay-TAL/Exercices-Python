def analyseur_de_phrase(phrase):
    sentence = phrase.lower()
    li = sentence.split()
    Total = len(li)
    print('nombre total de mot est:',Total)

    lenth = []
    
    for mot in li:
        if len(mot) >= 4: 
          lenth.append(mot)
            
        
    return lenth

pha = analyseur_de_phrase(input('inserer la phrase: '))

print("les mot de plus de 4 lettre sont:",pha)
       