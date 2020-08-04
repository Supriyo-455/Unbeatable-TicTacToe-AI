import pygame
import sys
import random
import math

pygame.init()

width = 600
height = 600
w = width//3

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

offset = 40

class MainGame():

    def __init__(self):

        self.board = [['','',''],['','',''],['','','']]
        self.human = 'O'
        self.AI = 'X'
        self.currentPlayer = self.AI

    def CheckWinner(self):

        #For row wise and column wise check
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '':
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '':
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '':
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '':
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '':
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '':
            return True
        #For diagonal check
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != '':
            return True

        return False

    def Winner(self):

        #For row wise and column wise check
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '':
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '':
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '':
            return self.board[2][0]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '':
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '':
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '':
            return self.board[0][2]
        #For diagonal check
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != '':
            return self.board[2][0]

        c = 0
        for i in self.board:
            if '' not in i:
                c += 1
        if c>2:
            return 'tie'
            
        else:
            return None


    def BoardFullCheck(self):

        if self.CheckWinner():
            print(self.currentPlayer+' is the winner!')
            pygame.display.set_caption(self.currentPlayer+' is the winner!')
            return False
        else:
            c = 0
            for i in self.board:
                if '' not in i:
                   c += 1
            if c>2:
                print("Game tied!")
                pygame.display.set_caption('Game tied!')
                return False
            
            else:
                return True

    def CheckSpace(self, i, j):

        if self.board[i][j] == '':
            return True
        return False

    def minimax(self, depth, isMaximizing):
        
        result = self.Winner()
        if result != None:
            if result == 'X':
                return 10
            elif result == 'O':
                return -10
            else:
                return 0

        if isMaximizing:
            bestScore = -math.inf
            for i in range(0,3):
                for j in range(0,3):
                    #Is the spot available
                    if(self.board[i][j] == ''):
                        self.board[i][j] = self.AI
                        score = self.minimax(depth+1, False)
                        self.board[i][j] = ''
                        bestScore = max(score, bestScore)
            return bestScore

        if not isMaximizing:
            bestScore = math.inf
            for i in range(0,3):
                for j in range(0,3):
                    #Is the spot available
                    if(self.board[i][j] == ''):
                        self.board[i][j] = self.human
                        score = self.minimax(depth+1, True)
                        self.board[i][j] = ''
                        bestScore = min(score, bestScore)
            return bestScore


    def BestMove(self):
        bestScore = -math.inf
        bestMove = None
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '':
                    self.board[i][j] = self.AI
                    s = self.minimax(0, False)
                    self.board[i][j] = ''
                    if s > bestScore:
                        bestScore = s
                        bestMove = [i,j].copy()
        
        self.board[bestMove[0]][bestMove[1]] = self.AI
         

    def checkMouseEvent(self):
        
        if self.currentPlayer == self.human:
            mouseLocation = pygame.mouse.get_pos()

            i = mouseLocation[0]//w
            j = mouseLocation[1]//w

            if pygame.mouse.get_pressed() == (1,0,0):
                if self.CheckSpace(i,j):
                    self.board[i][j] = self.human
                    if self.BoardFullCheck():
                        self.currentPlayer = self.AI

        elif self.currentPlayer == self.AI:
            self.BestMove()
            if self.BoardFullCheck():
                self.currentPlayer = self.human


                    
    def display(self):

        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == 'X':
                    pygame.draw.line(screen, (0,0,255), ((w*i)+offset,(w*j)+offset), ((w*(i+1))-offset,(w*(j+1))-offset), 10)
                    pygame.draw.line(screen, (0,0,255), ((w*i)+offset,(w*(j+1))-offset), ((w*(i+1))-offset,(w*j)+offset), 10)
                elif self.board[i][j] == 'O':
                    cx = (w*i+(w*(i+1)))//2
                    cy = (w*j+(w*(j+1)))//2
                    pygame.draw.circle(screen, (255,0,0), (cx,cy), w//4, 8)
                
              
Game = MainGame()
    
while True:

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    for i in range(0,2):
        pygame.draw.line(screen, (255,255,255), (0, w*(i+1)), (width, w*(i+1)), 5)
        pygame.draw.line(screen, (255,255,255), (w*(i+1), 0), (w*(i+1), height), 5)

    if Game.BoardFullCheck():
        Game.checkMouseEvent()

    Game.display()
    pygame.display.update()
