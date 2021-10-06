# pilha de chanada by crystian araujo
def sauda(nome):
    print ("Olá"+nome+"!")
    sauda2(nome)
    print("Preparando para dar tchau!")
    tchau()
def sauda2(nome):
    print("Como vai "+nome+"?")
def tchau():
    print("Ok, bye bye")

sauda('Crystian')