# Gerar números da sequencia de fibonnaci até que seja gerado um número maior que o numero da entrada

numero_entrada = int(input("Insira um número inteiro: "))


def sequencia_fibonnaci(valor):
    fibonnaci = [0, 1]
    count = 0
    while fibonnaci[-1] < valor:
        fibonnaci.append(fibonnaci[count] + fibonnaci[count + 1])
        count += 1
    return fibonnaci


def esta_em_fibonnaci():
    gerador_fibonnaci = sequencia_fibonnaci(numero_entrada)
    print(gerador_fibonnaci)
    if numero_entrada in gerador_fibonnaci:
        print(f"\nO valor {numero_entrada} pertence a sequencia de fibonnaci;"
              f"\nAparecendo no índice {gerador_fibonnaci.index(numero_entrada)};")
    else:
        print(f"\nO Valor {numero_entrada} não pertence a sequencia de fibonnaci;")


esta_em_fibonnaci()
