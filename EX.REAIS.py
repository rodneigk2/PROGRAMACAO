#Exercício 1: Processador de Lista de Compras. Objetivo: Ler dados de um arquivo de texto, processá-los e calcular um resultado. Esta é uma tarefa muito comum em análise de dados e automação.

# calculadora.py

def calcular_total(nome_arquivo):
    """
    Lê um arquivo de compras e calcula o total.
    """
    total = 0.0
    try:
        # 'with open' garante que o arquivo será fechado corretamente
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Remove espaços em branco no início/fim e quebra a linha na vírgula
                partes = linha.strip().split(',')
                
                # Garante que a linha tem duas partes (produto e preço)
                if len(partes) == 2:
                    try:
                        # Converte a segunda parte (preço) para float e soma ao total
                        preco = float(partes[1])
                        total += preco
                    except ValueError:
                        print(f"Aviso: Ignorando linha mal formatada (preço inválido): {linha.strip()}")
    except FileNotFoundError:
        return "Erro: O arquivo não foi encontrado."
    
    # Formata a saída para ter duas casas decimais, representando centavos
    return f"O custo total da sua compra é: R$ {total:.2f}"

# Nome do arquivo de compras
arquivo_compras = 'compras.txt'

# Chama a função e imprime o resultado
resultado = calcular_total(arquivo_compras)
print(resultado)
