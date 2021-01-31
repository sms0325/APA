import tkinter as tk
import sqlite3
import datetime as dt

import APAManager

#YYYY-MM-DD hh:mm:ss

# def connectToSQLite_new(name, timeCur, snooze):
#     try: 
#         conn = sqlite3.connect('APADatabase.db')
#         print("Connected!")
#     except:
#         print("Cannot connect to database.")
#     cur = conn.cursor()

#     cur.execute("CREATE TABLE IF NOT EXISTS APATable (Name character(50), ID integer, Time timestamp, Snooze integer, Type char)")
#     ID = 
#     cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?, ?, ?)", (name, ID, timeCur, snooze, 'r'))

#     conn.commit()
#     cur.close()
#     conn.close()

#     #this function can be called from APAManager.py, so that way the variables
#     #can be passed into here and sent to the database. 

#connecting to existing data and altering
def connectToSQLite(name, timeCur, snooze, ID = -1): 
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
        cur.execute("SELECT TOP 1 * FROM APATable ORDER BY ID DESC")
        row = cur.fetchone()
        ID = row[0] + 1
        cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?, ?, ?)", (name, ID, timeCur, snooze, 'r'))
        
    else:
        cur.execute("SELECT Time in APATable where Name is equal to (?)", (name))
        row = cur.fetchone()

        name = row[0]
        timeVal = row[1]
        print(timeVal)
        typeVal = row[2]

        f = '%Y-%m-%d %H:%M:%S' #timestamp format

        dt.datetime.strptime(timeVal, f)

    #if timeCur == (typeVal[14:15] + snooze)
        #typeValTemp = 'f' #force on window

        #cur.execute("INSERT INTO APATable (Name, Time, Type) VALUES (?, ?, ?)", (name, time, 'r'))
        #different executions depending on context

    #should certain commands indicate to go back to APAManager and trigger something?

    cur.close()
    conn.close()
