#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:42:11 2019

@author: Alex
"""
import random

#Alunos:
#- Alex Steijntjes, alexs4@al.insper.edu.br
#- Bruno Tosi, brunoct1@al.insper.edu.br

J = 10 #todas com figura valem 10 pontos
Q = 10
K = 10
A = 11 #vale 11 se a mao for estourar
baralhoinicial = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]*4 #cada baralho tem 4 desses
naipes = ["paus", "copas", "espadas", "pica"]
baralho = (baralhoinicial)
maojog = [] #mão do jogador
maocro = [] #mão do croupier

lista_sim = ["Sim", "SIM", "sim", "S", "s"] #lista de possibilidades de "sim"
lista_nao = ["Não", "NÃO", "não", "Nao", "NAO", "nao", "N", "n"] #lista de possibilidades de "não"
lista_continuar = ["continuar", "Continuar", "CONTINUAR"] # lista de possibilidade de "continuar"
lista_carta=["carta", "cartas", "Carta", "Cartas"]  #lista de possibilidades de "carta"

nome = input("Digite seu nickname: ")
dinheiro = float(input("Digite a quantidade de dinheiro que deseja apostar: "))

ajudinha = "nao"
help = "No inicio da partida, voce apostará um valor e em seguida receberá duas cartas. Cada carta tera um valor somado; caso esse valor passe de 21 pontos, voce estoura e perde.(Cartas de número valem seu próprio valor, cartas de figuras valem 10 pontos, e o Ás vale 11 pontos. Portanto, se sua mão valer mais de 21 pontos e você tem um Ás, o Ás passa a valer 1 ponto somente). Ganha o jogador que tiver o número mais proximo de 21 sem passa-lo. (Você pode pedir mais cartas caso deseje)" #texto de ajuda
print("Bem vindo ao Blackjack jogador {0}!".format(nome))

pergunta = input("Voce sabe como se joga Blackjack?: ")
while pergunta in lista_nao:
    print(help)
    ajudinha = input("Agora esta claro?: ")
    if ajudinha in lista_sim:
        break
    else:
        continue
        
        
print(" ")    
print("REGRINHAS / DICAS ADICIONAIS: ")
print(" ")

print("Dica-1: Não aposte mais dinheiro do que você tem.")
print(" ")
print("Dica-2: Se logo no inicio suas cartas já somarem 21 pontos (10 pontos + Ás), você ganha 1,5x o valor apostado.")
print(" ")
print("Dica-3: Se você ganhar ou perder de outra forma você ganha ou perde exatamente o valor apostado.")
print(" ")
print("Dica-4: Enquanto a mão do croupier for menor que a sua, ele vai tirar mais cartas até que o valor minimo de 17 pontos seja atingido.")
print(" ")
print("Dica-5: Se quiser que o jogo pare, digite 'desisto' ou 'fim'.")
print(" ")
print(" ")
print("Boa sorte {0}!".format(nome))

quant = 0 #loop quantidade de baralhos
incentivo = 0 #loop pra incentivar jogador a escolher menos baralhos

while quant<1 or quant>10 or incentivo in lista_nao:
    incentivo='s'
    quant=int(input("Com quantos baralhos deseja jogar? "))
    if quant>10:
        print("O valor máximo são 10 baralhos apenas!")
        continue
    elif quant<1:
        print("Valor inválido.")
        continue
    elif quant>3:
        incentivo=input("O jogo funciona melhor com menos baralhos, tem certeza que deseja manter {0} baralhos? ".format(quant))
    if incentivo in lista_nao:
        continue
    elif incentivo in lista_sim:
        break 

baralho = baralho * quant
while dinheiro != 0:
    maocro.clear()
    maojog.clear()
    print("Voce tem {0}, reais".format(dinheiro))
    aposta = int(input("Aposte um valor inteiro: "))
    if aposta == "fim" or aposta == "desisto":
        print("Você perdeu!")
        break
    if aposta < 1:
        print("Valor inválido!")
        continue
    if aposta > dinheiro:
        print("Você tentou apostar mais dinheiro do que realmente tem, invalido!")
        continue
    maojog.append(random.choice(baralho))
    maojog.append(random.choice(baralho))
    if sum(maojog) > 21 and A in maojog:
        substituir = maojog.index(A)
        maojog[substituir] = 1
    if sum(maojog) > 21:
        print("Voce ultrapassou o limite pontos")
        dinheiro -= aposta
        continue
    if sum(maojog) == 21:
        dinheiro = (dinheiro + (1.5*aposta))
        print("Meus parabens, voce ganhou um Blackjack")
        continue
    print("Suas cartas são: ", maojog, "dando um total de: ", sum(maojog))
    sn = input("voce quer 'continuar' ou 'mostrar cartas': ")
    if sn in lista_continuar:
        maojog.append(random.choice(baralho))
        if sum(maojog) > 21 and A in maojog:
            substituir = maojog.index(A)
            maojog[substituir] = 1
        if sum(maojog) > 21:
            print("Voce passou do limite com as cartas", maojog,)
            dinheiro -= aposta
            break
        elif sum(maojog) == 21:
            dinheiro = dinheiro + (1.5 * aposta)
            print("Meus parabéns voce completou um Blackjack com as cartas", maojog,)
            break
        print("Suas cartas são: ", maojog, "dando um total de: ", sum(maojog))
        sn = input("voce quer 'continuar' ou 'mostrar cartas': ")
    if sum(maojog) >= 21:
        continue
    maocro.append(random.choice(baralho))
    maocro.append(random.choice(baralho))
    print("As cartas do croupier são: ", maocro, "dando um total de: ", sum(maocro))
    while sum(maocro) < 17 and sum(maojog) > sum(maocro):
        maocro.append(random.choice(baralho))
        print("As cartas do croupier são: ", maocro, "dando um total de: ", sum(maocro))
    if sum(maocro) > 21 and A in maocro:
        substituir = maocro.index(A)
        maocro[substituir] = 1
    if sum(maocro) > 21:
        print("Croupier passou do limite")
        dinheiro += aposta
        print("Voce foi o vencedor!, parabens {0}".format(nome))
        continue
    if sum(maojog) == sum(maocro):
        print("Foi um empate!")
        continue
    elif sum(maojog) > sum(maocro):
        dinheiro += aposta
        print("Voce foi o vencedor!, parabens {0}".format(nome))
        continue
    elif sum(maocro) > sum(maojog):
        dinheiro -= aposta
        print("Que pena, o croupier ganhou")
        continue
if dinheiro == 0:
    print("Meu amigo {0}, parece que seu dinheiro acabou. PARE DE JOGAR E VÁ TRABALHAR VAGABUNDO".format(nome))
print(" ")
print("Até a próxima!") 
