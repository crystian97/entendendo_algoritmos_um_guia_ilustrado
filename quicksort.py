# algoritmo quicksort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    # aqui pegamos o primeiro elemento da lista e colocamos em um pivo
    # depois dividimos a lista em duas partes, uma com os elementos menores que o pivo e outra com os maiores
    # e ao final retornamos a junção das duas partes
    menores = [x for x in lista[1:] if x <= pivo]# [1:]] percorrer do primeiro até o ultimo elemento do array
    maiores = [x for x in lista[1:] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)
primos_ate_50 =[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(quick_sort(primos_ate_50))

