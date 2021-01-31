#this code is here for REFERENCE ONLY

import tkinter
import psycopg2

try: 
    conn = psycopg2.connect(database="APA", user="postgres", password="***", host="localhost")
    print("Connected!")
except:
    print("Cannot connect to database.")

cur = conn.cursor()
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO APADatabaseTable (name, time) VALUES (%s, %s)", (a, b))

#not collecting time initially

print(coins) #placeholder for token variables into the server.
conn.commit()

cur.close()
conn.close()

# for the purpose of reference:
# the tutorial's app.py code:

# import models
# window = Tk()
# window.title(“Join”)
# btn=Button(window, text=”OK”, fg=’blue’)
# btn.place(x=130, y=150)
# lbl=Label(window, text=”This is Label widget”, fg=’red’, font=(“Helvetica”, 16))
# lbl.place(x=60, y=50)
# txtfld=Entry(window, text=”This is Entry Widget”, bd=5)
# txtfld.place(x=80, y=100)
# window.title(‘Hello Python’)
# window.geometry(“300x200+10+10”)
# window.mainloop()