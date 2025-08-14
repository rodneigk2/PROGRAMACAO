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
# angulo1 = str(input('Coloque "-" para formar um triangulo: '))
# angulo2 = str(input('Coloque "-" para formar um triangulo: '))
# angulo3 = str(input('Coloque "-" para formar um triangulo: '))
# ag1 = len(angulo1)
# ag2 = len(angulo2)
# ag3 = len(angulo3)
# match(ag1, ag2, ag3):
#     case (i, p, c) if i > 0 and p > 0 and c > 0:
#         if i == p == c:
#             print('Com essas medidas você consegue formar um TRIANGULO EQUILATERO')
#         elif i == p or p == c or c == i:
#             print('Com essas medidas você consegue formar um TRIANGULO ISÓSCELES')
#         else:
#             print('Com essas medidas você consegue formar um TRIANGULO ESCALENO')
#     case _:
#         print('Com essas medidas você não consegue formar nenhum tipo de trângulo')


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


# DESAFIO: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço normal – 3x ou mais no cartão: 20% de juros

produto = float(input('Coloque o valor a ser pago pelo produto: '))
escolha = int(input('Escolha a forma de pagamento: [1] à vista dinheiro/cheque: 10% de desconto  [2] à vista no cartão: 5% de desconto  [3] em até 2x no cartão: preço normal  [4] 3x ou mais no cartão: 20% de juros:  '))
match escolha:
    case i if i == 1:
        desc1 = produto * 10
        desconto1 = produto - desc1
        print(f'Você escolheu a opção 1 (À VISTA/EM DINHEIRO/CHEQUE), ganhou um desconto de R${desc1:.2f}, totalizando valor do produto com desconto em: R${desconto1:.2f}')

        if i == 2:
            desc2 = produto * 0.05
            desconto2 = produto - desc2
            print(f'Você escolheu a opção 2 (À VISTA NO CARTÃO), ganhou um desconto de ')

        elif i == 3: 
            print(f'Você escolheu a opção 3 (2X no cartão)')

        elif i == 4:
            print(f'Você escolhei a opção 4 (3X ou mais no cartão)')

        else:
            print(f'Forma de pagamento não encontrada.')