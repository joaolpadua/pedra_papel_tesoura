import random
print("Bem vindo ao jogo pedra papel tesoura!!")

lista_PPT = [ 0 ,"Pedra", "Papel", "Tesoura"]
contador = 0
pontos_usuario = 0
pontos_computador = 0

while True:
    escolha_do_usuario = input( "Meus pontos: " + str(pontos_computador) + " Seus pontos: " + str(pontos_usuario) +
                                "\nQual sua escolha?: \n (1) Pedra \n (2) Papel \n (3) Tesoura \n Q para sair \n" )

    escolha_do_computador = random.randint(1, 3)

    if escolha_do_usuario == "q" or escolha_do_usuario == "Q":
        break

    else:
        escolha_do_usuario = int(escolha_do_usuario)
        if escolha_do_usuario == escolha_do_computador:
            print("Empate!! Escolhemos " + lista_PPT[escolha_do_usuario])
        elif escolha_do_usuario == 1 and escolha_do_computador == 2:
            print(lista_PPT[escolha_do_computador] + " ganha de " + lista_PPT[escolha_do_usuario] + " eu ganhei!")
            pontos_computador += 1
        elif escolha_do_usuario == 2 and escolha_do_computador == 3:
            print(lista_PPT[escolha_do_computador] + " ganha de " + lista_PPT[escolha_do_usuario] + " eu ganhei!")
            pontos_computador += 1
        elif escolha_do_usuario == 3 and escolha_do_computador == 1:
            print(lista_PPT[escolha_do_computador] + " ganha de " + lista_PPT[escolha_do_usuario] + " eu ganhei!")
            pontos_computador += 1
        else:
            print(lista_PPT[escolha_do_usuario] + " ganha de " + lista_PPT[escolha_do_computador] + " você ganhou!")
            pontos_usuario += 1
        continue


