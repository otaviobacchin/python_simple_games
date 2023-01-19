import random
import os
from time import sleep

#lista com opções do computador
pedra_papel_tesoura = ["pedra", "papel", "tesoura"]

#lista para checagem de comandos do usuário
comandos = pedra_papel_tesoura.copy()
comandos.append("q")

#validando a escolha do usuário
def escolha_usuario():
    
    while True:
        
        #escolha
        escolha = input('\nQual sua escolha? (pedra/papel/tesoura): ').lower()
        
        #checagem se o comando é válido
        try:
            if escolha in comandos:
                return escolha
        except:
            print("\nDigite um comando válido.")
        else:
            print("\nDigite um comando válido.")
    
#checagem da partida        
def check():
    
    if escolha == escolha_pc:
        print("\n-----\nEMPATE!\n-----")
        
    elif escolha == "pedra" and escolha_pc == "tesoura":
        print("\n-----\nVOCÊ GANHOU!\n-----")

    elif escolha == "tesoura" and escolha_pc == "papel":
        print("\n-----\nVOCÊ GANHOU!\n-----")
        
    elif escolha == "papel" and escolha_pc == "pedra":
        print("\n-----\nVOCÊ GANHOU!\n-----")
        
    else:
        print("\n-----\nVOCÊ PERDEU!\n-----")


#programa
while True:
    
    #mensagem inicial
    print('\n\n--------------------\nJogo do PEDRA, PAPEL ou TESOURA\n--------------------\n\n(Digite "q" para sair)\n\n')
    
    #função do comando do usuário
    escolha = escolha_usuario()
    
    #escolha do computador
    escolha_pc = random.choice(pedra_papel_tesoura)
    
    #comando para sair do jogo
    if escolha == "q":
            break

    #partida
    print(f"\nJogador >>>>>>>>>> {escolha.upper()} vs {escolha_pc.upper()} <<<<<<<<<< Computador")

    #função de checagem para ver o ganhador
    check()
        
    #comando para reiniciar ou sair do jogo
    escolha = input('\n\nPressione ENTER para jogar novamente ou "q" para sair: ')
    
    if escolha == "q":
        break
    
    #limpa o terminal
    os.system('cls')
    
#mensagem de finalização do programa
print("\n\nAté mais!\n")
sleep(1)





