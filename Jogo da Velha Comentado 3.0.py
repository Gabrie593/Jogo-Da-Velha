# Bibliotecas #
import random
import sys

# Tabuleiro #
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
collumn1 = (board[0][0]), (board[1][0]), (board[2][0])
collumn2 = (board[0][1]), (board[1][1]), (board[2][1])
collumn3 = (board[0][2]), (board[1][2]), (board[2][2])
diagonal1 = (board[0][0]), (board[1][1]), (board[2][2])
diagonal2 = (board[0][2]), (board[1][1]), (board[2][0])

print (board[0])
print (board[1])
print (board[2])

# A jogada do usuário #
# Decidir quem começa #
iniciante = (" ")
contrainiciante = (" ")
if random.random() * 100 < 50:
    iniciante = ("X")
    contrainiciante = ("O")
else:
    iniciante = ("O")
    contrainiciante = ("X")
jogada = 1
# indicar se é a vez do X ou da O #
while jogada < 9:
    # checando se tem vitória ou velha #
    win = False
    vitoriax = ('X', 'X', 'X')
    vitoriao = ('O', 'O', 'O')
    vitoriaxcolchete = ['X', 'X', 'X']
    vitoriaocolchete = ['O', 'O', 'O']
    if (board[0]) == (vitoriaxcolchete) or (board[1]) == (vitoriaxcolchete) or (board[2]) == (vitoriaxcolchete):
        print ("X won!")
        win = True
    elif (collumn1) == (vitoriax) or (collumn2) == (vitoriax) or (collumn3) == (vitoriax):
        print ("X won!")
        win = True
    elif diagonal1 == (vitoriax) or diagonal2 == (vitoriax):
        print ("X won!")
        win = True
    if (board[0]) == (vitoriaocolchete) or (board[1]) == (vitoriaocolchete) or (board[2]) == (vitoriaocolchete):
        print ("O won!")
        win = True
    elif (collumn1) == (vitoriao) or (collumn2) == (vitoriao) or (collumn3) == (vitoriao):
        print ("O won!")
        win = True
    elif diagonal1 == (vitoriao) or diagonal2 == (vitoriao):
        print ("O won!")
        win = True
    if win == False and jogada == 9:
        print ("It's a draw!")
        win = True
    if win == True:
        again = int(input("If you wanna play again, type 1, else, type 0: "))
        if again == 1:
            board = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
            collumn1 = (board[0][0]), (board[1][0]), (board[2][0])
            collumn2 = (board[0][1]), (board[1][1]), (board[2][1])
            collumn3 = (board[0][2]), (board[1][2]), (board[2][2])
            diagonal1 = (board[0][0]), (board[1][1]), (board[2][2])
            diagonal2 = (board[0][2]), (board[1][1]), (board[2][0])

            print ("========================= RESTARTING ========================= ")
            print (board[0])
            print (board[1])
            print (board[2])   
            jogada = 1
        elif again == 0:
            sys.exit()
    if (jogada % 2) != 0:
        caracter = iniciante
        print ("It's", iniciante, "turn!")
    else:
        caracter = contrainiciante
        print ("It's", contrainiciante, "turn!")

    movel = int(input("Type the line that you wanna play: "))
    movec = int(input("Type the collumn that you wanna play: "))
    # checando a validade da jogada #
    if movel < 0 or movel > 2 or movec < 0 or movec > 2:
        print ("Invalid move, try again!")
    elif type(board[movel][movec]) == str:
        print ("Invalid move, try again!")
    else:
        board[movel][movec] = (caracter)
        jogada = jogada + 1
        collumn1 = (board[0][0]), (board[1][0]), (board[2][0])
        collumn2 = (board[0][1]), (board[1][1]), (board[2][1])
        collumn3 = (board[0][2]), (board[1][2]), (board[2][2])
        diagonal1 = (board[0][0]), (board[1][1]), (board[2][2])
        diagonal2 = (board[0][2]), (board[1][1]), (board[2][0])

        print (board[0])
        print (board[1])
        print (board[2])

    









    

    

     
   



