# KATANA
# Update
# Script by RedToor
# 28/02/2015
from core import colors
import subprocess
import socket
import os
def update():
	print ""
	print "     ["+colors.O+"!"+colors.W+"] Updating KATANA..."
	try:
		red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
		red.connect(("google.com", int(80))) 
		if True:
			subprocess.Popen("cd /tmp;git clone https://github.com/RedToor/katana.git;cp -R /tmp/katana/* /usr/share/katana/;rm -rf /tmp/katana/*", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			pass
			print "     ["+colors.G+"+"+colors.W+"] SUCCESSFUL KATANA Updated"
			print ""
	except:
		print("     ["+colors.R+"-"+colors.W+"] Error ")
		print""