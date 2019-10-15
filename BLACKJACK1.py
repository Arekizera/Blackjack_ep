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
mc = [] #mão do croupier

lista_sim = ["Sim", "SIM", "sim", "S", "s"] #lista de possibilidades de "sim"
lista_nao = ["Não", "NÃO", "não", "Nao", "NAO", "nao", "N", "n"] #lista de possibilidades de "não"
lista_continuar = ["continuar", "Continuar", "CONTINUAR"] # lista de possibilidade de "continuar"
lista_carta=["carta", "cartas", "Carta", "Cartas"]  #lista de possibilidades de "carta"

nome = input("Digite seu nickname: ")
d = float(input("Digite a quantidade de dinheiro que deseja apostar: "))
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
    

    

    