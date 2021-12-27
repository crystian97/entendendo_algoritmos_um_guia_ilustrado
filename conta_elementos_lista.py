def contaElementosLista(lista):
    if(lista):
        return 1 + contaElementosLista(lista[1:])
    else:
        return 0

NumeroReais=[1,2,3]
print(contaElementosLista(NumeroReais))