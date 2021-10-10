import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='Abdulaziz',
    password='123123123',
)

mycursor = my_db.cursor()


class Project:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None

    def register(self):
        pass

    def log_in(self):
        pass

    def update_login_and_password(self):
        pass
    
    def log_out(self):
        pass

    def delete_profile(self):
        pass

