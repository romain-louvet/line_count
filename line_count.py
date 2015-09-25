# ---------------------------------------------------------------------------
# line_count.py
# Created on: 2015-09-25
# Author : Romain Louvet, PhD student
# Contact : romain.louvet@alumni.univ-avignon.fr
# Description: 
# Count lines of code of every file within a given directory.
# Remove commentaries (with "#")
#
# Tested with python 2.7.5 and Windows 7
# ---------------------------------------------------------------------------

import os, sys

wd = input("Directory containing files :")
files = os.listdir(wd)

for f in files:
    try:
        fi = wd+"\\"+f
        fichier = open(fi,"r")
        fichier = fichier.read()
        # remove blank spaces
        fichier = filter(lambda a: a != ' ', fichier)
        # remove tab
        fichier = filter(lambda a: a != "\t", fichier)
                         # transform into list
        liste = str.split(fichier,"\n")
        # remove list element beginning with "#"
        liste = [x for x in liste if not x.startswith('#')]
        # remove element without code
        liste = filter(lambda a: a != '', liste)
        # result
        print(f+" : "+str(len(liste)))
    except:
        # error
        print(file+" ERROR")


