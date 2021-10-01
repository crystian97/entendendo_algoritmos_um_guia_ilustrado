# neste exemplo utilizamos um array com uma função com o intuito de encontrar o item buscado na função pesquisa_binaria
# lembrando que uma pesquisa binária é uma técnica que percorre uma lista ordenada sempre eleminando metade dos elementos
# até se chegar no resultado
def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = round((baixo + alto) / 2)
        # sempre o chute vai ser no elemento central da lista
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            # se o chute for maior que o item define o alto como o meio -1 eliminando metade da lista
            alto = meio - 1
        else:
            baixo = meio +1
    return None

minha_lista = [1, 3, 5, 7, 9]

# print(pesquisa_binaria(minha_lista,3))
print(pesquisa_binaria(minha_lista,10))
