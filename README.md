# API-CA-Spectrum-Maintence-Server" 

* You can use Web-Server API of CA-Spetrum for add hosts in Maintenace, for it you need GET idspectrum.


- For use, you need change schedule.py:


\#ip_spectrum = "10.0.0.1"

\#user_spectrum = "user"

\#pass_spectrum = "password"

\#MHandle = "Number_MHandle"

* How can automatic generate MHandle:

 - In Windows Server you may execute this command in PowerShell or CMD:

\#Connect to DB Spectrum:

C:\ca\Spectrum\vnmsh\connect.exe

\#Genarate list of Model Handle:
C:\ca\Spectrum\vnmsh\show.exe devices > C:\scp\ic_spectrum.txt


