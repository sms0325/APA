import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
from datetime import date
from datetime import datetime

from APAConnect import *

class AddReminder:
	def __init__(self, master):
		self.master = master
		self.window = None
		self.nameField = None
		self.timeDateField = None
		self.timeHourField = None
		self.timeMinuteField = None
		self.timeampmField = None
		self.snoozeHourField = None
		self.snoozeMinuteField = None
		self.confirmation = None
		self.openAddWindow()
		return

	def addReminderButton(self):
		name = self.nameField.get()
		time = str(self.timeDateField.selection_get())
		time = time + ' ' + self.convert12hrTo24hr(self.timeHourField.get(),self.timeMinuteField.get(),self.timeampmField.get())
		snooze = str(int(self.snoozeHourField.get()) * 60 + int(self.snoozeMinuteField.get()))
		reminderInfo = 'Name: ' + name + '\nTime: ' + time + '\nSnooze: ' + snooze + ' minutes'
		print(reminderInfo)
		if (connectToSQLite(name, time, snooze)):
			self.confirmation.config(text = 'Sucessfully submitted reminder with:\n' + reminderInfo)
			self.confirmation.config(fg='black')
		else:
			self.confirmation.config(text = 'Failed to submit reminder with:\n' + reminderInfo)
			self.confirmation.config(fg='red')
		
		# TODO: close this window(?)

	def convert12hrTo24hr(self, hour, minute, ampm):
		hour = int(hour)
		if (hour == 12):
			hour = 0
		if (str(ampm) == 'pm'):
			hour += 12
		if (hour < 10):
			hour = '0' + str(hour)
		return str(hour) + ':' + str(minute) + ':00'

	def validateNonnegativeInteger(self, action, index, value_if_allowed,
						   prior_value, text, validation_type, trigger_type, widget_name):
		if value_if_allowed:
			try:
				value_if_allowed = int(value_if_allowed)
				if (value_if_allowed >= 0):
					return True
			except ValueError:
				return False
		return False

	def validateDateNotInPast(self, action, index, value_if_allowed,
						   prior_value, text, validation_type, trigger_type, widget_name):
		if value_if_allowed:
			try:
				value_if_allowed = int(value_if_allowed)
				if (value_if_allowed >= 0):
					return True
			except ValueError:
				return False
		return False
	
	def openAddWindow(self):
		self.window = tk.Toplevel(self.master)
		self.window.title("Add Reminder")
		
		# reminder name
		tk.Label(self.window, text = "What should I remind you to do?").grid(row = 0, column = 0, columnspan = 4)
		self.nameField = tk.Entry(self.window, width = 50)
		self.nameField.grid(row = 1, column = 0, columnspan = 4)
		self.nameField.insert(0, 'Reminder Name')

		# reminder time
		# TODO: Check if date/time is not in past
		validateDateNotInPastCommand = (self.window.register(self.validateDateNotInPast),
										'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		tk.Label(self.window, text = "When should I remind you?").grid(row = 2, column = 0, columnspan = 4)
		self.timeDateField = tkc.Calendar(self.window, mindate=date.today(), showweeknumbers = False)
		self.timeDateField.grid(row = 3, column = 0, columnspan = 4)
		self.timeHourField = ttk.Combobox(self.window, width = 2, validate = 'key', validatecommand = validateDateNotInPastCommand)
		self.timeHourField.grid(row = 4, column = 0)
		self.timeHourField['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
		self.timeHourField.current(11)
		tk.Label(self.window, text = ":").grid(row = 4, column = 1)
		self.timeMinuteField = ttk.Combobox(self.window, width = 2)
		self.timeMinuteField.grid(row = 4, column = 2)
		self.timeMinuteField['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
									 '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
									 '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
									 '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
									 '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
									 '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
		self.timeMinuteField.current(0)
		self.timeampmField = ttk.Combobox(self.window, width = 3, validate = 'key', validatecommand = validateDateNotInPastCommand)
		self.timeampmField.grid(row = 4, column = 3)
		self.timeampmField['values'] = ('am', 'pm')
		self.timeampmField.current(0)

		# reminder snooze
		validateNonnegativeIntegerCommand = (self.window.register(self.validateNonnegativeInteger),
										'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		tk.Label(self.window, text = "How long should I snooze for?").grid(row = 5, column = 0, columnspan = 4)
		self.snoozeHourField = tk.Entry(self.window, width = 4, validate = 'key', validatecommand = validateNonnegativeIntegerCommand)
		self.snoozeHourField.grid(row = 6, column = 0)
		self.snoozeHourField.insert(0, 0)
		tk.Label(self.window, text = " hours").grid(row = 6, column = 1)
		self.snoozeMinuteField = tk.Entry(self.window, width = 4, validate = 'key', validatecommand = validateNonnegativeIntegerCommand)
		self.snoozeMinuteField.grid(row = 6, column = 2)
		self.snoozeMinuteField.insert(0, 0)
		tk.Label(self.window, text = " minutes").grid(row = 6, column = 3)

		submit = tk.Button(self.window, text = "Add Reminder", command = self.addReminderButton)
		submit.grid(row = 8, column = 0, columnspan = 4)

		self.confirmation = tk.Label(self.window, text = "")
		self.confirmation.grid(row = 9, column = 0, columnspan = 4)