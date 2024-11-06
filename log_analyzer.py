#/!/bin/python3



#This imports the datetime module, which provides classes for manipulating dates and times.

import datetime



#This line sets the variable log_path to the path of the authentication log file.

log_path = '/var/log/auth.log'

#This opens the log file in read-only text mode ('rt') and assigns it to the variable file. The with statement ensures that the file is automatically closed after it's no longer needed.

#The with statement ensures that the file is automatically closed after it's no longer needed.

with open(log_path, 'rt') as file:

	data=file.readlines()

	for i in data:

		split_data = i.split()

		dt = datetime.datetime.fromisoformat(split_data[0])

		formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")

		#print(split_data) #Testing and analysis for positioning of the data for extraction and parsing



#Capturing ALL EXECUTED commands

		if "COMMAND" in split_data[-2]: #This checks if the second-to-last element of split_data contains the word "COMMAND".

			print("Command execution was captured for user:" + ' ' + split_data[1] + ' using ' + split_data[-2] + ' ' + split_data[-1] + ' at timestamp: ' + formatted_time)

		if "COMMAND" in split_data[-3]: #This checks if the third-to-last element of split_data contains the word "COMMAND".

			print("Command execution was captured for user:" + ' ' + split_data[1] + ' using ' + split_data[-3] + ' ' + split_data[-2] + ' ' + split_data[-1] + ' at timestamp: ' + formatted_time)



#su

		if "su:" in split_data: #his checks if the line contains "su:". If true, the script extracts the user who executed the su command and prints a message accordingly.

			su_info = str(split_data[-3][6:])

			su_print = print('The user ' + su_info + ' ' + 'used "su" command at datetime:' + ' ' +  formatted_time)



#sudo

		if "sudo:" in split_data: #This checks if the line contains "sudo:". If true, the script extracts the command executed using sudo and prints a message.

			sudo_splitinfo1 = split_data[-2]

			sudo_splitinfo2 = split_data[-1]

			if "COMMAND" in sudo_splitinfo1:

				sudo_info = str(sudo_splitinfo1 + ' ' + sudo_splitinfo2)

				print('sudo was used by ' + split_data[3] + ' ' + 'for the following: ' + sudo_info)



#ALERT!! (Failure to use) sudo

		if "sudoers" in split_data: #This checks if the line contains "sudoers". If true, the script extracts the user who failed to use sudo and the command they tried to execute, and prints an alert message.

			sudo_alert1 = split_data[3]

			sudo_alert2 = split_data[-2]

			sudo_alert3 = split_data[-1]

			print('ALERT!! The user ' + sudo_alert1 + ' ' + 'failed to use the command sudo for the following: ' + sudo_alert2 + ' ' + sudo_alert3)



#newly added user

#Checks if the line contains "sudo:" and then checks if the command executed using sudo is "useradd" or "adduser". If true, the script extracts the user who added the new user and the command used.

		if "sudo:" in split_data:

			sudo_splitinfo1 = split_data[-2]

			sudo_splitinfo2 = split_data[-1]

			sudo_splitinfo3 = split_data[-3]

			sudo_splitinfo4 = split_data[1]

			if "useradd" in sudo_splitinfo1:

				useradd_info = str(sudo_splitinfo1 + ' ' + sudo_splitinfo2)

				print('New user was added by ' + split_data[3] + ' ' + 'for the following: ' + useradd_info + ' ' + 'at datetime:' + ' ' + formatted_time)

			if "adduser" in sudo_splitinfo3:

				adduser_info = str(sudo_splitinfo3 + ' ' + sudo_splitinfo1 + ' ' + sudo_splitinfo2)

				print('New user was added by ' + sudo_splitinfo4 + ' ' + 'for the following: ' + adduser_info + ' ' + 'at datetime:' + ' ' + formatted_time)

#deleted users

#Checks if the line contains "sudo:" and then checks if the command executed using sudo is "userdel". If true, the script extracts the user who deleted the existing user and the command used.

		if "sudo:" in split_data:

			sudo_splitinfo1 = split_data[-2]

			sudo_splitinfo2 = split_data[-1]

			if "userdel" in sudo_splitinfo1:

				userdel_info = str(sudo_splitinfo1 + ' ' + sudo_splitinfo2)

				print('Existing user: ' + sudo_splitinfo2 + ' ' + 'was deleted by ' + split_data[3] + ' ' + 'under the following: ' + userdel_info + ' ' + 'at datetime:' + ' ' + formatted_time)



#changing passwords

#Checks if the line contains "password changed" and extracts the user who changed their password.

		sudo_splitinfo1 = split_data[-4]

		sudo_splitinfo2 = split_data[-3]

		chpsswd_info = str(sudo_splitinfo1 + ' ' + sudo_splitinfo2)

		if "password changed" in chpsswd_info:

			print('User: ' + split_data[-1] + ' ' + 'changed password at datetime:' + ' ' + formatted_time)		

