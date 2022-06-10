#!/usr/bin/python3

import sys
from random import randint
from time import sleep

itens = ('Pedra 🪨', 'Papel 📜', 'Tesoura ✂️')
JKPBot = randint(0,2)

if len(sys.argv) > 1:
    # se o primeiro argumento for um numero
    if sys.argv[1].isdigit():
        escolhaDoJogador = int(sys.argv[1])
    else:
        print("O argumento passado não é um número")
        exit(1)
else:
    print('''Escolha uma das opções:
    [0]Pedra   --------------- 🪨
    [1]Papel   --------------- 📜
    [2]Tesoura --------------- ✂️''')
    escolhaDoJogador = int(input("Faça sua jogada: "))

# se valor não está dentro de itens retirna erro
# escolhaDoJogador = int(input("Faça sua jogada: "))
if escolhaDoJogador not in range(0,3):
    print("-" *60)
    print('Valor inválido')
    print("-" *60)
    exit(1)

print(" " *60)
print("-" *60)
print("Você jogou {}".format(itens[int(escolhaDoJogador)]))
print("-" *60)

print(" " *60)
print('🪨  📜 ✂️')   # Pedra, Papel, Tesoura
print("JO")
sleep(0.5)
print(" " *5, "KEN")
sleep(0.5)
print(" " *10, "PO")
print(" " *15, "!!!!")

print('oo\n/\\')   # Tesoura

sleep(1)

# vencedor
if escolhaDoJogador == JKPBot:
    resultado ='Empate'
    emoji = '🤷 😶 🙄'
elif escolhaDoJogador == 0 and JKPBot == 2:
    resultado = 'Você venceu!'
    emoji = '🎉 🥳 🎊'
elif escolhaDoJogador == 1 and JKPBot == 0:
    resultado = 'Você venceu!'
    emoji = '🎉 🥳 🎊'
elif escolhaDoJogador == 2 and JKPBot == 1:
    resultado = 'Você venceu!'
    emoji = '🎉 🥳 🎊'
else:
    resultado ='JKPBot venceu'
    emoji = '😭 😭 😭'

print(" " *60)

print("-" *60)
print("-" *23, 'Fim do jogo', "-" *24)
print("-" *24, 'RESULTADO', "-" *25)
print("-" *60)
print(" " *60)
print(" " *(26), "...", " " *(28 - 3))
sleep(1)
print(" " *(26), "...", " " *(28 - 3))
sleep(1)
print(" " *(26), "...", " " *(28 - 3))
sleep(1)
print(" " *60)

metadeDoTamanho = len(resultado) // 2
print("-" *60)
print("-" *(26 - metadeDoTamanho), "> {} <".format(resultado), "-" *(28 - metadeDoTamanho))
print("-" *(26 - 4), "> {} <".format(emoji), "-" *(28 - 4))
print("-" *60)
print(" " *60)

sleep(1)

print("-" *60)
print("Você jogou {}".format(itens[int(escolhaDoJogador)]))
print("JKPBot 🤖 jogou {}".format(itens[JKPBot]))
print("-" *60)
print(" " *60)
