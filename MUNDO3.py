#DESAFIO 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# numero = int(input('Coloque um numero entre 0 e 20: '))
# while True: 
#     if numero >= 0 and numero <= 20:
#      print(contagem[numero])
#      break
#     else:
#         print('Coloque um numero valido')
#         numero = int(input('Coloque um numero entre 0 e 20: '))
#         continue


#DESAFIO 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da São Paulo.
# times_brasileirao_2025 = (
#     "Flamengo", "Palmeiras", "Botafogo", "Bahia", "São Paulo", "Cruzeiro", "Corinthians",
#     "Grêmio", "Ceará", "Atlético-MG", "Bragantino", "Internacional", "Fluminense", "Fortaleza",
#     "Sport", "Vasco da Gama", "Vitória", "Juventude", "Mirassol", "Santos"
# )
# print(times_brasileirao_2025[0:4])
# print(times_brasileirao_2025[-1:-5:-1])
# print(sorted(times_brasileirao_2025))
# print(times_brasileirao_2025.index('São Paulo')+1)


#DESAFIO 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# from random import randint
# numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# for i in numeros:
#     print(f'{i}',end=' ')
#     maior = max(numeros)
#     menor = min(numeros)
# print(f'\nO maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')


#DESAFIO 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
# for c in range(0, 4):
#     valores = int(input(f'Coloque o primeiro {c+1} numero: ')) 
#     if c == 0:
#         primeiro = valores
#     elif c == 1:
#         segundo = valores
#     elif c == 2:
#         terceiro = valores
#     else:
#         quarto = valores
# tupla = (primeiro, segundo, terceiro, quarto)

# print(tupla,end=' ')
# print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')
# if 3 in tupla:
#     print(f'A primeira vez que aparece o numero 3 é na {tupla.index(3)+1} linha')
# else:
#     print('O numero 3 não foi digitado')
# print(f'Os numeros pares são: ', end='')
# if primeiro % 2 == 0:
#     print(f'{primeiro}',end=' ')
# if segundo % 2 == 0:
#     print(f'{segundo}',end=' ')
# if terceiro % 2 == 0:
#     print(f'{terceiro}',end=' ')
# if quarto % 2 == 0:
#     print(f'{quarto}',end=' ')  

#DESAFIO 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 2.00, 'caneta', 2.50, 'cola', 5.00 )
nome = produtos[0], produtos[2], produtos[4]
preco = produtos[1], produtos[3], produtos[5]

print(f'{nome:<10} R$ {preco:>5.2f}')
