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
# from random import randint
# computador = randint(1,10)
# cont = 1
# jogador = int(input('Tente adivinhar o numero que o computador pensou, entre 1 a 10: '))
# while jogador != computador:
#     print(f'Você errou!')
#     resposta = input('Tentar novamente: [S/N] ').lower()
#     if resposta == 'n':
#         print(f'Você teve um total de {cont} tentativas')
#         break
#     elif resposta == 's':
#         jogador = int(input('Tente adivinhar novamente: '))
#         cont += 1
#     else: print('Coloque uma opção valida')
# else: 
#     print(f'Você ganhou! Com um total de {cont} tentativas')
# print('O jogo acabou.')


#DESAFIO 59: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
# primeiro = int(input('Coloque o primeiro numero: '))
# segundo = int(input('Coloque o segundo numero: '))
# escolha = 0
# print('=' * 30)
# print(' [1] SOMAR VALORES \n [2] MULTIPLICAR VALORES \n [3] MOSTRAR MAIOR VALOR \n [4] ESCOLHER NOVOS NUMEROS \n [5] SAIR DO PROGRAMA')
# while escolha != 5:
#     print('=' * 30)
#     escolha = int(input('Coloque a opção desejada: '))
#     if escolha == 1:
#         soma = primeiro + segundo
#         print(f'A opção selecionada foi a de SOMA, o resultado é {soma}')
#         print(' [1] SOMAR VALORES \n [2] MULTIPLICAR VALORES \n [3] MOSTRAR MAIOR VALOR \n [4] ESCOLHER NOVOS NUMEROS \n [5] SAIR DO PROGRAMA')
#         print(' ')
#     elif escolha == 2:
#          multiplicacao = primeiro * segundo
#          print(f'A opção selecionada foi a de MULTIPLICAÇÃO, o resultado é {multiplicacao}')
#          print('=' * 30)
#          print(' [1] SOMAR VALORES \n [2] MULTIPLICAR VALORES \n [3] MOSTRAR MAIOR VALOR \n [4] ESCOLHER NOVOS NUMEROS \n [5] SAIR DO PROGRAMA')
#          print(' ')
#     elif escolha == 3: 
#          if primeiro > segundo:
#               maior = primeiro
#          else:
#               maior = segundo
#               print(maior)
#          print(f'A opção selecionada foi a de MOSTRAR O MAIOR, o resultado é {maior}')
#          print('=' * 30)
#          print(' [1] SOMAR VALORES \n [2] MULTIPLICAR VALORES \n [3] MOSTRAR MAIOR VALOR \n [4] ESCOLHER NOVOS NUMEROS \n [5] SAIR DO PROGRAMA')
#          print(' ')
#     elif escolha == 4:
#           print('=' * 30)
#           primeiro = int(input('Coloque o primeiro numero: '))
#           segundo = int(input('Coloque o segundo numero: '))
#           continue
#     elif escolha == 5:
#          print('PROGRAMA FINALIZADO')


#DESAFIO 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# numero = int(input('Coloque um numero para ver seu fatorial: '))
# mult = 1
# for c in range(1,numero+1):
#     mult *= c
#     print(f'{numero} X {c} = {mult}')


#DESAFIO 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# numero = int(input('Coloque um numero para ver sua razão: '))
# razao = int(input('Coloque a razão: '))
# c = 0
# print(f'{numero}')
# while c != 9:
#     c += 1
#     numero += razao 
#     print(f'{numero}')
# print('FIM')


#DESAFIO 62:  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

# numero = int(input('Coloque o primeiro termo: '))
# razao = int(input('Coloque a razão: '))

# c = 0              # contador de termos mostrados
# total = 10         # começa mostrando 10 termos
# mais = 1           # só pra entrar no loop
# while mais != 0:
#     while c < total:   # mostra os termos até o limite atual
#         print(numero, end=' ')
#         numero += razao
#         c += 1
#     print()  # quebra de linha
#     mais = int(input('Quer ver mais quantos termos? '))
#     total += mais   # soma ao total de termos
# print('FIM')


