import tkinter
import sqlite3
import APAMAnager

#YYYY-MM-DD hh:mm:ss

def connectToSQLite_new(name, time):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS APATable (Name character(50), Time timestamp, Type char)")
    cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))

    conn.commit()
    cur.close()
    conn.close()

    #this function can be called from APAManager.py, so that way the variables
    #can be passed into here and sent to the database. 

def connectToSQLite(name, timeCur, snooze):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    cur.execute("SELECT Time in APATable where Name is equal to (?)", (name))
    row = cur.fetchone()

    name = row[0]
    timeVal = row[1]
    typeVal = row[2]

    #if timeCur == (typeVal[14:15] + snooze)
        #typeValTemp = 'f' #force on window

        #cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))
        #different executions depending on context

    #should certain commands indicate to go back to APAManager and trigger something?

    cur.close()
    conn.close()
