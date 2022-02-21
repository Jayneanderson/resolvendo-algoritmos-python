# Link: https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# Resolvendo o algoritmo:
#     - Remova os espaços da string
#     - Conte a quantidade de caracteres e guarde em uma variável
#     - Tire a raiz quadrada do tamanho total da string
#     - Arredonde o valor da raiz para baixo e coloque em uma variável (será a linha)
#     - Arredonde o valor da raiz para cima e coloque em outra variável (será coluna)
#     - A multiplicação da linha pela coluna precisa ser maior que o tamanho da string, então verifique:
#       Se a multiplicação for menor que o tamanho da string, some + 1 na linha
#     - Crie uma variável para ter controle ao percorrer a string (k)
#     - Crie um array de uma dimensão para colocar todos os caracteres de uma vez após cada ciclo do for interno
#     - Faça um for para percorrer a linha (for i in range(row))
#     - Crie um array temporário que será zerado a cada ciclo do for linha (arrayTemp = [])
#     - Faça um for para percorrer a coluna (for i in range(col))
#     - Verifique k (variável de controle da string) é menor do que o tamanho da string:
#       Se sim, acrescente uma letra da string (na posição k) no array temporário (arrayTemp.append(sentenceNoSpace[k]))
#       Senão, acrescente um caractere em branco (arrayTemp.apprend('')). Isso serve para quando acabar a string e ainda tiver espaços para percorrer, evitando erro "fora do range" 
#     - Some mais um na variável de controle da string (k)
#     - Pegue o array criado antes de entrar nos dois laços (array) e acrescente o conteúdo do arrayTemp no for de fora
#     - Agora vamos inverter a lógica para pegar as colunas
#     - Crie um for para percorrer a coluna
#     - Crie um array temporário
#     - Faça um for para percorrer a linha
#     - Acrescente no array temporário o array com elementos na posição i e j (arrayTemp.append(array[i][j])). Note que aqui pega os elementos da coluna e coloca no array
#     - Agora pegue um array novo criado antes de entrar nos dois laços e coloque o conteúdo do array temporário no array permanente (encryptedeArray.append(arrayTemp)
#     - Dê um join para juntar tudo e retorne o array.

#Difuldades
#     - Tive muita dificuldade em manipular matrizes com numpy
#     - Demorei para entender que não posso usar array[i][j] sem antes ter as interado com as dimensões necessárias
#     - Inicialmente eu interpretei errado achando que quando tinha uma raiz perfeita não precisa somais mais um na linha

import math as mt

 
def encryptation(s):
    
    #"if man was meant to stay on the ground god would have given us roots"
    sentenceNoSpace = s.replace(" ", "")
    size = len(sentenceNoSpace)
    resultSquare = mt.sqrt(size)
    row = mt.floor(resultSquare)
    col = mt.ceil(resultSquare)

    if(row * col < size):
        row = row + 1

    k = 0
    array = []

    for i in range(row):
        arrayTemp = []
        for j in range(col):
            print
            if(k < size):
                arrayTemp.append(sentenceNoSpace[k])
            else:
                arrayTemp.append('')
            k += 1
        print(arrayTemp)
        array.append(arrayTemp)

    print(array)

    print("Vamos inverter agora")
    encryptedArray = []

    for j in range(col):
        arrayTemp = []
        for i in range(row):
            arrayTemp.append(array[i][j])
        encryptedArray.append("".join(arrayTemp))

    return " ".join(encryptedArray)


print(encryptation("haveaniceday"))