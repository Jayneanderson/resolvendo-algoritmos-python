# Link do problema: https://www.hackerrank.com/challenges/bigger-is-greater/problem?
# Solução:
# transforme a string em um array de caracteres
# percorra o array de trás para frente e verifique:
#     se o caractere atual for maior do que o caractere anterior e a posição for maior 0, guarde este caracte (pivot) e a posição dele
#     senão, pule para a próxima iteração (use continue)
# declare uma variável para armazenar o menor valor que é maior em sequencia do que o pivot (se pivot é a, então o menor tem que ser b, ou c, d, o que for maior e venha depois do a)
# declare uma variável para pegar o index do menor caractere que é maior do que o pivot
# percorra da esquerda para a direita depois da posição do pivot
# verifique qual é o caractere menor depois do pivot, mas que é maior do que o pivot. Salve ele
# troque o pivot por este caractere menor da direira, mas que é maior do que o pivot
# ordene todos os elementos depois do pivot e salve em um array
# concatene os primeiros elementos até o pivor com o array ordenado
# dê um join para que tudo se torne string e retorne o array
# fora do laço for,  retorne 'no answer' se o array acabar


myStrings = []

def biggerIsGreater(w):
    #faça as duas validações: de tamanho da string e da quantidade de linhas (de size string já feita)
    array = list(w)
    numbersTemp = []
    pivot = ''
    pivotIndex = 0
    j = 0

    for i in reversed(range(len(array))):
        if (array[i] > array[i - 1] and i > 0):
            pivot = array[i - 1]
            pivotIndex = i - 1
        else:
            continue

        smallerNumber = 'zk'
        smallerIndex = 0
        j = i

        while (j < len(array)):
            if (array[j] < smallerNumber and array[j] > pivot):
                smallerNumber = array[j]
                smallerIndex = j
            
            j += 1
        array[pivotIndex] = smallerNumber
        array[smallerIndex] = pivot
        numbersTemp = sorted(array[i:len(array)])
        return "".join(array[0:i] + numbersTemp)
    return "no answer"


print(biggerIsGreater('bb'))
print(biggerIsGreater('lmno'))
print(biggerIsGreater('dcba'))
print(biggerIsGreater('dcbb'))
print(biggerIsGreater('abdc'))
print(biggerIsGreater('abcd'))
print(biggerIsGreater('fedcbabcd'))








