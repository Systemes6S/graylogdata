#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import os, tarfile, bz2, requests, readline, glob, sys, hashlib, time

#Disabling proxy
proxies = {
  "http": None,
  "https": None,
}

#GrayLog Indices directory
graylogPath = "/var/lib/elasticsearch/graylog/nodes/0/indices/"

#Current working directory
os.chdir(graylogPath)

def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

indexName = raw_input("\n" + "Nom de l\'index a exporter : ")

r = requests.post('http://localhost:9200/' + indexName + '/_close',proxies=proxies)

if r.status_code == 200:
 print("Fermeture de l\'index " + indexName + " \x1b[6;30;42m" + "[OK]" + "\x1b[0m")
 time.sleep(3)
else:
 print("\x1b[6;30;41m" + "[Erreur]" + "\x1b[0m" + " Impossible de fermer l\'index " + indexName)

try:
 archiveName = "SVG_" + indexName + ".tar.bz2"
 archive = tarfile.open(archiveName,'w:bz2')
 archive.add(indexName)
 archive.close()
 print("Création de l\'archive : " + archiveName + " \x1b[6;30;42m" + "[OK]" + "\x1b[0m")
 time.sleep(3)

 r = requests.post('http://localhost:9200/' + indexName + '/_open',proxies=proxies)

 if r.status_code == 200:
  print("Ouverture de l\'index " + indexName + " \x1b[6;30;42m" + "[OK]" + "\x1b[0m")
  time.sleep(3)
 else:
  print("\x1b[6;30;41m" + "[Erreur]" + "\x1b[0m" + " Impossible d\'ouvrir l\'index " + indexName)

 with open(archiveName) as file_to_check:
    #read contents of the file
    data = file_to_check.read()
    #pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()

 print("\n" + "\x1b[5;30;47m" + "Hash de l\'archive : " + md5_returned + "\x1b[0m" + "\n")

except:
 print("\x1b[6;30;41m" + "[Erreur]" + "\x1b[0m" + " Impossible de créer l\'archive")
 os.remove(archiveName)
