from ntpath import join
from posixpath import split
import string
from pandas import concat


myStrings = []

def biggerIsGreater(w):
    #faça as duas validações: de tamanho da string e da quantidade de linhas (de size string já feita)
    array = list(w)
    numbersTemp = []
    pivot = ''
    pivotIndex = 0
    j = 0
    result = 0

    for i in reversed(range(len(array))):
        if (array[i] > array[i - 1]):
            pivot = array[i - 1]
            pivotIndex = i - 1
        else:
            continue
        smallerNumber = 'z'
        smallerIndex = 0
        j = i

        while (j < len(array)):
            if (array[j] < smallerNumber and array[j] > pivot):
                smallerNumber = array[j]
                smallerIndex = j
            
            j += 1
        array[pivotIndex] = smallerNumber
        array[smallerIndex] = pivot
        slice_object = slice(i, len(array))
        numbersTemp = sorted(array[i:len(array)])
        return "".join(array[0:i] + numbersTemp)
    return "no answer"
        #numbersT'emp = array.slice(i, array.length).sort()

# - guarde a primeira string
# - guardar a primeira letra
# - ordenar as demais letras
# - pegar a última letra e mover para a penúltima posição
# - a string temporária é maior do que a string recebida?
#     se sim, retorne essa string
#     senão, mova o último caractere para a posição anterior
print(biggerIsGreater('dkhc'))