
# nome = input('Coloque seu nome: ')
# print(f'Olá {nome:=^20}!!!')



# Existem duas formas de mostrar o resultado da multiplicação:
# Armazenando o resultado em uma variável antes de exibir:
#  m = n1 * n2
#  print(m)
# Isso permite reutilizar o valor de 'm' depois, se necessário.



# Tipos de alinhamento
# Alinhamento à esquerda: O texto começa do lado esquerdo do espaço disponível.

# Alinhamento à direita: O texto termina do lado direito do espaço disponível.

# Alinhamento centralizado: O texto fica centralizado no espaço disponível.

# Como alinhar strings em Python
# Você pode usar o método .ljust(), .rjust(), .center() ou formatação com f-strings.

# Exemplos
# Ou usando f-strings:
# Dicas
# O número após os dois pontos (:.2f) indica o tamanho do campo. (2 é exemplo)
# O alinhamento é útil para criar tabelas ou relatórios legíveis no terminal.



# import emoji
# print(emoji.emojize(":alien:"))



# FORMATACAO DE TXT 
# {nome:=^20}: 20 (quantidade) define o tamanho total do campo,
#              ^ (acento circunflexo) centraliza o texto.
#              = (igual) preenche os espaços vazios com o caracter =;
#             Você pode trocar o '=' por qualquer outro caracter, como *, -, #, etc.



# valor = int(input('coloque o valor'))
# match valor:
#     case x if x < 5:  (Pode se ultilizar qualquer palavra para receber a variavel VALOR depois do case.)
#         print("Menor que 5")
#     case x if x < 10:
#         print("Entre 5 e 9")
#     case _:
#         print("10 ou mais")
     


usuario = int(input('Coloque um numero para ver sua tabuada: '))

# Aqui a gente cria uma variável chamada tab e começa ela em 0. 
# Ela vai ser usada como acumulador — ou seja, vamos somando valores nela ao longo do laço.
tab = 0  

# Esse for cria um contador chamado c. 
# O range(1, 11) gera os números de 1 até 10 (o último nunca entra).
# Então o c vai ter esses valores: 1, 2, 3, ..., 10.
# Cada volta do for é uma “rodada” da tabuada.
for c in range(1, 11):    

    # O operador += significa "pega o valor atual de tab e soma com usuario".
    # Como tab começa em 0, a cada volta do for ele vai acumulando o valor de usuario.
    tab += usuario   

    # O print mostra o número digitado (usuario), o multiplicador (c) e o resultado (tab).
    print(f'{usuario} X {c} = {tab}')



soma = 0    # acumulador (vai guardar a soma dos números)
cont = 0    # contador (vai contar quantos números já foram digitados)

for i in range(5):
    n = int(input('Digite um número: '))
    soma += n    # acumula os valores
    cont += 1    # conta +1 a cada número digitado

print(f'Você digitou {cont} números')
print(f'A soma deles foi {soma}')
print(f'A média é {soma / cont}')
