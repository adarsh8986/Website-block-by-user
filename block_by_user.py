import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"

siteNum = int(input("How many site you want to block"))

for i in range(1,siteNum+1):
	website_list=[]
	website = input("Enter Website you want to block")
	website_list.append(website)
	
startTime = int(input("Blocking time start for your pc (in hour)"))
endTime = int(input("End time of your block mode"))

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,startTime) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,endTime):
		with open(host_path,"r+") as file:
			content = file.read()
			for websites in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else:
		with open(host_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(lines)
				file.truncate()
				
	time.sleep(600)
	
	
					
	
					