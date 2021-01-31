import tkinter as tk
import sqlite3
import datetime as dt

import APAManager

#YYYY-MM-DD hh:mm:ss

#connecting to existing data and altering
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
        cur.execute("CREATE TABLE IF NOT EXISTS APATable (Name character(50), ID int, Time timestamp, Snooze integer, Type char)")
        cur.execute("SELECT * FROM APATable WHERE ID=(SELECT max(ID) FROM APATable)")
        row = cur.fetchone()
        if (row != None):
            ID = cur.fetchone() + 1
        else:
            ID = 0
        cur.execute("INSERT INTO APATable (Name, ID, Time, Type, Snooze) VALUES (?, ?, ?, ?, ?)", (name, ID, time, snooze, 'r'))
        print("New data has been pushed to table!")
        
    else:
        cur.execute("SELECT Time in APATable where Name is equal to (?)", (ID))
        row = cur.fetchone()

        nameCur = row[0]
        IDCur = row[1]
        timeCur = row[2]
        typeCur = row[3]
        snoozeCur = row[4]

        if (name != nameCur):
            cur.execute("UPDATE APATable SET Name = (?) WHERE ID = (?)", (name, ID))
        if (time != timeCur):
            cur.execute("UPDATE APATable SET Time = (?) WHERE ID = (?)", (time, IDCur))
        #if (typeCur != 'r'):
            #cur.execute("UPDATE APATable SET NAME = (?) WHERE ID = (?)", (, IDCur)) 
        #what to do about file types?
        if (snooze != snoozeCur):
            cur.execute("UPDATE APATable SET Snooze = (?) WHERE ID = (?)", (snooze, IDCur))

        #f = '%Y-%m-%d %H:%M:%S' #timestamp format

        #dt.datetime.strptime(timeVal, f)

        print("Data altercation is complete.")

    #if timeCur == (typeVal[14:15] + snooze)
        #typeValTemp = 'f' #force on window

        #cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))
        #different executions depending on context

    #should certain commands indicate to go back to APAManager and trigger something?

    cur.close()
    conn.close()
