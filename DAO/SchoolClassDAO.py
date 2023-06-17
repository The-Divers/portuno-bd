from entities.SchoolClass import SchoolClass
import psycopg2
import traceback

class SchoolClassDao:
    def __init__(self):
        self.USER = "postgres"
        self.PASSWORD = "Jv4984538171"
        self.HOST = "127.0.0.1"
        self.PORT = "5432"
        self.DATABASE = "portuno"

    def openConnection(self):
        return psycopg2.connect(user=self.USER, password=self.PASSWORD,
                                host=self.HOST, port=self.PORT, database=self.DATABASE)

def insertSchoolClass(schoolClass):
    try:
        connection = SchoolClassDao().openConnection()
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO class (id, day_week, subject) "
                       f"VALUES ('{schoolClass.id}', '{schoolClass.day_week}', '{schoolClass.subject}')")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def getOneSchoolClass(id):
    schoolClass = None
    try:
        connection = SchoolClassDao().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM class WHERE id = '{id}'")
        register = cursor.fetchone()
        if register:
            schoolClass = SchoolClass(register[0], register[1], register[2])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return schoolClass

def getAllSchoolClasses():
    schoolClasses = []
    try:
        connection = SchoolClassDao().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM class")
        registers = cursor.fetchall()
        for register in registers:
            schoolClasses.append(SchoolClass(register[0], register[1], register[2]))
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return schoolClasses

def updateSchoolClass(id, newSchoolClass):
    try:
        connection = SchoolClassDao().openConnection()
        cursor = connection.cursor()

        cursor.execute(f"UPDATE class SET "
                       f"day_week = '{newSchoolClass.day_week}', "
                       f"subject = '{newSchoolClass.subject}' "
                       f"WHERE id = '{id}'")

        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def deleteSchoolClass(id):
    try:
        connection = SchoolClassDao().openConnection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM class WHERE id= '{id}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()



