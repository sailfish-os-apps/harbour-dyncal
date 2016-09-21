Name:          harbour-dyncal
Version:       0.4.1
Release:       1
Summary:       DynCal
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 2.0.1
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Change Calendar icon accordingly with the day.

%files
%defattr(-,root,root,-)
/usr/share/*

%post
chmod +x /usr/share/harbour-dyncal/*.sh
mv /usr/share/harbour-dyncal/harbour-dyncal.service /etc/systemd/system/
mv /usr/share/harbour-dyncal/harbour-dyncal.timer /etc/systemd/system/
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
rm /etc/systemd/system/harbour-dyncal.timer
rm /etc/systemd/system/harbour-dyncal.service
rm -rf /usr/share/harbour-dyncal
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Wed Sep 21 2016 0.4.1
- High-res icons.
- Some icons redesigned.

* Tue Jan 19 2016 0.4.0
- Sailfish OS 2.0.7 support.

* Tue Dec 29 2015 0.3.1
- Reduced package size.

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

* Thu Sep 22 2015 0.1
- First build.
