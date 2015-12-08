#!/bin/bash
#This script is written by fravaccaro fravaccaro@jollacommunity.it
#If you want to reuse it, please don't remove this notice

day="$(date +'%d')"
month="$(date +'%m')"

rm -rf /usr/share/themes/jolla-ambient/meegotouch/z1.0/icons/icon-launcher-calendar.png
cp /usr/share/harbour-dyncal/icons/$month$day.png /usr/share/themes/jolla-ambient/meegotouch/z1.0/icons/icon-launcher-calendar.png
rm -rf /usr/share/applications/jolla-calendar.desktop
/usr/bin/desktop-file-install /usr/share/applications/jolla-calendar.desktop
echo '[Desktop Entry]
Type=Application
Name=Calendar
X-MeeGo-Logical-Id=calendar-ap-name
X-MeeGo-Translation-Catalog=calendar
Exec=invoker --type=silica-qt5 -n -d 5 -s /usr/bin/jolla-calendar
Comment=Jolla calendar
X-Maemo-Service=com.jolla.calendar.ui
X-Maemo-Object-Path=/com/jolla/calendar/ui
X-Maemo-Method=com.jolla.calendar.ui.activateWindow
X-Desktop-File-Install-Version=0.20' > /usr/share/applications/jolla-calendar.desktop
/usr/bin/desktop-file-install /usr/share/applications/jolla-calendar.desktop --set-icon=/usr/share/harbour-dyncal/icons/$month$day.png
exit 0
