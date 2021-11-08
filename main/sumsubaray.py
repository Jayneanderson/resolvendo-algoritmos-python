#Somar um subarray contínuo para capturar o index dos elementos
sum = 0
start = 0
end = 0

def sum(vector, s):
    for i in vector:
        sum = sum + vector[end]

        while sum > s and start < end:
            sum = sum - v[start]
        
        if sum == s:
            print(start + 1, end+1)
            return True

    return False

