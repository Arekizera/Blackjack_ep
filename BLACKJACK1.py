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
              \n' 
              'BlackJack é um jogo cujo o objetivo é somar 21 pontos com a soma dos valores das cartas.\n'
              '\n'
              'Como jogar:\n'
              '• Inicialmente, é feito uma aposta por parte do jogador, e recebendo duas cartas do baralho.\n'
              '• O Croupier também recebe duas cartas, porém você não sabe quais são.\n'
              '• Caso o valor das cartas passe de 21 pontos, você ou o Croupier perdem.\n'
              '\n'
              'Regras do Jogo:\n'
              '• O jogo é composto de no maximo 10 baralhos de 52 cartas cada.\n'
              '• As cartas Reis, Damas e Valetes valem 10 pontos.\n'
              '• As demais cartas valem o proprio valor escrito nelas.\n'
              '• Caso você receba um As e a sua ou a pontuação do Croupier estore, esse As passa a valer apenas 1 (um) ponto.\n'
              '• A cada rodada é feita uma nova aposta por parte do jogador e é sorteada mais uma carta tanto para ele quanto para o Croupier.\n'
              '• As apostas são feitas no inicial de cada dedido de carta.\n'
              '• Caso você faça Blackjack ou o Croupier perca, você recebe o valor apostado.\n'
              '• Caso você perca, o dinheiro é perdido também.\n')
        break
    elif pergunta == "s":
        break
        print("Desculpe, não entendi.")
    pergunta = input("Você sabe jogar Blackjack?: ")
    
         
print("\n\nDICAS ADICIONAIS: \n")    
print("Dica-1: Não aposte mais dinheiro do que você tem.\n")
print("Dica-2: Se logo no inicio suas cartas já somarem 21 pontos (10 pontos + Ás), você ganha 1,5x o valor apostado.\n")
print("Dica-3: Se você ganhar ou perder de outra forma você ganha ou perde exatamente o valor apostado.\n")
print("Dica-4: Enquanto a mão do croupier for menor que a sua, ele vai tirar mais cartas até que o valor minimo de 17 pontos seja atingido.\n")
print("Dica-5: Se quiser que o jogo pare, digite 'desisto' ou 'fim'.\n\n")
print("Boa sorte {0}!".format(nome))

dinheiro = float(input("Quanto dinheiro você tem pra apostar?: "))
if dinheiro < 1:
    print("Não é possivel apostar esse valor, tente apostar um pouco mais!")
    dinheiro = float(input("Quanto dinheiro você tem para jogar?: "))

quant = 0 #loop quantidade de baralhos
incentivo = 0 #loop pra incentivar jogador a escolher menos baralhos
