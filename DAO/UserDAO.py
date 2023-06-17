from entities.SchoolClass import SchoolClass
import psycopg2
import traceback

from entities.User import User


class UserDAO:
    def __init__(self):
        self.USER = "postgres"
        self.PASSWORD = "Jv4984538171"
        self.HOST = "127.0.0.1"
        self.PORT = "5432"
        self.DATABASE = "portuno"

    def openConnection(self):
        return psycopg2.connect(user=self.USER, password=self.PASSWORD,
                                host=self.HOST, port=self.PORT, database=self.DATABASE)

def insertUser(user):
    try:
        connection = UserDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO usuario (id, name, password, ddd, number) "
                       f"VALUES ('{user.id}', '{user.name}', '{user.password}', '{user.ddd}', '{user.number}')")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def getOneUser(id):
    user = None
    try:
        connection = UserDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuario WHERE id = '{id}'")
        register = cursor.fetchone()
        if register:
            user = User(register[0], register[1], register[2], register[4], register[5])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return user

def getAllUsers():
    users = []
    try:
        connection = UserDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuario")
        registers = cursor.fetchall()
        for register in registers:
            users.append(User(register[0], register[1], register[2], register[4], register[5]))
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return users

def updateUser(id, newUser):
    try:
        connection = UserDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE usuario SET name = %s, password = %s, ddd = %s, number = %s WHERE id = %s",
                       (newUser.name, newUser.password, newUser.ddd, newUser.number, id))

        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def deleteUser(id):
    try:
        connection = UserDAO().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM usuario WHERE id= '{id}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()



