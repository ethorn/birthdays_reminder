# App for reminding me of birthdays

# Launching on login:
# 1) create shell_launch.sh
# 2) create com.startup.plist
# 4) put com.birthdays.reminder.plist in ~/Library/LaunchAgents/
# 5) Add the plist to launch on load
#    : sudo launchctl load -w ~/Library/LaunchAgents/com.birthdays.reminder.plist
# To remove: sudo launchctl unload -w ~/Library/LaunchAgents/com.birthdays.reminder.plist

# Neste steg:
# * Få den til å kjøre i bakgrunnen og sjekke 2-3 ganger per dag

import os
import time


# Take the birthday lookup file from home directory
file_path = os.environ['HOME'] + '/Desktop/birthdays_reminder_app/birthdays_library.txt'


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def check_birthday():
    lookup_file = open(file_path, 'r')
    today = time.strftime('%d-%m')
    # birth_day_flag = 0

    for entry in lookup_file:
        if today in entry:
            line = entry.split(' ')
            # birth_day_flag = 1
            notify('BURSDAG: ' + line[1] + ' ' + line[2], "Husk!")


check_birthday()
