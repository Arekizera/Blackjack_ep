import random

#Alunos:
#- Alex Steijntjes, alexs4@al.insper.edu.br
#- Bruno Tosi, brunoct1@al.insper.edu.br

J = 10 #todas com figura valem 10 pontos
Q = 10
K = 10
A = 11 #vale 1 se a mao for estourar
baralhoinicial = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]*4 #cada baralho tem 4 desses
naipes = ["paus", "copas", "espadas", "ouros"]
baralho = (baralhoinicial)
maojog = [] #mão do jogador
maocro = [] #mão do croupier


lista_continuar = ["continuar", "Continuar", "CONTINUAR"] # lista de possibilidade de "continuar"
lista_carta=["carta", "cartas", "Carta", "Cartas", "CARTA", 'CARTAS', 'c', "C"]  #lista de possibilidades de "carta"


nome = input("Qual o seu nickname?: ")
    
print('Seja bem vindo ao jogo Blackjack, {0}!'.format(nome))

pergunta = input("Você sabe jogar Blackjack? (s/n): ")
while pergunta != "s" or pergunta != "n":
    if pergunta == "n":
        print('\n'
              'Blackjack Insper!\n'
