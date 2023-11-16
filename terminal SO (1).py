import os
import sys

# Função para analisar a entrada do usuário em tokens
def parse_input(input_str):
    tokens = input_str.split()
    return tokens

# Simular terminal
print("Bem-vindo ao terminal")
vetor = []  # Lista para armazenar o histórico de comandos
while True:
    entrada = input("osh> ")

    # Verifica se o usuário digitou "exit" para sair
    if entrada == "exit":
        print("Adeus usuário, foi bom tê-lo aqui")
        break

    # Comando 'history' para listar o histórico
    if entrada == "history":
        for i, comando in enumerate(vetor, start=1):
            print(f"{i} {comando}")
        continue

    # Comando '!!' para executar o comando mais recente
    if entrada == "!!":
        if vetor:
            entrada = vetor[-1]
        else:
            print("Nenhum comando no histórico")
            continue

    # Comando '!N' para executar o N-ésimo comando
    if entrada.startswith("!"):
        try:
            n = int(entrada[1:])
            if 1 <= n <= len(vetor):
                entrada = vetor[n - 1]
            else:
                print("Nenhum comando correspondente no histórico")
                continue
        except ValueError:
            print("Formato de comando inválido")
            continue

    # Analisa a entrada do usuário em tokens
    args = parse_input(entrada)

    # Criar um processo-filho
    pid = os.fork()

    if pid == 0:
        # Processo-filho
        try:
            # Executar o comando utilizando a função execvp
            os.execvp(args[0], args)
        except Exception as e:
            print("Erro ao executar o comando: {e}")
            sys.exit(1)
    elif pid > 0:
        # Processo-pai
        os.wait()  # Aguarda o processo-filho terminar

    # Adiciona o comando ao histórico
    vetor.append(entrada)
