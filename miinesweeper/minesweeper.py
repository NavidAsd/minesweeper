from random import randint
from User import Config
import os

char,aout ='*','-'

class MineSwp():
    def __init__(self,User,Flag_state,Flag_limit,Flag_removeState):
        self.User = User
        self.Flag_state = Flag_state
        self.Flag_limit = Flag_limit
        self.Flag_removeState=Flag_removeState

    def base_grid(self,n,k):

        """create the background grid as the basic str of the game"""

        map=[[0 for row in range(n)] for column in range(n)]
        
        self.add_bombs(map,n,k)
        return map
        

    def print_grid(self,map):

        """ prints the grids """

        for row in map:
            for cell in row:
                if cell == 0:
                    print(aout , end = "   ")
                else:
                    print(cell, end = '   ')
            print()
            print()
            

    def add_bombs(self,map,n, k = 10):

        """
        add bombs randomly in the grid accoring to percentage.
        05% easy
        10% medium 
        15% hard 
        20% very hard
        """
        for column in range(n):
            for row in range(n):
                if randint(1,100) < k:
                    map[row][column] = "X"
                    Game.number(row,column,n,map)
        

    def number(self,x,y,n,arr):
        
        """increment numbers around the bomb"""

        if y > 0:
            if arr[x][y-1] != "X":
                arr[x][y-1] += 1 #centre right
        if y < (n-1):
            if arr[x][y+1] != "X":
                arr[x][y+1] += 1 #centre right
    
        if x < (n-1) and  y < (n-1):
            if arr[x+1][y+1] != "X" :
                arr[x+1][y+1] += 1 #bottom right
        if x < (n-1) and y > 0:
            if arr[x+1][y-1] != "X":
                arr[x+1][y-1] += 1 #bottom left 
        if  x < (n-1) :
            if arr[x+1][y] !="X":
                arr[x+1][y] += 1 #bottom centre
    
        if x > 0 and y < (n-1):
            if arr[x-1][y+1] != "X":
                arr[x-1][y+1] += 1 #top right
        if  x > 0 and y > 0:
            if arr[x-1][y-1] != 'X':
                arr[x-1][y-1] += 1 #top left
        if x > 0 :
            if arr[x-1][y] != 'X':
                arr[x-1][y] += 1 #top centre

    #game_start___________________________________________________________________________________________
    def player_grid(self,n):
        map=[[char for row in range(n)] for column in range(n)]
        return map

    def cont_game(self,n,score):
        print('your score is :', score,"/", n*n,'!!')
        totalScore = Config.save_score(self.User,int(score))
        print(f'TotalScore: {totalScore}')
        again = input("\n\nWant to play again (y/n) ? : ")
        if again == "y":
            Game.game()
        else:
            input('press any key to quit')

    def check_won(self,n,map):
        for column in range(n):
            for row in range(n):
                if map[row][column] == char:
                    return False
        return True

    def flag_count(self,n,map):
        count=0
        for column in range(n):
            for row in range(n):
                if map[row][column] == 'f':
                    count+=1
        return count

    def get_x(self,n,map):
        while True:
            print()
            if(self.Flag_state):
                print('[Flag Mode]')
                print('Enter the cell u want to flag :' )
                print ("Enter value X and Y (1 to",n,")")
                print('Enter 99 to open or 97 to remove flag')
            elif(self.Flag_removeState):
                print('[Remove Flag Mode]')
                print('Enter the cell u want to flag :' )
                print ("Enter value X and Y (1 to",n,")")
                print('Enter 99 to open or 98 to flag')
            else:
                print('Enter the cell u want to open :' )
                print ("Enter value X and Y (1 to",n,")")
                print('Enter 98 to flag or 97 to remove flag')
            try:
                x = int(input("X : "))
                y=0
                if(x == 98):
                    if(self.Flag_limit > Game.flag_count(n,map)):
                        self.Flag_state = True
                        self.Flag_removeState = False
                    else:
                        print('You can not add more flags')
                    Game.get_x(n,map)
                elif (x == 99):
                    self.Flag_state = False
                    self.Flag_removeState=False
                    Game.get_x(n,map)
                elif(x == 97):
                    self.Flag_state=False
                    self.Flag_removeState =True
                    Game.get_x(n,map)
                else:
                    x -= 1
                    y = Game.get_y(n,map)
            except:
                print()
                print('Please enter the value in the defined range')
                Game.get_x(n,map)
            return x,y
        

    def get_y(self,n,map):
        while True:
            try:
                y = int(input("Y : "))
                if(y == 98):
                    self.Flag_state = True
                    self.Flag_removeState = False
                    Game.get_x(n,map)
                elif (y == 99):
                    self.Flag_state = False
                    self.Flag_removeState = False
                    Game.get_x(n,map)
                elif(y == 97):
                    self.Flag_state=False
                    self.Flag_removeState =True
                    Game.get_x(n,map)
                else:
                    y -= 1
            except:
                print()
                print('Please enter the value in the defined range')
                Game.get_y(n,map)
            return y

    def check_x(self,n,loc,map):
        if loc[0] == 98 or loc[0] == 99 or loc[0] == 97:
            print()
            print('"Please enter the coordinates again"')
            return Game.get_x(n,map)
        elif loc[1] == 98 or loc[1] == 99 or loc[1] == 97:
            print()
            print('"Please enter the coordinates again"')
            return Game.get_x(n,map)
        else:
            return loc


    def game(self,n,k):
        Game_status = True
        while Game_status:
            mine_map=Game.base_grid(n,k)
            player_map=Game.player_grid(n)
            score = 0
            Game.print_grid(player_map)
            while True:
                if Game.check_won(n,player_map)==False:
                    location = Game.check_x(n,Game.get_x(n,player_map),player_map)
                    x = location[0]
                    y = location[1]
                    if(self.Flag_state):
                        if(player_map[x][y] == "X" or player_map[x][y] == char):
                            os.system("cls")
                            player_map[x][y] = 'f'
                            Game.print_grid(player_map)
                        else:
                            Game.print_grid(player_map)
                    elif(self.Flag_removeState):
                        if(player_map[x][y] == "f"):
                            os.system("cls")
                            player_map[x][y] = char
                            Game.print_grid(player_map)
                        else:
                            Game.print_grid(player_map)
                    else:
                        try:
                            if mine_map[x][y] == "X" and player_map[x][y] != 'f':
                                os.system("cls")
                                print("Game Over :(")
                                Game.print_grid(mine_map)
                                Game_status = Game.cont_game(n,score)
                                break
                            elif player_map[x][y] == 'f':
                                Game.print_grid(player_map)
                            else:
                                os.system("cls")
                                player_map[x][y] = mine_map[x][y]
                                score += 1
                                Game.print_grid(player_map)
                        except:
                            print()
                            print('Please enter the value in the defined range')
                else:
                    os.system("cls")
                    Game.print_grid(player_map)
                    print("\nYou have Won!!")
                    GameStatus = Game.cont_game(n,score)
                    break

    def grid_size(self):
        print("GRID SIZE AVAILABE \n1. 10x10 \n2. 15x15 \n3. 25x25 \n4. Exit")
        grid= int(input('\nChoose grid size : '))
        if grid == 1:
            n = 10
        elif grid == 2:
            n = 15
        elif grid == 3:
            n = 25
        elif grid == 4:
            print('Exit..')
            exit()
        else:
            print('Choosen option unavailable. TIP: CHOOSE CORRECTLY !')
            Game.grid_size()
        return n

    def difficulty(self):
        print("DIFICULTY LEVELS AVAILABLE \n1. Easy \n2. Medium \n3. Hard \n4. Very Hard \n5. Exit")
        
        diff= int(input('\nChoose grid size (1/2/3/4) : '))
        if diff == 1:
            k = 5
        elif diff == 2:
            k = 10
        elif diff == 3:
            k = 15
        elif diff == 4:
            k = 20
        elif diff == 5:
           print('Exit..')
           exit()
        else:
            print('Choosen option unavailable. TIP: CHOOSE CORRECTLY !')
            Game.difficulty()
        return k
    #game_end_____________________________________________________________________________________________
    
    def start_game(self,User):
        self.User=User
        print("Welcome to MineSweeper \n")
        n = Game.grid_size()
        print()
        k = Game.difficulty()
        os.system("cls")
        Game.game(n,k) 
        

Game = MineSwp('',False,7,False)
