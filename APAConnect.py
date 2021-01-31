import tkinter
import psycopg2
import APA

def setup():
    name = 
        #enter name of file here
    time =
        #in milliseconds
    #default value for type is reminder (r)

    return name, time

def connectToPostgres():
    try: 
        conn = psycopg2.connect(database="APA", user="postgres", password="He4rty6452!", host="localhost")
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    name, time = setup()

    cur.execute("INSERT INTO APADatabaseTable (name, time, type) VALUES (%s, %s, %s)", (name, time, 'r'))

    conn.commit()

    cur.close()
    conn.close()

