Name:          harbour-dyncal
<<<<<<< HEAD
Version:       0.3.0
Release:       1
=======
Version:       0.1
Release:       14
>>>>>>> c6234cee16cd4c6023e5d96a95d9f3e6b04848a7
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
<<<<<<< HEAD
%defattr(-,root,root,-)
/usr/share/*

%post
chmod +x /usr/share/harbour-dyncal/*.sh
mv /usr/share/harbour-dyncal/harbour-dyncal.service /etc/systemd/system/
mv /usr/share/harbour-dyncal/harbour-dyncal.timer /etc/systemd/system/
=======
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
>>>>>>> c6234cee16cd4c6023e5d96a95d9f3e6b04848a7
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
<<<<<<< HEAD
rm /etc/systemd/system/harbour-dyncal.timer
rm /etc/systemd/system/harbour-dyncal.service
=======
rm  /etc/systemd/system/harbour-dyncal.timer
rm  /etc/systemd/system/harbour-dyncal.service
>>>>>>> c6234cee16cd4c6023e5d96a95d9f3e6b04848a7
rm -rf /usr/share/harbour-dyncal
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
<<<<<<< HEAD
* Tue Dec 8 2015 0.3.0
- Extensions support added.

* Thu Oct 8 2015 0.2.5
- Holidays' icons updated.

* Wed Oct 7 2015 0.2.4
- Icon jumping to the bottom of the app tray may be fixed.

* Sat Oct 3 2015 0.2.3
- Bugfix.

* Tue Sep 29 2015 0.2.2
- Bugfix.

* Tue Sep 29 2015 0.2.1
- Bugfix.

* Mon Sep 28 2015 0.2
- Added some holidays' icons.
- Fixed icon not updating.

=======
>>>>>>> c6234cee16cd4c6023e5d96a95d9f3e6b04848a7
* Thu Sep 22 2015 0.1
- First build.
