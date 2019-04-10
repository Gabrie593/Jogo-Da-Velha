# Bibliotecas que serão usadas
import random

# Variaveis que representam cada posição
p1 = "1"
p2 = "2"
p3 = "3"
p4 = "4"
p5 = "5"
p6 = "6"
p7 = "7"
p8 = "8"
p9 = "9"

# Construção do Tabuleiro
collumdiv = "|"
boarddiv = "\n---------"
linha1 = p1 + collumdiv + p2 + collumdiv + p3 + boarddiv
linha2 = p4 + collumdiv + p5 + collumdiv + p6 + boarddiv
linha3 = p7 + collumdiv + p8 + collumdiv + p9 
diagonal1 = (p3, p5, p7)
diagonal2 = (p1, p5, p9)
coluna1 = (p1, p4, p7)
coluna2 = (p2, p5, p8)
coluna3 = (p4, p6, p9)
bigboard = ((linha1) + '\n' + (linha2) + '\n' + (linha3))

# Coletar os nomes dos jogadores, e decidir quem deverá começar
nome1 = input("Digite o nome do jogador que representa [x]: ")
nome2 = input("Digite o nome do jogador que representa [O]: ")
iniciante = " "
contrainiciante = " "
if (random.random() * 100) < 50:
    iniciante = nome1
    contrainiciante = nome2
else:
    iniciante = nome2
    contrainiciante = nome1

# Variáveis relativas
quantidade = 0
validade = 0
caracter = (" ")
again = (" ")

# Mostrar o Tabuleiro
print (bigboard)

# O jogo de fato
while (quantidade < 9):
    if (quantidade % 2) != 0:
        caracter = "x"
    else:
        caracter = "O"

    if (quantidade % 2) == 0:
        position1 = input("Agora é a vez de " + iniciante.lower().capitalize() + ", Digite qual posição você quer jogar: ")
    else:
        position1 = input("Agora é a vez de " + contrainiciante.lower().capitalize() + ", Digite qual posição você quer jogar: ")

    validade = 0

    if position1 == ("1") and p1 == "1":
        p1 = caracter 
    elif position1 == ("2") and p2 == "2":
        p2 = caracter
    elif position1 == ("3") and p3 == "3":
        p3 = caracter
    elif position1 == ("4") and p4 == "4":
        p4 = caracter
    elif position1 == ("5") and p5 == "5":
        p5 = caracter
    elif position1 == ("6") and p6 == "6":
        p6 = caracter
    elif position1 == ("7") and p7 == "7":
        p7 = caracter
    elif position1 == ("8") and p8 == "8":
        p8 = caracter
    elif position1 == ("9") and p9 == "9":
        p9 = caracter

    # Checando validade da jogada
    if validade == 1 and position1 == ("1") or position1 == ("2") or position1 == ("3") or position1 == ("4") or position1 == ("5") or position1 == ("6") or position1 == ("7") or position1 == ("8") or position1 == ("9"):
        quantidade = quantidade + 1

        # Atualizando variáveis relativas
        linha1 = p1 + collumdiv + p2 + collumdiv + p3 + boarddiv
        linha2 = p4 + collumdiv + p5 + collumdiv + p6 + boarddiv
        linha3 = p7 + collumdiv + p8 + collumdiv + p9
        diagonal1 = (p3, p5, p7)
        diagonal2 = (p1, p5, p9)
        bigboard = ((linha1) + '\n' + (linha2) + '\n' + (linha3))
        print (bigboard)

        # Checando se aconteceu uma vitória ou uma velha
        if linha1 == 'O|O|O\n---------' or linha2 == 'O|O|O\n---------' or linha3 == 'O|O|O\n---------':
            print ("Vitória de " + nome2)
            break
        if diagonal1 == ("O", "O", "O") or diagonal2 == ("O", "O", "O"):
            print ("Vitória de " + nome2)
            break
        if coluna1 == ("O", "O", "O") or coluna2 == ("O", "O", "O") or coluna3 == ("O", "O", "O"):
            print ("Vitória de " + nome2)
            break
        if linha1 == 'x|x|x\n---------' or linha2 == 'x|x|x\n---------' or linha3 == 'x|x|x\n---------':
            print ("Vitória de " + nome1)
            break
        if diagonal1 == ("x", "x", "x") or diagonal2 == ("x", "x", "x"):
            print ("Vitória de " + nome1)
            break
        if coluna1 == ("x", "x", "x") or coluna2 == ("x", "x", "x") or coluna3 == ("x", "x", "x"):
            print ("Vitória de " + nome1)
            break
        elif quantidade == 9:
            print ("Deu velha!")
            break
     
    else:
        print ("Jogada inválida, tente novamente!")



