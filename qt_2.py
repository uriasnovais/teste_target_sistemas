# Gerar números da sequencia de fibonnaci até que seja gerado um número maior que o numero da entrada


def sequencia_fibonnaci(fim):
    fibonnaci = [0, 1]
    count = 0
    while count < fim:
        fibonnaci.append(fibonnaci[count]+fibonnaci[count+1])
        count += 1
    return fibonnaci

gerador_fibonnaci = sequencia_fibonnaci(10)
print(gerador_fibonnaci)

while True:
    while numero_entrada < fibonnaci[-1]:
        fibonnaci.append()

