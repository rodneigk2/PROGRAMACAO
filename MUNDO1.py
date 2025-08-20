#Desafio Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado
# nome = input("seu nome: ")
# print(f"Boas vindas, {nome}")


#Desafio Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada dia mês e ano
#dia = input("dia: ")
#mês = input("mês: ")
#ano = input("ano: ")
#print("Você nasceu no dia", dia, "de", mês, "de", ano)


#Desafio Faca um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas informacoes possiveis sobre ele.
# coisa = input('Coloque algo: ')
# print(type(coisa), coisa.isalnum(), coisa.isalpha(), coisa.isascii(), coisa.isdecimal(), coisa.isdigit(), coisa.isidentifier(), coisa.islower(), coisa.isnumeric(), coisa.isspace(), coisa.isupper(), coisa.istitle())


#Desafio, faca um programam que leia um numero inteiro e mostre seu antecessor e seu sucessor.
# n1 = int(input('Coloque seu numero: '))
# soma = n1 + 1
# subt = n1 - 1
# print(f'O antecessor do numero {n1} é o {subt} e o sucessor é {soma}')


#Desafio, crie um algoritimo que leia seu numero e mostre o seu dobro, triplo e raiz.
# n = int(input('Coloque um numero: '))
# dobro = n * 2
# triplo = n * 3
# raiz = n ** (1/2)
# print(f'O dobro do seu numero é {dobro}, triplo é {triplo}, e a raiz é {raiz}')


#Desafio, desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
# nota1 = float(input('Coloque sua nota do primeiro bimestre: '))
# nota2 = float(input('Coloque a do segundo: '))
# media = (nota1+nota2) / 2
# print(f'A sua media entre os bimestres é de {media}')


#Desafio, escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
# metros = int(input('Coloque quantos mestros você quer converter: '))
# cm = metros * 100
# mm = metros * 1000
# print(f'Os {metros}MTS acima convertidos em cm são: {cm}cms e em mm são {mm}mms.')

#Desafio, faca um programa que leia um numero inteiro qualquer e mostra na tela sua tabuada.
# tabuada = int(input('Coloque um numero: '))
# n1 = tabuada * 1
# n2 = tabuada * 2
# n3 = tabuada * 3
# n4 = tabuada * 4
# n5 = tabuada * 5
# n6 = tabuada * 6
# n7 = tabuada * 7
# n8 = tabuada * 8
# n9 = tabuada * 9
# n10 = tabuada * 10
# print(f'A tabuada do numero {tabuada} é:\n1 x {tabuada} = {n1}\n2 x {tabuada} = {n2}\n3 x {tabuada} = {n3}\n4 x {tabuada} = {n4}\n5 x {tabuada} = {n5}\n6 x {tabuada} = {n6}\n7 x {tabuada} = {n7}\n8 x {tabuada} = {n8}\n9 x {tabuada} = {n9}\n10 x {tabuada} = {n10}')


#Desafio 10, Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar, considere: US 1,00 = R$ 5,45
# dinheiro = float(input('Quantos R$ você tem?\nR$ '))
# dolar = dinheiro / 5.45
# print(f'Com R$ {dinheiro:.2f} você consegue comprar USD {dolar:.2f}')


#Desafio, faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que para cada litro de tinta, pinta uma area de 2MTS quadrados.
# largura = float(input('Coloque a largura:'))
# altura = float(input('Coloque a altura: '))
# area = largura * altura
# tinta = area / 2
# print(f'A parede tem uma area de {area}MTS e é necessario {tinta}L de tinta para cobri-la inteira.')


#Desafio, faca um algoritimo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.
# produto = int(input('Coloque o valor do produto: '))
# desconto = produto * 0.05
# valor = produto - desconto
# print(f'O valor de {produto} com o desconto de 5% fica em {valor}')


#Desafio, faca um algoritimo que leia o salario de um funcionario e mosre seu novo salario, com 15% de aumento
# salario = int(input('Coloque o seu salario mequetrefe aqui: '))
# valor = salario + (salario * 0.15)
# print(f'O valor do seu salario com o aumento é de {valor}')


#Desafio, escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# celsius = float(input('Coloque quantos graus está fazendo: '))
# fahrenheit  = 32 + (celsius * 1.8)
# print(f'Se esta fazendo {celsius} graus, nos USA está fazendo {fahrenheit:.1f} fahrenheit.')


# Desafio: escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# carro = float(input('Coloque quantos km rodados: '))
# dia = int(input('Coloque quantos dias você alugou o carro: '))
# km = 0.15 * carro
# aluguel = 60 * dia
# total = km + aluguel
# print(f'Você pagará R${aluguel} de aluguel pelos dias, e R${km} pelos km rodados \ntotal da conta fica em {total}')


# # Desafio: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira:
# numero = float(input('Coloque um numero: '))
# arredondar = int(numero)
# print(f'O seu numero arredondado para inteiro é {arredondar}.')


# Desafio: Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
# import math
# oposto = float(input('Coloque o comprimento do cateto oposto: '))
# adjacente = float(input('Coloque o comprimento do cateto adjacente: '))
# potencia = oposto ** 2 + adjacente ** 2
# raiz = math.sqrt(potencia)
# print(f'A hipotenusa dos comprimentos acima é {raiz}')


