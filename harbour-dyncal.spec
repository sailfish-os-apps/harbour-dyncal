Name:          harbour-dyncal
Version:       0.1
Release:       14
Summary:       DynCal
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Change Calendar icon accordingly with the day.

%files
/usr/share/harbour-dyncal/harbour-dyncal.sh
/usr/share/harbour-dyncal/harbour-dyncal-uninstall.sh
/usr/share/harbour-dyncal/harbour-dyncal.service
/usr/share/harbour-dyncal/harbour-dyncal.timer
/usr/share/harbour-dyncal/icons/01.png
/usr/share/harbour-dyncal/icons/02.png
/usr/share/harbour-dyncal/icons/03.png
/usr/share/harbour-dyncal/icons/04.png
/usr/share/harbour-dyncal/icons/05.png
/usr/share/harbour-dyncal/icons/06.png
/usr/share/harbour-dyncal/icons/07.png
/usr/share/harbour-dyncal/icons/08.png
/usr/share/harbour-dyncal/icons/09.png
/usr/share/harbour-dyncal/icons/10.png
/usr/share/harbour-dyncal/icons/11.png
/usr/share/harbour-dyncal/icons/12.png
/usr/share/harbour-dyncal/icons/13.png
/usr/share/harbour-dyncal/icons/14.png
/usr/share/harbour-dyncal/icons/15.png
/usr/share/harbour-dyncal/icons/16.png
/usr/share/harbour-dyncal/icons/17.png
/usr/share/harbour-dyncal/icons/18.png
/usr/share/harbour-dyncal/icons/19.png
/usr/share/harbour-dyncal/icons/20.png
/usr/share/harbour-dyncal/icons/21.png
/usr/share/harbour-dyncal/icons/22.png
/usr/share/harbour-dyncal/icons/23.png
/usr/share/harbour-dyncal/icons/24.png
/usr/share/harbour-dyncal/icons/25.png
/usr/share/harbour-dyncal/icons/26.png
/usr/share/harbour-dyncal/icons/27.png
/usr/share/harbour-dyncal/icons/28.png
/usr/share/harbour-dyncal/icons/29.png
/usr/share/harbour-dyncal/icons/30.png
/usr/share/harbour-dyncal/icons/31.png

%post
mv /usr/share/harbour-dyncal/harbour-dyncal.service /etc/systemd/system/
mv /usr/share/harbour-dyncal/harbour-dyncal.timer /etc/systemd/system/
cp /usr/share/themes/jolla-ambient/meegotouch/z1.0/icons/icon-launcher-calendar.png /usr/share/harbour-dyncal/default.png
cp /usr/share/applications/jolla-calendar.desktop /usr/share/harbour-dyncal/jolla-calendar.desktop.bak
/usr/share/harbour-dyncal/harbour-dyncal.sh
systemctl start harbour-dyncal.timer
systemctl enable harbour-dyncal.timer
systemctl start harbour-dyncal.service
systemctl enable harbour-dyncal.service

%preun
/usr/share/harbour-dyncal/harbour-dyncal-uninstall.sh

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
systemctl stop harbour-dyncal.timer
systemctl disable harbour-dyncal.timer
systemctl stop harbour-dyncal.service
systemctl disable harbour-dyncal.service
rm  /etc/systemd/system/harbour-dyncal.timer
rm  /etc/systemd/system/harbour-dyncal.service
rm -rf /usr/share/harbour-dyncal
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Thu Sep 22 2015 0.1
- First build.
