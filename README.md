# pretix-email-net
Email renderer for Netways Event Services


das HTML Template ist in dem Verzeichnis pretix/src/pretix/base/templates/pretixbase/email/ abzulegen. 
Das Verzeichnis pretix_nes_mail ist unter pretix/src/pretix/plugins/ abzulegen.
Im Plugin Dir müssen die Commands 
python3 setup.py develop

und 

make

ausgeführt werden. 

Unter Umständen kann es bei ausführen des develop Befehls notwendig sein, das Pip Paket von Pretix nachzuinstallieren. Warum, ist zzt nicht bekannt. 


Das Plugin kann im Webinterface unter den Eventsettings -> Plugins -> Customization aktiviert werden. 


Zu beachten ist, dass hier **keine** Signatur enthalten ist, diese muss unter den Email-Settings, unter Generell -> *Signature*-Box eingetragen werden.
