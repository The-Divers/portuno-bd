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
    try:
        connection = __openConection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM semester WHERE name = '{name}'")
        register = cursor.fetchone()
        print("name = ", register[0])
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
        connection.close()


