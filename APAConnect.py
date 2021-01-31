import tkinter
import psycopg2
import APA

def setup():
    name = "TestName"
        #enter name of file here
    time = 65137085
        #in milliseconds
    #default value for type is reminder (r)

    return name, time

def connectToPostgres_new():
    try: 
        conn = psycopg2.connect(database="APA", user="postgres", password="He4rty6452!", host="localhost")
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    name, time = setup()

    cur.execute("CREATE TABLE APATable (Name character(50), Time int, Type char)")
    cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (%s, %s, %s)", (name, time, 'r'))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    connectToPostgres_new()
