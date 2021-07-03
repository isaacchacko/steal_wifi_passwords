import subprocess

def WifiPassword(wifi_name):
	try:
		output = subprocess.check_output(['netsh','wlan','show','profile', wifi_name, 'key=clear']).decode('utf-8').split('\n')
		for i in output:
			if "Key Content" in i:
				return i.split(":")[1].strip()
	except:
		return 'Problem with finding password'

def WifiDirectory():
	output = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
	wifis = []
	for i in output:
		if "All User Profile" in i:
			wifis.append(i.split(":")[1].strip())

	return wifis

def WifiPassDirectory():
	wifis = WifiDirectory()
	pass_directory = {}
	for wifi in wifis:
		pass_directory[wifi] = WifiPassword(wifi)

	return pass_directory

pass_dir = WifiPassDirectory()

for key, item in pass_dir.items():
	print(key + ' = ' + str(item))