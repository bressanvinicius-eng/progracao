import random

def jogar():
    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print("Escolha seu nível de dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 50)")
    print("3 - Difícil (1 a 100)")

    escolha = input("Digite o nível (Fácil/Médio/Difícil): ").strip().capitalize()

    # Definindo o limite superior baseado na dificuldade
    if escolha == "Fácil":
        limite_superior = 10
    elif escolha == "Médio":
        limite_superior = 50
    elif escolha == "Difícil":
        limite_superior = 100
    else:
        print("Opção inválida! Definindo dificuldade para Médio por padrão.")
        limite_superior = 50

    # Gerando o número aleatório com base no intervalo escolhido
    numero_secreto = random.randint(1, limite_superior)
    tentativas = 0
    acertou = False

    print(f"\nLegal! Eu pensei em um número entre 1 e {limite_superior}.")

    while not acertou:
        try:
            chute = int(input("Qual é o seu palpite? "))
            tentativas += 1

            if chute == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                acertou = True
            elif chute < numero_secreto:
                print("Mais alto...")
            else:
                print("Mais baixo...")
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    jogar()
