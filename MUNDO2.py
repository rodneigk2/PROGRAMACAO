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


#DESAFIO 38:
# numero1 = int(input('Coloque um numero:  '))
# numero2 = int(input('Coloque outro: '))
# if numero1 > numero2:
#     print(f'O primeiro numero é maior')
# elif numero2 > numero1:
#     print('O segundo numero é maior.')
# else:
#     print('Nao existe numero maior, os dois sao iguais')


#DESAFIO 39:
# ano_atual = date.today().year
# data_nasc = int(input('Coloque seu ano de nascimento: '))
# idade = ano_atual - data_nasc
# ano_alistamento = data_nasc + 18
# if idade > 18:
#     atraso = idade - 18
#     print(f'Você precisa se alistar! Passou {atraso} ano(s) do prazo.')
# elif idade == 18:
#     print('Você precisa se alistar este ano!')
# else:
#     falta = 18 - idade
#     print(f'Você ainda não precisa se alistar. Faltam {falta} ano(s).')


#DESAFIO 40:
# nota1 = float(input('Coloque a nota: '))
# nota2 = float(input('Coloque a 2 nota: '))
# media = (nota1 + nota2) / 2
# if media >= 6:
#     print(f'Você tirou {media}, uma nota aceitavel, Parabens')
# else: print(f'Você tirou {media}, uma nota abaixo da media.')


#DESAFIO 41:
# from datetime import date
# ano_atual = date.today().year
# ano = int(input('Coloque seu ano de nascimento: '))
# data = ano_atual - ano
# idade = data
# match idade:
#     case i if i <= 9:
#         print(f'Você é da categoria mirin, por ter {idade} anos')
#     case i if i <= 14:
#         print(f'Você é da categoria infantil, por ter {idade} anos')
#     case i if i <= 19:
#         print(f'Você é da categoria junior, por ter {idade} anos')
#     case i if i <= 25:
#         print(f'Você é da categoria senior, por ter {idade} anos')
#     case _:
#         print(f'Você é da categoria master tem mais de 25 anos, idade: {idade} anos')


# DESAFIO 42:
# lado1 = float(input('Coloque o tamanho do primeiro lado: '))
# lado2 = float(input('Coloque o tamanho do segundo lado: '))
# lado3 = float(input('Coloque o tamanho do terceiro lado: '))
# match lado1, lado2, lado3:
#     case i, p, c if i > 0 and p > 0 and c > 0:
#         if i < p + c and p < i + c and c < i + p:
#             if i == p == c:
#                 print('Com essas medidas você consegue formar um TRIÂNGULO EQUILÁTERO')
#             elif i == p or p == c or c == i:
#                 print('Com essas medidas você consegue formar um TRIÂNGULO ISÓSCELES')
#             else:
#                 print('Com essas medidas você consegue formar um TRIÂNGULO ESCALENO')
#         else:
#             print('Com essas medidas você não consegue formar nenhum triângulo')
#     case _:
#         print('Lados inválidos. Todos devem ser maiores que zero.')


# DESAFIO 43:
# peso = float(input('Coloque seu peso: '))
# altura = float(input('Coloque sua altura: '))
# imc = peso / (altura ** 2)
# if imc <= 18.5:
#     print('Você esta abaixo do peso.')
# elif imc <= 25:
#     print('Você esta com o peso ideal.')
# elif imc <= 30:
#     print('Você esta com sobrepeso')
# elif imc <= 40:
#     print('Você está obeso')
# else:
#     print('Você está com obesidade morbida.')


# DESAFIO 44:
# produto = float(input('Coloque o valor a ser pago pelo produto: '))
# print(' ')
# escolha = int(input('Escolha a forma de pagamento: \n[1] à vista dinheiro/cheque: 10% de desconto  \n[2] à vista no cartão: 5% de desconto  \n[3] em até 2x no cartão: preço normal  \n[4] 3x ou mais no cartão: 20% de juros \n\nOpção: '))
# match escolha:
#     case 1:
#         desc1 = produto * 0.10
#         desconto1 = produto - desc1
#         print(f'Você escolheu a opção [1] (À VISTA/EM DINHEIRO/CHEQUE) \nE ganhou um desconto de R${desc1:.2f}, \nTotalizando valor do produto com desconto em: R${desconto1:.2f}')
#     case 2:
#         print(' ')
#         desc2 = produto * 0.05
#         desconto2 = produto - desc2
#         print(f'Você escolheu a opção [2] (À VISTA CARTÃO) \nE ganhou um desconto de R${desc2:.2f}, \nTotalizando valor do produto com desconto em: R${desconto2:.2f}')
#     case 3:
#         print(f'Você escolheu a opção 3 (ATÉ 2X NO CARTÃO), Valor a pagar R${produto:.2f}')
#     case 4:
#         acr = produto * 0.20
#         acrescimo = produto + acr
#         print(f'Você escolheu a opção 4 (3X OU MAIS NO CARTÃO) \nE teve um acrescimo de R${acr:.2f}, \nTotalizando valor do produto em R${acrescimo:.2f}')
#     case _:
#             print(f'Forma de pagamento não encontrada.')


