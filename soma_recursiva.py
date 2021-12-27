def soma(array):
    if len(array) == 1:
        return array[0]
    elif len(array)== 0:
        return 0
    else:
        return array[0]  + soma(array[1:]) ##1: significa que vai de 0 até o penultimo elemento

numerosPrimos =[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

print(soma(numerosPrimos))