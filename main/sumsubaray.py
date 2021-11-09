#Somar um subarray contínuo para capturar o index dos elementos

def currentSum(vector, number):
    sum = 0
    start = 0
    end = 0
    for i in vector:
        # primeiro eu somo o valor do ponteiro final na variável soma
        sum = sum + vector[end]
        # daí eu pergunto: soma é maior que o número digitado e o ponteiro inicial é menor que o ponteiro final?
        # a 1ª vez dará falsa porque não há soma, a não ser que o primeiro valor já seja maior
        while sum > number and start < end: 
            # quando for maior, eu decremento o valor do ponteiro inicial
            # sempre que eu volto é porque a soma for maior do que o número de entrada
            sum = sum - vector[start]
            start = start + 1
        
        # a soma atual é igual ao número digitado no início?
        if sum == number:
            print(f'início {start} e final {end}')
            return True

        end = end + 1

    return False

items = [4,2,3,7,2,4,2]
items2 = [7,2,4,4,2,3,2]

print(currentSum(items2, 13))