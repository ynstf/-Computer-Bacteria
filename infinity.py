import os

cont = open("infinity.py", "r")           #open this file to read
pycont = cont.read()                      #read this file and save it as pycont
cont.close                                #close this file

with open("infinity.py", "a+") as f:      #open this file to write and append
    f.write(pycont)                       #add the pycont to this file
f.close                                   #close this file

os.system('python infinity.py')           #execuit this file.py to repeat the script
