#!/bin/bash
#
#    DynCal - Sailfish OS calendar icon will show you the current day of the month.
#    Copyright (C) 2015-2016  fravaccaro <fravaccaro90@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Get date and define variables
day="$(date +'%d')"
month="$(date +'%m')"
main=/usr/share/harbour-dyncal

# Find if there's an holiday icon for the current day
if [ -f $main/icons/$month$day.png ]; then
icon=$month$day
else
icon=$day
fi

# Apply icon
rm -rf /usr/share/themes/sailfish-default/meegotouch/z1.0/icons/icon-launcher-calendar.png
cp $main/icons/$icon.png /usr/share/themes/sailfish-default/meegotouch/z1.0/icons/icon-launcher-calendar.png
rm -rf /usr/share/applications/jolla-calendar.desktop && touch /usr/share/applications/jolla-calendar.desktop
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
/usr/bin/desktop-file-install /usr/share/applications/jolla-calendar.desktop --set-icon=$main/icons/$icon.png
exit 0
