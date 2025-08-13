# #Desafio 36:
# casa = float(input('Qual valor da casa: '))
# salario = float(input('Qual o valor do seu salario: '))
# anos = int(input('Em quantos anos pretende paga-lá: '))
# prestacao = salario * 0.30
# mensal = anos * 12
# parcelas = casa / mensal
# if parcelas <= prestacao:
#     print(f'As parcelas ficarao em {mensal}X de R${parcelas:.2f}, então o emprestimo foi aprovado pelo banco')
# else:
#     print(f'As parcelas ficariam em {mensal}X de R${parcelas:.2f}, seu emprestimo nao foi aprovado pelo banco pois o limite maximo foi escedido, que é 30% (R${prestacao})')


#DESAFIO 37: 
# import time
# numero = int(input('Escreva um numero: '))
# time.sleep(1.2)
# print(' '*20)
# print('1 [BINARIO]  2 [OCTAL]  3 [HEXADECIMAL]')
# time.sleep(1)
# print(' '*20)
# conversao = int(input('Escolha para qual base quer converte-lo: '))
# if conversao == 1:
#     bi = bin(numero)
#     print(f'Convertendo seu numero {numero} para BINARIO, ele vira: {bi}')
# elif conversao == 2:
#     oc = oct(numero)
#     print(f'Convertendo seu numero {numero} para OCTAL, ele vira: {oc}')
# elif conversao == 3:
#     he = hex(numero)
#     print(f'Convertendo seu numero {numero} para HEXADECIMAL, ele vira: {he}')
# else:
#     print('Numero não identificado! Tente novamente com uma das escolhas acima...')


#DESAFIO: 
# numero1 = int(input('Coloque um numero:  '))
# numero2 = int(input('Coloque outro: '))
# if numero1 > numero2: 
#     print(f'O primeiro numero é maior')
# elif numero2 > numero1: 
#     print('O segundo numero é maior.')
# else:
#     print('Nao existe numero maior, os dois sao iguais')


#DESAFIO:  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.    
from datetime import date

ano_atual = date.today().year
data_nasc = int(input('Coloque seu ano de nascimento: '))

idade = ano_atual - data_nasc
ano_alistamento = data_nasc + 18

if idade > 18:
    atraso = idade - 18
    print(f'Você precisa se alistar! Passou {atraso} ano(s) do prazo.')
elif idade == 18:
    print('Você precisa se alistar este ano!')
else:
    falta = 18 - idade
    print(f'Você ainda não precisa se alistar. Faltam {falta} ano(s).')