# Desafio: Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
# import math
# angulo = float(input('Coloque um angulo para convertelos: '))
# radiano = math.radians(angulo)
# seno = math.sin(radiano)
# coss = math.cos(radiano)
# tan = math.tan(radiano)
# print(f'O seno é {seno:.4f}, cosseno {coss:.4f}, tangente {tan:.4f}')


# Desafio: Um professor que sortear um dos seus quatro alunos para apagar o quadro. faca um programam que ajude ele, escrevendo e lendo o nome do escolhido.
# import random
# aluno1 = 'GABRIEL'
# aluno2 = 'RODNEI'
# c
# sorteio = aluno1, aluno2, aluno3
# choise = random.choice(sorteio)
# print(f'O aluno escolhido aleatoriamente foi: {choise}')


# Desafio: O mesmo professor anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia e mostre a ordem sorteada.
# import random
# aluno1 = 'GABRIEL'
# aluno2 = 'RODNEI'
# aluno3 = 'FOFAO'
# sorteio = [aluno1, aluno2, aluno3]
# random.shuffle(sorteio)
# print(f'{sorteio}')


# #Desafio: Faca um programa em python que abra e reproduza o audio de um arquivo MP3.
# import pygame
# pygame.init()
# pygame.mixer.init()
# musica = input()
# pygame.mixer.music.load('Michel jaquison.mp3')
# pygame.mixer.music.play()
# input('Clique ENTER para parar a musica.')
# pygame.mixer.music.stop() 


#Desafio 28: Escreva um programa que faca o computador 'pensar' em um numero inteiro entre 0 e 5 e peca para o usuario descobrir qual foi o numero escolhido pelo computador. O programa devera dizer na tela se o usuario venceu ou perdeu.
# import random
# numero = random.randint(1,10)
# jogador = int(input('Tente adivinhar o numero: '))
# if jogador == numero:
#     print(f'Parabens, você acertou o numero {numero}!')
# else:
#     print('Você errou.')


#Desafio: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h. Mostre um mensagem dizendo que ele foi multado. A multa vai custar R$7,00 para cada km acima do limite.
# velocidade = int(input('Coloque a velocidade que o carro estava: '))
# limite = 80
# valor = (velocidade - 80) * 7
# if velocidade > limite:
#     print(f'Você estava acima do limite de velocidade, sua multa será de R${valor}')
# else: print('Você passou batido dessa vez meu chapa')


#Desafio: Crie um programa que leia um numero na tela e diga se ele é impar ou par.
# numero = int(input('Coloque um numero e teste se e par ou impar: '))
# if numero % 2 == 0:
#     print(f'Seu numero {numero} é par.')
# else: print('Seu numero é impar.')


#Desafio: Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preco da passagem. Cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. 
# viagem = int(input('Quantos km você viajou: '))
# if viagem <= 200:
#     valor1 = 0.50 * viagem
#     print(f'O valor total da sua viagem ficou em R$ {valor1}')
# else:  
#     valor2 = 0.45 * viagem 
#     print(f'O valor total da sua viagem ficou em R$ {valor2}')


# Desafio: faca um programa que leia um ano qualquer e mostre se ele é bissexto.
# ano = int(input('Coloque um ano para verifica-lo: '))
# if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#     print('Seu ano é Bissexto!')
# elif ano % 100 == 0 and ano % 400 != 0: 
#     print('Seu ano nao é bissexto')
# else:
#     print('Seu ano nao é bissexto')


#Desafio: Faca um programa que leia tres numeros e mostre qual o menor e qual o maior.
# numero1 = int(input('Coloque um numero: '))
# numero2 = int(input('Coloque outro numero: '))
# numero3 = int(input('Coloque outro: '))
# lista = [numero1, numero2, numero3]
# om = max(lista)
# on = min(lista)
# print(f'O maior entre é {om}')
# print(f'O menor é {on}')


#Desafio: Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$1.250,00, calcule um aumento 10%. Para os inferiores ou iguais o aumento é de 15$.
# salario = float(input('Coloque o valor do seu salario aqui:'))
# if salario > 1250.00: 
#     aumento = salario * 0.10 + salario
#     valor = salario * 0.10
#     print(f'O seu salario aumentou para {aumento:.2f} subiu um valor de {valor:.2f}') 
# else: 
#     aumento2 = salario * 0.15 + salario
#     valorm = salario * 0.15
#     print(f'O valor do seu salario aumentou para {aumento2:.2f} teve um acrescimo de {valorm:.2f}')


#Desafio: Desenvolva um programa que leia o comprimento de tres restas e diga ao usuario se elas podem ou nao formar um triagulo. 
# angulo1 = input('Preencha com tracos para ver se forma um triangulo: ')
# angulo2 = input('Preencha com tracos para ver se forma um triangulo: ')
# angulo3 = input('Preencha com tracos para ver se forma um triangulo: ')
# a1 = len(angulo1)
# a2 = len(angulo2)
# a3 = len(angulo3)

# if a1 > 0 and a2 > 0 and a3 > 0 and (a1 + a2 > a3) and (a1 + a3 > a2) and (a2 + a3 > a1 ):
#     print('Você consegue fazer um triangulo!')
# else:
#     print('Você nao consegue formar um triangulo')