#DESAFIO 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
# n = int(input('Coloque um numero para ver a sua sequencia: '))
# primeiro = 0
# segundo = 1
# c = 0
# print(primeiro, segundo,  end=' ')
# while c < n-2:
#     proximo = segundo + primeiro
#     print(proximo, end=' ')
#     primeiro = segundo
#     segundo = proximo
#     c += 1


#DESAFIO 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# n = 0
# cont = 0
# soma = 0
# while n != 999:
#     n = int(input('Coloque um numero: ')) 
#     cont += 1
#     soma += n
#     if n == 999:
#         soma -= 999
# print(soma)
# print(cont-1)
 

#DESAFIO 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# media = 0 
# continuar = ''
# maior = 0
# menor = 0
# cont = 0

# while continuar != 'n':
#     n = int(input('Coloque um numero: '))
#     media += n
#     cont += 1
#     if n == 1:
#         maior = n
#         menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
#     continuar = input('Quer continuar [S/N]: ').lower()
#     if continuar != 's' and 'n':
#         print('Coloque uma opção valida.')
# print(f'A média entre os numeros foi de {media/cont}')
# print(f'O maior numero foi {maior} e o menor foi {menor}')
# print('Fim do programa!')


#DESAFIO 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
# n = 0 
# soma = 0
# cont = 0
# while True:
#     n = int(input('Coloque um numero: '))
#     if n == 999:
#         break
#     cont += 1
#     soma += n
# print(f'A soma dos numeros digitados acima é de {soma} e foram digitados {cont} numeros')
# print('Fim do programa')


#DESAFIO 67:  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# while True:
#     tabuada = int(input('Coloque um numero para ver sua tabuada: '))
#     if tabuada < 0:
#         break
#     for c in range(1, 11):
#         print(f'{tabuada} X {c} = {tabuada * c}')
# print('FIM')


#DESAFIO 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# from random import randint
# from time import sleep
# print('=' * 30)
# print('VAMOS JOGAR PAR OU IMPAR')
# print('=' * 30)
# cont = 0
# while True:
#     computador = randint(1,10)
#     escolha_jogador = input('PAR ou IMPAR: ').upper().strip()
#     if escolha_jogador != 'PAR' and escolha_jogador != 'IMPAR':
#         print('Coloque uma opção valida')
#         print('=' * 30)
#         continue
#     jogador = int(input('Coloque um numero: '))
#     soma = jogador + computador
#     resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'
#     print('=' * 30)
#     if escolha_jogador == resultado:
#         sleep(1)
#         print(f'Você ganhou!: {computador} [COMPUTADOR] + {jogador} [JOGADOR] = {soma} [{resultado}]')
#         print('=' * 30)
#         cont += 1
#         sleep(1)
#         if cont == 1: print(f'Você tem {cont} vitoria')
#         else: print(f'Você tem {cont} vitorias consecutivas')
#         print('=' * 30)
#         sleep(0.5)
#         print('Vamos jogar novamente!')
#     else:
#         sleep(1)
#         print(f'Você perdeu.: {computador} [COMPUTADOR] + {jogador} [JOGADOR] = {soma} [{resultado}]')
#         break
# print('=' * 30)
# sleep(1)
# print('FIM DE JOGO')
# if cont > 1:
#     print(f'Você ganhou {cont} vezes consecutivas')
# elif cont == 1:
#     print('Você ganhou apenas uma vez')
# else:
#     print('Você não ganhou nenhuma vez')
# print('=' * 30)


#DESAFIO 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

cont = 0
contador_masculino = 0
contador_feminino = 0 

while True: 
    idade = int(input('Coloque sua idade: '))
    sexo = input(f'Coloque seu sexo: ').upper().strip()[0]
    if idade > 18:
        cont += 1
    if sexo == 'M':
        contador_masculino += 1
    if sexo == 'F' and idade < 20:
        contador_feminino += 1
    escolha = input('Quer continuar: ')
    if escolha == 'N':
        break
    elif escolha == 'S':
        continue
    else:
        print('Coloque uma opção valida')

print(f'Foram cadastradas {cont} pessoas com mais de 18 anos')
print(f'Foram cadastrados {contador_masculino} homens')
print(f'Foram cadastradas {contador_feminino} mulheres com menos de 20 anos')