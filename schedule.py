#!/usr/bin/python
# -*- coding: utf-8 -*-
from maintenance import Spectrum

###Configuration Spectrum
ip_spectrum = "10.0.0.1"
user_spectrum = "user"
pass_spectrum = "password"
hostid='x111111'

s=Spectrum(ip_spectrum,user_spectrum,pass_spectrum)

##Example add maintenance in server of Spectrum.
print s._add_maintence(hostid)


