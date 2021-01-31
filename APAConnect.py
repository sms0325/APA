import tkinter
import sqlite3
#import APA

def setup():
    name = "TestName"
        #enter name of file here
    time = 65137085
        #in milliseconds
    #default value for type is reminder (r)

    return name, time

def connectToSQLite_new():
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    name, time = setup()

    #cur.execute("CREATE TABLE APATable (Name character(100), Time int, Type char)")
    cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    connectToSQLite_new()
