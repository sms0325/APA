import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc

def addReminderButton():
	print("Name:", nameField.get())
	print("Time:", timeDate.selection_get(), "|",timeHourField.get(), ":",timeMinuteField.get())
	print("Snooze:", snoozeHourField.get(), ":", snoozeMinuteField.get())

window = tk.Tk()
window.title("Add Reminder")

tk.Label(window, text = "What should I remind you to do?").grid(row = 0, column = 0, columnspan = 3)
nameField = tk.Entry(window)
nameField.grid(row = 1, column = 0, columnspan = 3)

tk.Label(window, text = "When should I remind you?").grid(row = 2, column = 0, columnspan = 3) # epoch (ms)
timeDate = tkc.Calendar(window)
timeDate.grid(row = 3, column = 0, columnspan = 3)
timeHourField = ttk.Combobox(window)
timeHourField.grid(row = 4, column = 0)
timeHourField['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
						   '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
timeHourField.current(0)
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

tk.Label(window, text = "How long should I snooze for?").grid(row = 5, column = 0, columnspan = 3) # minutes
snoozeHourField = ttk.Combobox(window)
snoozeHourField.grid(row = 6, column = 0)
snoozeHourField['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
							 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
snoozeHourField.current(0)
tk.Label(window, text = ":").grid(row = 6, column = 1)
snoozeMinuteField = ttk.Combobox(window)
snoozeMinuteField.grid(row = 6, column = 2)
snoozeMinuteField['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09'
							   '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'
							   '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'
							   '30', '31', '32', '33', '34', '35', '36', '37', '38', '39'
							   '40', '41', '42', '43', '44', '45', '46', '47', '48', '49'
							   '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
snoozeMinuteField.current(0)

button1 = tk.Button(window, text = "Add Reminder", command = addReminderButton)
button1.grid(row = 8, column = 0, columnspan = 3)

window.mainloop()
