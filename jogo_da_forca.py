import random
import os
from time import sleep

#lista de palavras
lista_palavras_forca = [
"Abacaxi",
"Banheiro",
"Computador",
"Carnaval",
"Dança",
"Elefante",
"Futebol",
"Girassol",
"Heliporto",
"Jacare",
"Kaleidoscopio",
"Leao",
"Maracuja",
"Navio",
"Ovo",
"Passaro",
"Quiabo",
"Refrigerante",
"Surpresa",
"Teatro",
"Uva",
"Violao",
"Xicara",
"Yoga",
"Zebra",
"Abajur",
"Bicicleta",
"Carrinho",
"Dicionario",
"Escola",
"Flauta",
"Gato",
"Hidrante",
"Igreja",
"Jardim",
"Kilt",
"Lampada",
"Microfone",
"Numero",
"Ovelha",
"Pagina",
"Qualidade",
"Relogio",
"Sapato",
"Tijolo",
"Urso",
"Vela",
"Xadrez",
"Yacht",
"Zoologico"
]

programa = ""
letra = ""

while True:
    
    #início do programa
    programa = input("\n----------JOGO DA FORCA----------\n\nPressiona ENTER pra jogar ou '0' para sair. ")
    
    #comando para parar o programa
    if programa == "0":
        os.system('cls')
        print('\n\nEspero que tenha se divertido, até mais!')
        sleep(3)
        break
    
    #palavra aleatória da lista
    palavra_forca = random.choice(lista_palavras_forca).lower()
    
    letras_corretas = []
    letras_erradas = []
    
    #dicas pré-jogo
    os.system('cls')
    print(f"\nSerá que você vai acertar essa?\nA palavra sorteada tem {len(palavra_forca)} letras.")
    print("\nLembre-se que você só tem 6 vidas!")
    print('\n\nCarregando...')
    sleep(5)
    
    chances = 6
    
    while True:    
        
        os.system('cls')
    
        #layout forca e letras utilizadas
        print('\nPalavra: ' + " " .join([letra if letra in letras_corretas else "_" for letra in palavra_forca]))
        print('Letras erradas: ' + " " .join(letras_erradas))
        
        #mensagem de acerto
        if set(palavra_forca) == set(letras_corretas) or letra == palavra_forca:
            os.system('cls')
            print(f'\n\nParabéns, você acertou!\nA palavra correta é "{palavra_forca}".')
            sleep(1)
            print('\nQuer tentar de novo?\n')
            sleep(1)
            break
        
        #input letra
        letra = input(f'\n{chances} Chance(s): ').lower()
        
        #mensagem letras repetidas
        if letra in letras_corretas + letras_erradas:
            print('\nVoce ja chutou essa letra!')
            sleep(2)
        
        #mensagem caso perca o jogo
        if len(letras_erradas) == 6:
            os.system('cls')
            print(f'\nVocê excedeu as 6 vidas. :(\n\nA palavra certa era "{palavra_forca}".')
            sleep(2)
            print('\nVocê gostaria jogar novamente?')
            sleep(1)
            break
        
        #adicionar letra na forca 
        elif letra in palavra_forca:
            letras_corretas.append(letra)
            
        #adicionar letra na lista de letras erradas + contabilizar n° chances
        else:
            letras_erradas.append(letra)
            chances -= 1
            if chances == 0:
                chances = "ÚLTIMA"