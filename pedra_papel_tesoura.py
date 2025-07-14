import random

placar = 0

while True:
    cpu = random.randint(1, 3)
    escolha = int(input("Escolhe\n 1 para Pedra\n 2 para Papel\n 3 para Tesoura: "))
    match cpu:
         case 1 : pal = "Pedra"
         case 2 : pal = "Papel"
         case 3 : pal = "Tesoura"
    match escolha:
         case 1 : pala = "Pedra"
         case 2 : pala = "Papel"
         case 3 : pala = "Tesoura"
    if cpu == escolha:
        print("Empate!")
    elif (escolha == 1 and cpu == 3) or (escolha == 2 and cpu == 1) or (escolha == 3 and cpu == 2):
        print("Você venceu!")
        placar += 1
    else:
        print("Você perdeu!")
        placar -= 1

    print(f"Computador escolheu: {pal}")
    print(f"Você escolheu: {pala}")
    print(f"Placar: {placar}")

    i = int(input("Aperte 1 se quiser sair ou 2 para continuar: "))
    if i == 1:
        break
    elif i != 2:
        print("Digite errado, saindo do jogo!")
        break