import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
#yyyy-mm-dd hh:mm:ss

def addReminderButton():
	name = nameField.get()
	time = str(timeDateField.selection_get()) + ' ' + convert12hrTo24hr(timeHourField.get(),timeMinuteField.get(),timeampmField.get())
	snooze = str(int(snoozeHourField.get()) * 60 + int(snoozeMinuteField.get()))
	print("Name:", name)
	print("Time:", time)
	print("Snooze:", snooze)

def convert12hrTo24hr(hour,minute,ampm):
	hour = int(hour)
	if (hour == 12):
		hour = 0
	if (str(ampm) == 'pm'):
		hour += 12
	if (hour < 10):
		hour = '0' + str(hour)
	return str(hour) + ':' + str(minute) + ':00'


window = tk.Tk()
window.title("Add Reminder")

# reminder name
tk.Label(window, text = "What should I remind you to do?").grid(row = 0, column = 0, columnspan = 4)
nameField = tk.Entry(window)
nameField.grid(row = 1, column = 0, columnspan = 4)

# reminder time
tk.Label(window, text = "When should I remind you?").grid(row = 2, column = 0, columnspan = 4) # epoch (ms)
timeDateField = tkc.Calendar(window)
timeDateField.grid(row = 3, column = 0, columnspan = 4)
timeHourField = ttk.Combobox(window)
timeHourField.grid(row = 4, column = 0)
timeHourField['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
timeHourField.current(11)
tk.Label(window, text = ":").grid(row = 4, column = 1)
timeMinuteField = ttk.Combobox(window)
timeMinuteField.grid(row = 4, column = 2)
timeMinuteField['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
							 '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
							 '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
							 '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
							 '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
							 '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
timeMinuteField.current(0)
timeampmField = ttk.Combobox(window)
timeampmField.grid(row = 4, column = 3)
timeampmField['values'] = ('am', 'pm')
timeampmField.current(0)

# reminder snooze
tk.Label(window, text = "How long should I snooze for?").grid(row = 5, column = 0, columnspan = 4) # minutes
snoozeHourField = tk.Entry(window)
snoozeHourField.grid(row = 6, column = 0)
tk.Label(window, text = " hours").grid(row = 6, column = 1)
snoozeMinuteField = tk.Entry(window)
snoozeMinuteField.grid(row = 6, column = 2)
tk.Label(window, text = " minutes").grid(row = 6, column = 3)

button1 = tk.Button(window, text = "Add Reminder", command = addReminderButton)
button1.grid(row = 8, column = 0, columnspan = 4)

window.mainloop()
