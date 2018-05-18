operacao = input ('Se você deseja somar, digite (soma). Se você deseja multiplicar, digite (multiplica)')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

if operacao == 'soma':
    print(n1 + n2)
elif operacao == 'multiplica':
    print(n1 * n2)


