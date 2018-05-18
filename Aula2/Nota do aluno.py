frequencia = int(input('Digite a frequencia do aluno: \n'))
if frequencia <= 75:
    print ('Reprovado!')
if frequencia >= 75:

    print ('Digite a média do aluno: \n')
media = int(input('Digite a média do aluno: \n'))
if media >= 7:
    print ('Aprovado!')
elif media < 3:
    print ('Reprovado!')
elif media > 3 and media < 7:
    print ('Prova final!')

prova_final = int(input('Digite a media final: \n'))

if (prova_final + media)/2 >= 5:
    print ('Aprovado na final!')
elif (prova_final + media)/2 <= 5:
    print ('Reprovado na final!')



