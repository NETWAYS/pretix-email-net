Dies ist ein Plugin für Pretix, das eine eigene Vorlage für E-Mails erstellt.

Sie besteht aus 2 Boxen im Haupteil und einem Footer mit Signatur und Logos.
In der ersten Box ist nach der Eventüberschrift der erste Paragraf mit der Begrüßung blau, der jeweilige Kundenname kann über die Email-Einstellungen unter "Email-Content" mit der Variable "{name}" oder "{name_for_salutation}" dynamisch eingestellt werden.

In der zweiten Box werden die Bestelldetails dargestellt

In der Vorlage können Sie optional ein Veranstaltungslogo in der linken oberen Ecke einblenden und die Signatur ist in der Pretix-GUI auswählbar.

Die ersten beiden Zeilen der Signatur sind in blauer Farbe gehalten.
Rechts neben der Signatur befinden sich 4 Social Media Icons mit Hyperlinks. Die URLs der Icons und Hyperlinks sind in der Fußzeile hartcodiert und müssen auf Wunsch manuell geändert werden.

Rechts von der Signatur befinden sich vier Social Media Icons für Twitter, Youtube, Facebook und Instagram.

Installation:
Installieren Sie das Plugin mit ``pip install pretix-nes-email``.
Dann konfigurieren Sie Pretix neu mit den Befehlen ``python -m pretix rebuild && python migrate``
Dann starten Sie den Server neu mit ``systemctl restart pretix-web pretix-worker`` (je nach Installation)

