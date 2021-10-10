import mysql.connector
import os

my_db = mysql.connector.connect(
    host='localhost',
    user='Abdulaziz',
    password='123123123',
    database='login_password'
)

mycursor = my_db.cursor()


class Project:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None

    def enterance(self):
        self.clear_everything()
        self.first_msg()
        enter_ = input(">>> ").strip()
        options = ['1','2','3','4']

        while enter_ not in options:
            self.clear_everything()
            print("Invalid input. You can only enter [1,2,3,4] ")
            enter_ = input(">>> ").strip()

        if enter_ == options[0]:
            self.register()
        elif enter_ == options[1]:
            self.log_in()
        elif enter_ == options[2]:
            self.log_out()
        else:
            self.delete_profile()

    def register(self):
        self.clear_everything()
        us_name = input("Enter you name: ").strip().capitalize()
        while not us_name.isalpha() or self.is_empty(us_name):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
            -> Entered something other than letters
            -> An empty input""")
            us_name = input("Enter you name: ").strip().capitalize()

        us_age = input("Enter your age: ").strip()
        while not us_age.isnumeric() or self.is_empty(us_age):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                        -> Entered something other than numbers
                        -> An empty input""")
            us_age = input("Enter your age: ").strip()

        us_log = input("Enter your login: ").strip().lower()
        while not us_log.isalnum() or self.is_empty(us_log):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                                    -> Entered something other than leters and numbers
                                    -> An empty input""")
            us_log = input("Enter your login: ").strip().lower()

        us_password = input("Enter your password: ").strip()
        while not us_password.isalnum() or self.is_empty(us_password):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                                                -> Entered something other than leters and numbers
                                                -> An empty input""")
            us_password = input("Enter your password: ").strip()

        self.name = us_name
        self.age = us_age
        self.login = us_log
        self.password = us_password
        self.save_to_database()
        self.enterance()

    def log_in(self):
        pass

    def update_login_and_password(self):
        pass

    def log_out(self):
        pass

    def delete_profile(self):
        pass

    @staticmethod
    def clear_everything():
        os.system("clear")

    @staticmethod
    def first_msg():
        print("""
        Welcome!
    
    What do you want to do:
    [1] -> Register 
    [2] -> Log in
    [3] -> Log out
    [4] -> Delete profile""")

    def is_empty(self, str_):
        return not bool(str_)


    def save_to_database(self):
        mycursor.execute(f"insert into logn__pasword (name, age, login, password) values ('{self.name}','{self.age}','{self.login}','{self.password}')")
        my_db.commit()


person = Project()
person.enterance()