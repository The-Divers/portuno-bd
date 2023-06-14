from entities.Semester import Semester
import psycopg2
import traceback

def __openConection():
    return psycopg2.connect(user="postgres", password="Jv4984538171",
                                  host="127.0.0.1", port="5432", database="portuno")

def insertSemester(semester):
    try:
        connection = __openConection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO semester (name, beginning_date, ending_date) "
                       f"VALUES ('{semester.name}','{semester.beginning_date}', '{semester.ending_date}')")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success insert!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def getOneSemester(name):
    semester = None  # Inicializa a variável semester antes do bloco try
    try:
        connection = __openConection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM semester WHERE name = '{name}'")
        register = cursor.fetchone()
        if register:
            semester = Semester(register[0], register[1], register[2])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
        return semester

def getAllSemesters():
    semesters = []
    try:
        connection = __openConection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM semester")
        registers = cursor.fetchall()
        print(registers)
        for register in registers:
            semesters.append(Semester(register[0], register[1], register[2]))

    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()
        return registers

def updateSemester(name, newSemester):
    try:
        connection = __openConection()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE semester SET name= '{newSemester.name}', "
                       f"beginning_date='{newSemester.beginning_date}', ending_date='{newSemester.ending_date}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success update!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()

def deleteSemester(name):
    try:
        connection = __openConection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM semester WHERE name= '{name}'")
        connection.commit()
        if cursor.rowcount > 0:
            print("Success delete!")
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()



