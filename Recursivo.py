



def soma(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero + soma (numero - 1)
x = int(input('Digite um número para mostrar a sequência de Fibonacci: '))
res = soma(x)
print(f'A sequência de {x} é {res}: ')