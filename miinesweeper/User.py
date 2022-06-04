import csv
import os

class UserConfig():
    def __init__(self):
        pass

    def login(self):
        User = input("Enter Your UserName: ")
        Pass = input("Enter Your Password: ")
        if(User != '' and Pass != ''):
            result = Filemanage.check_user(User,Pass)
            return result
        else:
            print()
            print('Please do not leave a field blank') 
            Config.login()

    def register(self):
        User = input("Enter Your UserName: ")
        if(Filemanage.check_username(User) == 0):
            print('Username already registered in the system Please enter another name')
            Config.register()
        else:
            Pass = input("Enter Your Password: ")
            if(len(Pass) >= 4):
                RepPass = input("Enter Your RepPassword: ")
                if(RepPass == Pass):
                    if(User != '' and Pass != ''):
                        return Filemanage.add_newuser(User,Pass)
                    else:
                        print('Please do not leave a field blank')
                        print()
                        Config.register()
                else:
                    print('Repeating the password is different from the original password!')
                    print()
                    Config.register()
            else:
                print('Password can not be less than 4 letters')
                print()
                Config.register()
            
    def show_user_data(self,User):
        return Filemanage.return_userdata(User)

    def save_score(self,User,Score):
        return Filemanage.save_score(User,Score)

    def show_scoreboard(self,Top,Print):
        List = Filemanage.return_scoreboard(Top)
        if(Print):
            Filemanage.print_scoreboard(List)
        return List

class FileManage():
    def __init__(self,TopCount):
        self.TopCount = TopCount

    def create_folder(self,path):
        try:
            if os.path.isdir(path) == False:
                os.mkdir(path)
        except:
            pass

    def read_datafile(self,Normal):
        Filemanage.create_folder('./Files')
        try:
            file = open('./Files/UserData.txt','r')
            if(Normal):
                return file
            else:
                return csv.reader(file,delimiter=':')
        except:
            open('./Files/UserData.txt','w')
            return None

    def open_forwrite(self):
        return open('./Files/UserData.txt','w')

    def check_user(self,User,Pass):
        file = Filemanage.read_datafile(False)
        if(file != None):
            result = 1
            for i in file:
                userfound = ("".join(i[:1]).strip())
                passfound =  ("".join(i[1:2]).strip())
                if(User == userfound and Pass == passfound):
                    result = User # login success
                    break
                else:
                    result = 1 # login faile
            return result
        else:
            return None

    def check_username(self,User):
        file = Filemanage.read_datafile(False)
        if(file != None):
            result = 1
            for i in file:
                userfound = ("".join(i[:1]).strip())
                if(User == userfound):
                    result = 0 # user found
                    break
                else:
                    result = 1 # user not found
            return result
        else:
            return None

    def add_newuser(self,User,Pass):
        oldfile = Filemanage.read_datafile(True).read()
        file = Filemanage.open_forwrite()
        try:
            file.write(oldfile)
        except:
            pass
        file.write('\n')
        file.write(f'{User}:{Pass}:0')
        file.close()
        return User

    def save_score(self,User,Score):
        file = Filemanage.read_datafile(True).read()
        csvfile = Filemanage.read_datafile(False)
        if(file != None):
            for i in csvfile:
                if(User == ("".join(i[:1]).strip())):
                    oldscore = int(("".join(i[2:]).strip()))
                    Pass = ("".join(i[1:2]).strip())
                    oldline = f'{User}:{Pass}:{oldscore}'
                    newline = f'{User}:{Pass}:{oldscore + Score}'
                    newfile = file.replace(oldline,newline)
                    oldfile = Filemanage.open_forwrite()
                    oldfile.write(newfile)
                    oldfile.close()
                    return oldscore + Score
        else:
            return None

    def return_userdata(self,User):
        file = Filemanage.read_datafile(False)
        if(file != None):
            for i in file:
                if(User == ("".join(i[:1]).strip())):
                    return f'User: {User}  Score: {("".join(i[2:]).strip())}'
        else:
            return None

    def return_scoreboard(self,Top):
        file = Filemanage.read_datafile(False)
        allData,Data =[],[]
        count = 0
        if(file != None):
            for i in file:
                if(Top == False):
                    Data.append(f'{("".join(i[:1]).strip())}')
                    Data.append(f'{("".join(i[2:]).strip())}')
                    allData.append(Data)
                    Data = []
                else:
                    if(count < self.TopCount):
                        Data.append(f'{("".join(i[:1]).strip())}')
                        Data.append(f'{("".join(i[2:]).strip())}')
                        allData.append(Data)
                        Data = []
                        count+=1
                    else:
                        break
            return Filemanage.sort_list(allData)

    def sort_list(self,List):
        temp = []
        up=[List[0]]
        cv,cc=0,0
        while(True):
            try:
                if(List[cv][1] > up[0][1]):
                    up[0] = List[cv]
                    cc = cv
                cv+=1
            except:
                temp.append(up[0])
                try:
                    del List[cc]
                    up[0] = List[0]
                except:
                    break
                cv,cc=0,0
        return temp

    def print_scoreboard(self,List):
        print('Rank  |  UserName  |  Score')
        for i in range(0,len(List)):
            print(f'{i+1}      {List[i][0]}     {List[i][1]}')

Filemanage = FileManage(10)
Config = UserConfig()
