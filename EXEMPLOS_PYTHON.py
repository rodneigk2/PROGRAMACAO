# ==============================================================
# 1️⃣ TIPOS PRIMITIVOS
# ==============================================================

# int() → converte string ou float para inteiro
num_inteiro = int("7")  
print(num_inteiro)  # Saída: 7

# float() → converte string ou inteiro para número real
num_real = float("4.5")  
print(num_real)  # Saída: 4.5

# bool() → converte valor para True ou False
logico = bool(0)  
print(logico)  # Saída: False (0 é considerado falso)

logico2 = bool("texto")  
print(logico2)  # Saída: True (string não vazia é verdadeira)

# str() → converte qualquer valor para texto
texto = str(123)  
print(texto)  # Saída: '123'

# ==============================================================
# 2️⃣ MÉTODOS DE VARIÁVEIS
# ==============================================================

var = "Python3"

print(type(var))        # Mostra o tipo da variável → <class 'str'>
print(var.isnumeric())  # Verifica se contém apenas números → False
print(var.isdigit())    # Verifica se contém apenas dígitos → False
print(var.isalpha())    # Verifica se contém apenas letras → False
print(var.isalnum())    # Letras ou números? → True
print(var.islower())    # Todas minúsculas? → False
print(var.isupper())    # Todas maiúsculas? → False
print("   ".isspace())  # Contém apenas espaços? → True
print(var.istitle())    # Primeira letra maiúscula e o resto minúscula? → True

# ==============================================================
# 3️⃣ OPERADORES ARITMÉTICOS
# ==============================================================

a, b = 5, 2
print(a + b)   # Soma → 7
print(a - b)   # Subtração → 3
print(a * b)   # Multiplicação → 10
print(a / b)   # Divisão → 2.5
print(a ** b)  # Potência → 25
print(a // b)  # Divisão inteira → 2
print(a % b)   # Resto da divisão → 1

# Ordem de precedência
result = 2 + 3 * 4  # Multiplicação acontece primeiro
print(result)       # Saída: 14
result = (2 + 3) * 4  # Parênteses alteram a precedência
print(result)         # Saída: 20

# ==============================================================
# 4️⃣ IMPORTAÇÃO DE BIBLIOTECAS
# ==============================================================

import math  # importa toda a biblioteca math
print(math.sqrt(16))  # Raiz quadrada → 4.0

from math import pow  # importa apenas a função pow
print(pow(2, 3))     # 2 elevado a 3 → 8.0

# ==============================================================
# 5️⃣ CONDIÇÕES E OPERADORES LÓGICOS
# ==============================================================

x = 10
y = 5
if x > 0 and (y > 0 or y == 5):
    print("Condição satisfeita")  # Será exibido pois x>0 e y==5

# ==============================================================
# 6️⃣ MATCH CASE (Python 3.10+)
# ==============================================================

valor = "B"
match valor:
    case "A":
        print("Opção A")
    case "B":
        print("Opção B")  # Saída: Opção B
    case _:  
        print("Outro valor")  # Caso nenhum dos anteriores seja verdadeiro

# ==============================================================
# 7️⃣ CONTADORES
# ==============================================================

soma = 0
cont = 0
for i in range(1, 6):
    soma += i  # Acumula o total → 1+2+3+4+5 = 15
    cont += 1  # Conta quantos números foram percorridos → 5

print(soma)  # Saída: 15
print(cont)  # Saída: 5

# ==============================================================
# 8️⃣ LISTAS E MÉTODOS
# ==============================================================

lista = [1, 2, 3]

lista.insert(1, 10)  # Insere 10 na posição 1 → [1, 10, 2, 3]
print(lista)

lista.append(4)       # Adiciona 4 no final → [1, 10, 2, 3, 4]
print(lista)

del lista[2]          # Remove elemento no índice 2 → [1, 10, 3, 4]
print(lista)

lista.pop()           # Remove último elemento → [1, 10, 3]
print(lista)

lista.remove(10)      # Remove o valor 10 → [1, 3]
print(lista)

nova_lista = sorted([5, 2, 9])  # Retorna nova lista ordenada → [2, 5, 9]
print(nova_lista)

lista.sort(reverse=True)  # Ordena a lista original do maior para o menor → [3, 1]
print(lista)

# ==============================================================
# 9️⃣ FUNÇÕES DIVERSAS
# ==============================================================

# end e \n
print("Olá", end=" ")  # Não quebra linha
print("Mundo")          # Saída: Olá Mundo

print("Linha 1\nLinha 2")  # Quebra de linha → Linha 1, Linha 2
print("Sobrescrevendo\rNova")  # Sobrescreve a linha → Nova

# max e min
numeros = (3, 7, 1)
print(max(numeros))  # Maior valor → 7
print(min(numeros))  # Menor valor → 1

# len() → tamanho de string ou lista
print(len("Python"))  # 6
print(len([1,2,3]))  # 3

# replace(), split(), join(), lower()
texto = "a b c"
print(texto.replace(" ", ""))  # Remove espaços → 'abc'

texto = "Python é legal"
palavras = texto.split()       # Divide em lista → ['Python', 'é', 'legal']
print(" ".join(palavras))     # Junta lista → 'Python é legal'

print("PYTHON".lower())       # Converte para minúsculas → 'python'

# locals() → verifica se variável existe no escopo atual
x = 10
print('x' in locals())        # True

# enumerate() → percorre lista com índice
frutas = ["maçã", "banana"]
for i, fruta in enumerate(frutas):
    print(i, fruta)           # 0 maçã, 1 banana

# count() → conta quantas vezes valor aparece
lista = [1, 2, 1, 3]
print(lista.count(1))         # 2

# index() → retorna índice da primeira ocorrência
print(lista.index(3))         # 3 está no índice 3

# startswith() e endswith()
palavra = "Python"
print(palavra.startswith("Py"))  # True → começa com "Py"
print(palavra.endswith("on"))    # True → termina com "on"

# Filtrando vogais
for l in "Python":
    if l.lower() in 'aeiou':     # Só permite passar vogais
        print(l, end=" ")        # Saída: i o