#DESAFIO 45: Crie um programa que faça o computador jogar Jokenpô com você.
# from random import choice
# print(f'{"VAMOS JOGAR":=^30}')
# print(' ')
# jogar = int(input('Escolha uma das opções: [1] PEDRA  [2] PAPEL  [3] TESOURA: \n\nOpção: '))
# comp = [1, 2, 3]
# escolhac = choice(comp)
# if jogar == escolhac:
#     if escolhac == 1 and escolhac == jogar:
#         esc1 = 'PEDRA'
#         print(f'Vocês EMPATARAM, o computador JOGOU {esc1}')
#     elif escolhac == 2 and escolhac == jogar:
#         esc2 = 'PAPEL'
#         print(f'Vocês EMPATARAM, o computador JOGOU {esc2}')
#     elif escolhac == 3 and escolhac == jogar:
#         esc3 = 'TESOURA'
#         print(f'Vocês EMPATARAM, o computador JOGOU {esc3}')
#     else: print('Opcão não identificada, por favor coloque um numero valido.')
# elif escolhac == 1 and jogar == 2:
#     print('Você VENCEU, o computador JOGOU PEDRA')
# elif escolhac == 1 and jogar == 3:
#     print('Você PERDEU, o computador JOGOU PEDRA')
# elif escolhac == 2 and jogar == 1:
#     print('Você PERDEU, o computador JOGOU PAPEL')
# elif escolhac == 2 and jogar == 3:
#     print('Você VENCEU, o computador JOGOU PAPEL')
# elif escolhac == 3 and jogar == 1:
#     print('Você VENCEU, o computador JOGOU TESOURA')
# elif escolhac == 3 and jogar == 2:
#     print('Você PERDEU, o computador JOGOU TESOURA')
# else:
#     print('Opcão não identificada, por favor coloque um numero valido.')


# #DESAFIO 46:
# from time import sleep

# for c in range(10, 0, -1):
#     print(c)
#     sleep(1)
# print('KATCHAUUUUU')


# DESAFIO 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# for c in range(0,50):
#     if c % 2 == 0:
#         print(c)


#DESAFIO 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# for c in range(1, 501):
#     if c % 3 == 0:
#         print(c)


#DESAFIO 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# usuario = int(input('Coloque um numero para ver sua tabuada: '))
# tab = 0
# for c in range(1, 11):
#     tab += usuario
#     print(f'{usuario} X {c} = {tab}')


#DESAFIO 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# soma = 0
# cont = 0
# for c in range(6):
#     n = int(input('Coloque um numero para soma-los: '))
#     if n % 2 == 0:
#         soma += n
#         cont += 1
# print(f'Você digitou um total de {cont} numeros e a soma dos pares são de {soma}')


#DESAFIO 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# t = int(input('Coloque o termo para ver sua progressao: '))
# r = int(input('Coloque a razao: '))
# soma = 0
# soma += t
# print(soma)
# for c in range(9):
#     soma += r
#     print(soma)


#DESAFIO 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# n = int(input('Coloque um numero para verifica-lo: '))
# cont = 0
# for c in range(1, n+1):
#     if n % c == 0:
#         cont += 1
# if cont == 2:
#     print('Este numero é primo.')
# else: print('Esse numero não é primo.')


#DESAFIO 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
# palindromo = str(input('Coloque uma frase para verificar se é um palindromo: ')).lower()
# esp = palindromo.replace(" ", '')
# inv = esp[::-1]
# if esp == inv:
#     print(f'A frase {palindromo} que você colocou é um palindromo. {inv}')
# else:
#     print('Essa frase não é um palindromo.')


# DESAFIO 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# from datetime import date
# cont = 0
# cont2 = 0
# ano = date.today().year
# for c in range(1,4):
#     ano_nasc = int(input('Coloque seu ano de nascimento: '))
#     idade = ano - ano_nasc
#     if idade >= 18:
#         cont +=1
#     else:
#         cont2 += 1
# print(f'Das datas citadas acima {cont} são maiores de idade, e {cont2} são menores.')


#DESAFIO 55:  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# for c in range(1,6):
#     p = float(input(f'Coloque o peso da {c} pessoa: '))
#     if c == 1:
#         maior = p
#         menor = p
#     else:
#         if p > maior:
#             maior = p
#         else:
#             menor = p
# print(f'O maior peso é {maior}, e o menor é {menor} ')


#DESAFIO 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
# ida = 0
# cont = 0
# velho = 0
# nome_velho = ''
# for p in range(1,6):
#     nome = str(input('Coloque seu nome: '))
#     idade = int(input('Coloque sua idade: '))
#     sexo = str(input('Coloque seu sexo: ')).lower()
#     ida += idade
#     if p == 1:
#         velho = idade
#     else:
#          if idade > velho:
#             velho = idade
#             nome_velho = nome
#     if sexo[:1].lower() == 'f':
#         if idade < 20:
#             cont += 1
#     print('=' * 30)
# ida /= 5
# print(f'A média entre as idade é de {ida} e o mais velho entre todos é o {nome_velho} e tem {velho} anos e por ultimo temos {cont} mulheres com menos de 20 anos')


#DESAFIO 56:  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
# sexo = ''
# while sexo != 'm' and sexo != 'f':
#     sexo = input('Coloque seu sexo (m/f): ').lower()
#     if sexo != 'm' and sexo != 'f':
#             print('Coloque um sexo válido')
# print('FIM')


# DESAFIO 57: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(1,10)
jogador = 0
cont = 0
while jogador != computador:
    escolha = input('Escolha um numero: ').lower
    cont += 1
    if jogador != computador:
        escolha = input('Você errou, quer continuar: [S/N] ').lower
        if escolha == 'n':
            print(f'Você teve um total de {cont} tentativas.')
    else:
        print(f'Você GANHOU, com um total de {cont} tentativas.')
print('O jogo ACABOU')
print(computador)
