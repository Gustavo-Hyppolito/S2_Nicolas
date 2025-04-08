import random

# Função pra gerar saldo inicial
def gerar_saldo():
    return round(random.uniform(1000.00, 50000.00), 2)

# Função principal do jogo
def cassino():
    print("Bem-vindo ao Cassino Python")
    cpf = input("Digite seu CPF para iniciar: ")
    saldo = gerar_saldo()
    print(f"CPF cadastrado com sucesso! Seu saldo inicial é de R$ {saldo:.2f}\n")

    while True:
        print("\nJogo da Roleta - Aposta em um número de 1 a 10")
        print(f"Saldo atual: R$ {saldo:.2f}")
        
        try:
            aposta = float(input("Digite o valor da sua aposta: R$ "))
            if aposta <= 0 or aposta > saldo:
                print("Aposta inválida. Verifique o valor.")
                continue

            numero_escolhido = int(input("Escolha um número entre 1 e 10: "))
            if numero_escolhido < 1 or numero_escolhido > 10:
                print("Número inválido.")
                continue
        except ValueError:
            print("Entrada inválida. Use apenas números.")
            continue

        numero_sorteado = random.randint(1, 10)
        print(f"A roleta girou e caiu no número: {numero_sorteado}")

        
            saldo -= aposta
            print(f"Você perdeu R$ {aposta:.2f}")

        if saldo <= 0:
            print("Você perdeu todo seu dinheiro. Fim de jogo.")
            break

        continuar = input("Deseja jogar novamente? (sim/não): ").lower()
        if continuar != "sim":
            input(f"Obrigado por jogar. Seu saldo final foi R$ {saldo:.2f}")
            def
# Inicia o jogo
cassino()
