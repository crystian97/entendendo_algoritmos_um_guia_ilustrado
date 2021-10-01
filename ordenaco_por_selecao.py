numeros_primos = [3,1,25,11,13,17]

def busca_menor(arr):
    menor = arr[0] #armazena menor valor
    menor_indice=0 #armazena o indice do menor valor
    for i in range(1,len(arr)):
        if arr[i]<menor:
            menor=arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):# função para ordenação de um array
    novoArr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)#Encontra o menor elemento do array e adiciona ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr
print (ordenacaoporSelecao(numeros_primos))