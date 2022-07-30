#Escrever uma frase de trás para frente

frase_input = input("Escreva uma frase bonita para ve-la ao contrario: ")

for l in range(len(frase_input), 0, -1):
    print(frase_input[l-1])