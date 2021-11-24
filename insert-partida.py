import psutil
import time
from functools import reduce
from connectdb import *

opcaoMenu = 0;
opcaoVencer = 0;
opcaoSair = 0;
frag = "0";
jogoEscolhido = "";
nickname = "";
statusPartida = "";

print("Digite seu nick no jogo: ")
nickname = input()
sair = True;

while opcaoMenu != "1" and opcaoMenu != "2" and opcaoMenu != "3" or sair: 
    print("-"*40, "//", "-"*45)
    print(" "*44, f"Bem vindo - {nickname}")
    print("-"*45, "//", "-"*45)
    print("1 - Counter Strike - Global Offensive")
    print("2 - League of Legends")
    print("3 - Valorant")
    opcaoMenu = input("Digite o jogo escolhido para registrar partida: ")
    print("-"*45, "//", "-"*45)

    if(opcaoMenu == "1"):
        jogoEscolhido = "Counter Strike - Global Offensive"
        print("Você venceu ?")
        print("1 - Sim")
        print("2 - Não")
        opcaoVencer = input()
        if(opcaoMenu == 1):
            statusPartida = "Venceu"
        else:
            statusPartida = "Perdeu"

    if(opcaoMenu == "2"):
        jogoEscolhido = "League of Legends"
        print("Você venceu ?")
        print("1 - Sim")
        print("2 - Não")
        opcaoVencer = input()
        if(opcaoMenu == 1):
            statusPartida = "Venceu"
        else:
            statusPartida = "Perdeu"

    if(opcaoMenu == "3"):
        jogoEscolhido = "Valorant"
        print("Você venceu ?")
        print("1 - Sim")
        print("2 - Não")
        opcaoVencer = input()
        if(opcaoMenu == 1):
            statusPartida = "Venceu"
        else:
            statusPartida = "Perdeu"
    
    frag = input("Informe seu frag da partida: ")

    insert_db(nickname, jogoEscolhido, statusPartida, frag);

    print("Deseja sair ?")
    print("1 - Sim")
    print("2 - Não")
    opcaoSair = input()
    if(opcaoSair == "1"):
        sair = False;
    else:
        sair = True;
    

