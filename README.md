# API-CA-Spectrum-Maintence-Server" 

* You can use Web-Server API of CA-Spetrum for add hosts in Maintenace, for it you need GET idspectrum.


- For use, you need change schedule.py:


\#ip_spectrum = "10.0.0.1"\\n
\#user_spectrum = "user"\\n
\#pass_spectrum = "password"\\n
\#MHandle = "Number_MHandle"\\n

* How can automatic generate MHandle:

C:\ca\Spectrum\vnmsh\connect.exe
C:\ca\Spectrum\vnmsh\show.exe devices > C:\scp\ic_spectrum.txt


