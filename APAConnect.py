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
        return False
    cur = conn.cursor()

    success = False

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
            return True
        except: 
            print("Can't push to table, please try again.")
            cur.close()
            conn.close()
            return False
        
    else:
        cur.execute("SELECT Time in APATable where Name is equal to (?)", (ID))
        conn.commit()
        row = cur.fetchone()

        nameCur = row[0]
        IDCur = row[1]
        timeCur = row[2]
        snoozeCur = row[4]

        if (name != nameCur):
            try:
                cur.execute("UPDATE APATable SET Name = (?) WHERE ID = (?)", (name, ID))
                conn.commit()
                print("Change sucessfully made.")
                success = True
            except:
                print("Change failed.")
                cur.close()
                conn.close()
                return False
        if (time != timeCur):
            try:
                cur.execute("UPDATE APATable SET Time = (?) WHERE ID = (?)", (time, IDCur))
                conn.commit()
                print("Change sucessfully made.")
                success = True
            except:
                print("Change failed.")
                cur.close()
                conn.close()
                return False
        if (snooze != snoozeCur):
            try:
                cur.execute("UPDATE APATable SET Snooze = (?) WHERE ID = (?)", (snooze, IDCur))
                conn.commit()
                print("Change sucessfully made.")
                success = True
            except:
                print("Change failed.")
                cur.close()
                conn.close()
                return False
        print("Data altercation is complete.")

        #f = '%Y-%m-%d %H:%M:%S' #timestamp format
        #dt.datetime.strptime(timeVal, f)
    cur.close()
    conn.close()
    return success

def PrintTable(ID):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
        return False
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
    return True

def deleteRow(name):
    try: 
        conn = sqlite3.connect('APADatabase.db')
        print("Connected!")
    except:
        print("Cannot connect to database.")
        return False
    cur = conn.cursor()

    try:
        cur.execute("UPDATE APATable DROP ROWS WHERE Name = (?)", (name))
        conn.commit()
        cur.execture("delete from APATable where Time < NOW()")
        conn.commit()
    except:
        print("Uh oh, deletion check failed.")
        cur.close()
        conn.close()
        return False

    cur.close()
    conn.close()