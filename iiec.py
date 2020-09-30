#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/plain")
print()

mydata = cgi.FieldStorage()
myx = mydata.getvalue("x")
output = subprocess.getstatusoutput("sudo "+myx)
status = output[0]
myout = output[1]
print(myout)

