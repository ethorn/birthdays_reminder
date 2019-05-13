# App for reminding me of birthdays

# Launching on login:
# 1) create shell_launch.sh
# 2) create com.startup.plist
# 4) put com.birthdays.reminder.plist in ~/Library/LaunchAgents/
# 5) Add the plist to launch on load
#    : sudo launchctl load -w ~/Library/LaunchAgents/com.birthdays.reminder.plist
# To remove: sudo launchctl unload -w ~/Library/LaunchAgents/com.birthdays.reminder.plist


import os
import time


file_path = os.environ['HOME'] + '/Desktop/birthdays_reminder_app/birthdays_library.txt'


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def check_birthday():
    lookup_file = open(file_path, 'r')
    today = time.strftime('%d-%m')

    for entry in lookup_file:
        if today in entry:
            line = entry.split(' ')
            notify(line[1] + ' ' + line[2], "Has birthday today!")


check_birthday()
