import psycopg2
from config import host,user,password,db_name

class User:
    def __init__(self,login1='',password1=''):
        self.log = login1
        self.pas = password1
    @property
    def Login(self):
        print(self.log)
    def Auth(self):
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        cursor = connection.cursor()
        def LoginSet(self):
            print("Введите логин")
            login = input()
            self.log = login
            try:
                cursor.execute(f"""SELECT COUNT(*) from auth WHERE login = '{self.log}'""")
                a = cursor.fetchone()[0]
                if a != 0:
                    exit()
            except:
                    raise ValueError('Логин занят')
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
        cursor.execute(
            f"""INSERT INTO auth(login,password) VALUES ('{self.log}','{self.pas}')""")
        cursor.close()
        connection.close()

Vlad = User()
Vlad.Auth()
