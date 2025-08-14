
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
     
