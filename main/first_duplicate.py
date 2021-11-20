#Esse algoritmo é para encontrar o número que se repete primeiro. No caso, se houver mais de uma repetição o retornado será o que aparecer primeiro
#Solução: ler o array e colocar todos os valores em um novo vetor até que um repetido apareça. O primeiro repetido que aparecer será nosso valor procurado
def firstDuplicate(vetor):
    elements = []
    indice = 0
    for i in vetor:
        if(i in elements): 
            return vetor[indice]
        elements.append(vetor[indice])
        indice = indice + 1

    return -1

print(firstDuplicate([2,1,3,5,2,3]))