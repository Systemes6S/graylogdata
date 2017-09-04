#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-

import subprocess, sys, os, tarfile, bz2, requests, readline, glob, hashlib, time
from os import popen

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

indexName = raw_input("\n" + "Nom de l\'index a importer : ")
archiveName = "SVG_" + indexName + ".tar.bz2"

with open(archiveName) as file_to_check:
 data = file_to_check.read()
 md5_returned = hashlib.md5(data).hexdigest()

 print("\n" + "\x1b[5;30;47m" + "Hash de l\'archive : " + md5_returned + "\x1b[0m" + "\n")

try:
 archive = tarfile.open(archiveName,'r:bz2')
 for tarinfo in archive:
    archive.extract(tarinfo)
 archive.close()
 print("Décompression de l\'archive" + " \x1b[6;30;42m" + "[OK]" + "\x1b[0m")
except:
 print("\x1b[6;30;41m" + "[Erreur]" + "\x1b[0m" + " Impossible de décompresser l\'archive" + "\n")
 sys.exit(0)
try:
 subprocess.check_call("sudo service elasticsearch restart".split())
 time.sleep(5)

 r = requests.post('http://localhost:9200/' + indexName + '/_open',proxies=proxies)

 if r.status_code == 200:
  print("Ouverture de l\'index " + indexName + " \x1b[6;30;42m" + "[OK]" + "\x1b[0m" + "\n")
 else:
  print("\x1b[6;30;41m" + "[Erreur]" + "\x1b[0m" + " Impossible d\'ouvrir l\'index " + indexName + "\n")
except:
 print("\x1b[6;30;41m" + "[Erreur]" + "\x1b[0m" + " Impossible de redémarrer le service elasticsearch" + "\n")
 sys.exit(0)
