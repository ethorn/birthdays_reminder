import os
import time


file_path = os.environ['HOME'] + \
            '/Desktop/birthdays_reminder_app/birthdays_library.txt'


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
