# birthdays_reminder
Small python app for reminding you of birthdays. Works on Mac OS.

This is just for fun and I don't think anyone will ever view this readme or try to use this program. If, however, you have gone down a rabbit hole and ended up here, this is how you use this "app":

What it does:
* When you login on your computer, the program checks birthdays_library.txt to see if there are any birthdays today. If it is, you get a notification.

Installation:
1) Download this project to a folder.
2) Change paths in birthday_reminder_app.py AND shell_launch.sh
3) Copy com.birthdays.reminder.plist to ~/Library/LaunchAgents
4) Make sure com.birthdays.reminder.plist is executable. Write this in terminal: sudo chmod +x ~/Library/LaunchAgents/com.birthdays.reminder.plist
5) Make sure shell_launch.sh is executable. Write this in terminal: sudo chmod +x /PATH/TO/BIRTHDAY_APP_FOLDER/shell_launch.sh
6) Add plist to run when you login to your mac. Write this in terminal: sudo launchctl load -w ~/Library/LaunchAgents/com.birthdays.reminder.plist

To remove this app from running when you login:
1) sudo launchctl unload -w ~/Library/LaunchAgents/com.birthdays.reminder.plist

Usage:
* Add birthdays to birthdays_library.txt in the format DD-MM

Settings:
* Default reminder interval is set to show a notification every 4 hours. To change this, open ~/Library/LaunchAgents/com.birthdays.reminder.plist and go to <key>StartInterval</key>. The value under this (14400) is how long the script should wait until it runs again (in seconds). Change this to anything you want.