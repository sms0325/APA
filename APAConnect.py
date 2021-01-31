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

    cur.execute("CREATE TABLE IF NOT EXISTS APATable (Name character(100), Time timestamp, Type char)")
    cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))

    conn.commit()
    cur.close()
    conn.close()

    #this function can be called from APAManager.py, so that way the variables
    #can be passed into here and sent to the database. 

def connectToSQLite(name, time, type):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    #if-elif statements for different types
        #cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))
        #different executions depending on context

    #should certain commands indicate to go back to APAManager and trigger something?

    cur.close()
    conn.close()
