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
# produtos = ('Lápis', 2.00, 'caneta', 2.50, 'cola', 5.00 )
# print('-' * 30)
# print(f'{"LISTAGEM DE PREÇOS":^30}')
# print('-' * 30)
# print(' ')
# for i in range(0, len(produtos)):
#     if i % 2 == 0:
#         print(f'{produtos[i]:.<30}', end='R$ ')
#     else:
#         print(f'{produtos[i]}')

# print(' ')
# print('-' * 30)


#DESAFIO 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# palavras = ('Programaçao', 'Hello World', 'Python', 'Anoes Pelados')
# for p in palavras:
#     print(f'\nNa palavra {p} temos ', end=' ')
#     for l in p:
#         if l.lower() in 'aeiou':
#             print(l, end=' ')


#DESAFIO 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# values = []
# for i in range(0,5):
#     num = int(input(f'Input one value for position: '))
#     values.append(num)
#     if i == 0:
#         greater = num
#         lesser = num
#     else:
#         if num > greater:
#             greater = num
#         elif num < lesser:
#             lesser = num     
# print(f'{greater} is the greater value and your position is {values.index(greater)}')
# print(f'{lesser} is the lesser value and your position is {values.index(lesser)}')


#DESAFIO 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# list_numbers = []
# while True:
#     choice_user = int(input('Imput a number: '))
#     if choice_user in list_numbers:
#         list_numbers.remove(choice_user)
#     else:
#         list_numbers.append(choice_user)
#     cont = input('Do you want continue: [Y/N]: ').lower()[0]
#     if cont == 'n':
#         break
#     elif cont == 'y':
#         continue
#     else:
#         while cont != 'n' and cont != 'y':
#             cont = input('Do you want continue: [Y/N]: ').lower()[0]
# list_numbers.sort()
# print(list_numbers)


#DESAFIO 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
# numbers = [] 
# for i in range(5):
#     num = int(input("Enter a number: "))
#     if len(numbers) == 0:
#         numbers.append(num)
#     else:
#         position = 0
#         while position < len(numbers):
#             if num <= numbers[position]:
#                 break
#             position += 1
#         numbers.insert(position, num)
#print("Ordered list:", numbers)


#DESAFIO 81:  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:  A) Quantos números foram digitados.  B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

list_numbers = []
cont = 0
while True:
    choice_user = int(input('Imput a number: '))
    cont += 1
    list_numbers.append(choice_user)
    user_choice = input('Do you want continue: [Y/N]: ').lower()
    if user_choice == 'n':
        break
    elif user_choice == 'y':
        continue
    else:
        while user_choice != 'n' and user_choice != 'y':
            user_choice = input('Do you want continue: [Y/N]: ').lower()

print(cont)
print(sorted(list_numbers, reverse=True))

if 5 in list_numbers:
    print(f'Have the number five in the list')
else:
    print('Dont have the number five in the list.')