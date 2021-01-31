import tkinter as tk
import sqlite3
import datetime as dt

import APAManager

#YYYY-MM-DD hh:mm:ss

#ID value not contained: entering new data
#ID value contained: altering existing data
def connectToSQLite(name, time, snooze, ID = -1): 
    new = True
    if (ID != -1):
        new = False
    
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    if (new):
        cur.execute("CREATE TABLE IF NOT EXISTS APATable (Name character(50), ID int, Time timestamp, Snooze integer)")
        cur.execute("SELECT * FROM APATable WHERE ID=(SELECT max(ID) FROM APATable)")
        row = cur.fetchone()
        if (row != None):
            ID = cur.fetchone() + 1
        else:
            ID = 0
        
        try:
            cur.execute("INSERT INTO APATable (Name, ID, Time, Snooze) VALUES (?, ?, ?, ?)", (name, ID, time, snooze))
            conn.commit()
            print("New data has been pushed to table!")
        except: 
            print("Can't push to table, please try again.")
        
    else:
        cur.execute("SELECT Time in APATable where Name is equal to (?)", (ID))
        conn.commit()
        row = cur.fetchone()

        nameCur = row[0]
        IDCur = row[1]
        timeCur = row[2]
        snoozeCur = row[4]

        if (name != nameCur):
            cur.execute("UPDATE APATable SET Name = (?) WHERE ID = (?)", (name, ID))
            conn.commit()
        if (time != timeCur):
            cur.execute("UPDATE APATable SET Time = (?) WHERE ID = (?)", (time, IDCur))
            conn.commit()
        if (snooze != snoozeCur):
            cur.execute("UPDATE APATable SET Snooze = (?) WHERE ID = (?)", (snooze, IDCur))
            conn.commit()

        #f = '%Y-%m-%d %H:%M:%S' #timestamp format

        #dt.datetime.strptime(timeVal, f)

        print("Data altercation is complete.")

    #should certain commands indicate to go back to APAManager and trigger something?

    cur.close()
    conn.close()

def PrintTable(ID):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    cur.execute("SELECT * FROM APATable")
    conn.commit()

    cur.execute("SELECT Time FROM APATable where Name is equal to (?)", (ID))
    conn.commit()
    row = cur.fetchall()

    print("Displaying all tasks in the table")
    for i in row:
        nameCur = row[0 + i]
        IDCur = row[1 + i]
        timeCur = row[2 + i]
        snoozeCur = row[4 + i]
        print("Data for row " + IDCur + ": Name: " + nameCur + ", Time of reminder: " + timeCur + ", Snooze time set: " + snoozeCur)
        print("----------")

    cur.close()
    conn.close()

def deleteRow(name):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
    cur = conn.cursor()

    cur.execute("UPDATE APATable DROP ROWS WHERE Name = (?)", (name))
    conn.commit()

    cur.execture("delete from APATable where Time < NOW()")
    conn.commit()

    cur.close()
    conn.close()