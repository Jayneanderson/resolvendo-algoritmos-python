def firstDuplicate(vetor):
    elements = []

    for i in vetor:
        if(i in elements):
            return vetor[i]
        elements.append(vetor[i])

    return -1