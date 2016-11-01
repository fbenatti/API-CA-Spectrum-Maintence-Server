#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth


class Spectrum(object):
	def __init__(self, Urlhost=None, user_spectrum=None, pass_spectrum=None, database=None):
		self.Urlhost = Urlhost
		self.user_spectrum = user_spectrum
		self.pass_spectrum = pass_spectrum
		self.database = database
		
	def _add_maintence(self,idspectrum):
		comado_spectrum = ('http://'+ self.Urlhost +'/spectrum/restful/model/'+ idspectrum +'?attr=0x1295d&val=false')
		j = requests.put(comado_spectrum, auth=HTTPBasicAuth(self.user_spectrum, self.pass_spectrum), verify=False)	
		return j.text
		
	def _del_maintence(self,idspectrum):
		comado_spectrum = ('http://'+ self.Urlhost +'/spectrum/restful/model/'+ idspectrum +'?attr=0x1295d&val=true')
		j = requests.put(comado_spectrum, auth=HTTPBasicAuth(self.user_spectrum, self.pass_spectrum), verify=False)	
		return j.text
	