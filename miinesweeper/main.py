from minesweeper import MineSwp
from User import Config
from time import sleep
import os

class Main():
    def __init__(self,User,Login):
        self.User=User
        self.Login=Login

    def items(self):
        print()
        print(""" 
You have a playground where there are square houses. Some of these houses have bombs.
You must clear all surfaces without encountering mines
Good luck.
        """)
        print('1. Full ScoreBoard')
        print('2. Top ScoreBoard')
        print('3. Login')
        print('4. Sign up')
        print('0. Exit')

    def game_item(self):
        print(Config.show_user_data(self.User))
        print()
        print('1. Start Game')
        print('2. Back')

    def menu(self):
        os.system('cls')
        Start.items()
        try:
            choose = int(input('Enter Your Choose: '))
            if(choose == 1):
                os.system('cls')
                Config.show_scoreboard(False,True)
                input('press any key to continue')
                Start.menu()
            elif(choose == 2):
                os.system('cls')
                Config.show_scoreboard(True,True)
                input('press any key to continue')
                Start.menu()
            elif(choose == 3):
                os.system('cls')
                result = Config.login()
                if(result != 1 and result != None):
                    self.User = result
                    self.Login = True 
                    Start.game_menu()# go to game manu
                else:
                    self.User=''
                    self.Login = False
                    print('The username or password entered is incorrect')
                    sleep(2)
                    Start.menu()
            elif(choose == 4):
                os.system('cls')
                result = Config.register()
                if(result != None):
                    print('Your account was created successfully')
                    input('press any key to continue')
                    self.User = result
                    self.Login = True
                    Start.game_menu()# go to game manu
                else:
                    self.User=''
                    self.Login = False
                    print('There was a problem recording the information')
                    sleep(2)
                    Start.menu()
            elif(choose == 0):
                print('Exit..')
                exit()
            else:
                print('Please enter only one of the defined items')
                sleep(2)
                Start.menu()    
        except:
            print('Please enter only one of the defined items')
            sleep(2)
            Start.menu()

    def game_menu(self):
        if(self.Login):
            os.system('cls')
            Start.game_item()
            try:
                choose = int(input('Enter Your Choose: '))
                if(choose == 1):
                    MineSwp.start_game(MineSwp,self.User)
                    Start.game_menu()
                elif(choose == 2):
                    Start.menu()
                else:
                    print('Please enter only one of the defined items')
                    sleep(2)
                    Start.game_menu()
            except:
                print('Please enter only one of the defined items')
                sleep(2)
                Start.game_menu()
        else:
            Start.menu()


Start = Main('',False)
Start.menu()