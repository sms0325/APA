import tkinter
import sqlite3
import APAMAnager

def connectToSQLite_new(name, time):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    cur.execute("CREATE TABLE APATable (Name character(100), Time timestamp, Type char)")
    cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))

    conn.commit()
    cur.close()
    conn.close()

def connectToSQLite(name, time, type):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    cur.close()
    conn.close()

if __name__ == "__main__":
    connectToSQLite_new()
