#!/usr/bin/env python

import sys
import os
from pyvirtualdisplay import Display
from selenium import webdriver

#usage first create a directory (ss) -> python browserscreenshot.py labscanresults_p80.gnmap ss
def getProto(port):
    return {
	"80": "http",
	"443": "https"
    }.get(port,"http")


def takeSS(host,port):
	display = Display(visible=0, size=(800, 600))
	display.start()
	url=getProto(port)+"://"+host+":"+port
	browser = webdriver.Firefox()
	browser.get(url)
	ssfile=sys.argv[2]+"/"+host+"_"+port+".png"
	browser.save_screenshot(ssfile)
	print ssfile+" has created"
	browser.quit()
	display.stop()


hostfile=open(sys.argv[1])
lines=hostfile.readlines()
for line in lines:
	#for custom where IP:port,port,port style
	#host=line[:-1].split(":")[0]
	#ports=line[:-1].split(":")[1].split(",")
	
	#for port in ports:
	#	takeSS(host,port)
	
	#for gnmap file	
	if ("ports" in line.lower() and "open" in line.lower()):
		host=line.split(" ")[1]
		ports=line.split(":",2)[2].split("/,")
#		print "line: "+line
#		print ports
		for item in ports:
#			print "item: "+item
			if ("open" in item.lower()):
				port=item.split("/")[0][1:]
				takeSS(host,port)
#				print "port:"+port
#		print "==============================================================================\n"
hostfile.close()
