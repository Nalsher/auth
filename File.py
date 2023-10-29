import psycopg2
from config import host,user,password,db_name


class Connect:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
    def Connected(self):
        self.connection = psycopg2.connect(host = self.host,user = self.user,password = self.password,database = self.db_name)
        self.connection.autocommit = True
        return self.connection
    def cursor_execute(self,command):
        self.cursor = self.Connected().cursor()
        return self.cursor.execute(command)
    def cursor_fetchone(self,command):
        self.cursor = self.Connected().cursor()
        self.cursor.execute(command)
        return self.cursor.fetchone()
    def close(self):
        self.cursor.close()
        self.connection.close()
class User:
    def __init__(self,Name,login1='',password1=''):
        self.log = login1
        self.pas = password1
        self.Name = Name
    @property
    def Login(self):
        print(self.log)
    def Reg(self):
        Con = Connect()
        Con.Connected()
        
        def LoginSet(self):
            print("Введите логин")
            login = input()
            self.log = login
        LoginSet(self)

        def PassSet(self):
            print("Введите пароль")
            passwords = input()
            self.pas = passwords
            if len(self.pas) <= 6:
                raise ValueError('Bad pass')
                exit()
        PassSet(self)

        def Testing(self):
            if self.pas == self.log:
                raise ValueError('Pass shoudl != Login')
                exit()
        Testing(self)
        cursor = Con.cursor_execute(f"""INSERT INTO auth(login,password) VALUES ('{self.log}','{self.pas}')""")
        Con.close()
        
    def Login(self):
        Con = Connect()
        Con.Connected()
        name = input("Введите логин \n")
        pas = input("Введите пароль\n")
        passwrd = Con.cursor_fetchone(f"""SELECT password FROM auth WHERE login = '{name}'""")[0]
        if passwrd == pas:
            print(f"Вход выполнен,Добро пожаловать {self.Name}")
        else:
            print(False)
        Con.close()


