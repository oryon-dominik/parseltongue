"""
Initialisierung 
Python-Entwciklungsumgebung 
in System : Pythia / Vanatik
"""

__version__ = '0.3'
__author__ = 'Pythia Vanatik'

## Import-Module

import os
import subprocess
import time
import threading

## Initialisation
print ("Initialisiere...")

session_start = time.time()

sleeptimer = 5
progressbar = ["|", "/", "-", "\\", "|", "/", "-", "\\"]
pgb_counter = 0 # Initialisation des progressbaritems auf Anfang

## End-Sequenz
print
print ("Diese Session dauerte: ", time.time()-session_start)
print ("Beende Python Programmiersession in ...  ", end=' ')

#end of programm