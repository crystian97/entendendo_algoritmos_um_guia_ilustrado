import random
from random import shuffle
# algoritmo quicksort
def qsort(lista):
    # verifica se a lista é de um unico elemento ou vazia
    if len(lista) <2:
        return lista
    else:
        # escolhemos o elemento pivo para se basear a ordenação de forma aleatória
        pivo = lista[0];
        # separar a lista em duas , uma contando os elemtentos menores que o pivo e outra com os maiores
        menores = [ i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
    # aqui retornamos o array ordenado
    return qsort(menores) + [pivo] + qsort(maiores)
numeros_aleatorios_ate_50 = [ i for i in range(50)]
# bagunçando os numeros
shuffle(numeros_aleatorios_ate_50)

print(numeros_aleatorios_ate_50)
print(qsort(numeros_aleatorios_ate_50))
