#--> Author's Info
Version   = '0.2'
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu

#--> Import Module & Run
try :
    import os, sys, time, re, datetime, random, urllib, base64, struct, binascii, json
    from datetime import datetime
except Exception as e :
    exit('\nTerjadi Kesalahan!')
try :
    import requests
except Exception as e :
    os.system('pip install requests')
    import requests
try :
    import bs4
    from bs4 import BeautifulSoup as bs
except Exception as e :
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs
try:
    from concurrent.futures import ThreadPoolExecutor
except Exception as e :
    os.system('pip install concurrent')
    os.system('pip install futures')
    from concurrent.futures import ThreadPoolExecutor
try :
    from Crypto.Cipher import AES
    from Cryptodome import Random as RDM
except Exception as e :
    os.system('pip install Crypto')
    os.system('pip install pycryptodome')
    os.system('pip install pycryptodomex')
    from Crypto.Cipher import AES
    from Cryptodome import Random as RDM
try :
    import nacl
    from nacl.public import PublicKey as PK
    from nacl.public import SealedBox as SB
except Exception as e :
    print('%sModule %spynacl %sBelum Terpasang !\n'%(P,M,P))
    if 'linux' in sys.platform.lower():
        print('%sAnda Menggunakan %sLinux %s( %sEx : Termux Android%s ),\nKetik :'%(P,M,P,M,P))
        print('   %s$ %spkg install libsodium'%(M,P))
        print('   %s$ %sSODIUM_INSTALL=system pip install pynacl'%(M,P))
    elif 'win' in sys.platform.lower():
        print('%sAnda Menggunakan %sWindows%s/%sMacOS%s,\nKetik :'%(P,M,P,M,P))
        print('   %s$ %spip install pynacl'%(M,P))
    exit('')

#--> Geo Locator
try: country = requests.Session().get('http://ip-api.com/json/').json()['country']
except Exception as e: country = ''

#--> Global Variable
auth1 = 'Dapunta Khurayra X'
auth2 = 'Suci Maharani Putri'
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
ok = 0
cp = 0
boys_name = ['Axel Lateef Noah','Anzel Qasim Wisthara','Basheer Malik Yazdan','Bernardus Clementine Christian','Carel Vasco Zachariah','Cyrus Osmanth Elkanah','Damian Vasyl Isaac','Dominic Valdi Xander','Ephraim Benedict Gevariel','El Fatih Ghazwan','Fawwaz Rafisqy Ezaz','Faheem Fakhri Isyraq','Gianluca Nathanael Nadav','Haddad Ammar Ar-Rayyan','Istafa Tabriz Qiwam','Kenneth Krisantus Lazarus','Nathanael Alfred William','Vaskylo Yeremia Clearesta','Xaferius Eliel Antonios','Yesaya Nathanael Liam']
girls_name = ['Atika Fithriya Tsabita','Alya Kinana Juwairiyah','Adzkiya Naila Taleetha','Adiva Arsyila Savina','Aqeela Nabiha Sakhi','Bilqis Adzkiya Rana','Chayra Ainin Qulaibah','Caliana Fiona Syafazea','Chaerunnisa Denia Athalla','Dhawiyah Nisrin Naziha','Dilara Adina Yuani','Farah Sachnaz Ashanty','Ghariyah Zharufa Abidah','Hamna Nafisa Raihana','Hanin Raihana Syahira','Izza Hilyah Nafisah','Kayla Zhara Qamela','Mahreen Shafana Almahyra','Rasahana Shafwa Ruqayah','Shakayla Aretha Shaima']

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> Penjeda Waktu
def jeda(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                                 '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)
def tunggu_kode(t):
    for x in range(t+1):
        print('\r%sTunggu Kode %s Detik                            '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> User Agent Vivo
def random_ua_vivo():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Samsung
def random_ua_samsung():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B']) #--> Device Type
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Realme
def random_ua_realme():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                        #--> OS Version
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])   #--> Device Type
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                     #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                #--> Device Version
    sd_ver = random.randrange(1,10)                                                         #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                               #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Custom
def random_ua_custom():
    try:
        _file_ = uman
        if 'Android' in str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(10,13))
            ua1 = _file_.replace(ad_ver,os_ver)
        else: ua1 = _file_
        if 'Build' in str(_file_):
            od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A','PKQ1'])
            dv_ver = random.randrange(100000,250000)
            sd_ver = random.randrange(1,10)
            nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.replace(od_ver,nw_str)
        else: ua2 = ua1
        if 'Chrome' in str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            a = random.randrange(112,115)
            b = random.randrange(1000,10000)
            c = random.randrange(10,100)
            ch_ver = f'{a}.0.{b}.{c}'
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.replace(ch_old,ch_new)
        else: ua3 = ua2
        return(ua3)
    except Exception as e:
        return('Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')

#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s;'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.2 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,M,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      ─────────────── %s• %sRaya Artha %s• %s───────────────\n%s'%(A,M,P,M,A,P))

#--> Main Menu
class menu:
    def __init__(self):
        logo()
        try:
            data = eval(open('Setting_Create_FB/my_set.txt','r').read())
            self.ua       = data['ua']
            self.foto_pp  = data['pp']
            self.foto_ps  = data['ps']
            self.nama_bio = data['bio']
            self.city     = data['kota']
            self.web      = data['web']
            self.rl       = data['rl']
            self.listgrup = data['grup']
            self.accfoll  = data['akun']
            self.postid   = data['post']
            self.react    = data['react']
            self.comment  = data['com']
            self.create   = data['create']
            self.stat_bot = P
        except Exception as e:
            self.stat_bot = M
        self.main_menu()
    def main_menu(self):
        print('%s[%s1%s] %sCreate Account'%(M,P,M,P))
        print('%s[%s2%s] %sCheck Result'%(M,P,M,P))
        print('%s[%s3%s] %sSetting'%(M,P,M,P))
        print('%s[%s4%s] %sBot Account%s'%(M,P,M,self.stat_bot,P))
        print('%s[%s5%s] %sBot Page%s'%(M,P,M,self.stat_bot,P))
        x = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).lower()
        print('')
        if   x in ['1','01','001','a']: menu_create()
        elif x in ['2','02','002','b']: menu_check()
        elif x in ['3','03','003','c']: setting_bot()
        elif x in ['4','04','004','d']: bot_account()
        elif x in ['5','05','005','e']: bot_page()
        else: exit('%sIsi Yang Benar!%s'%(M,P))

#--> Menu Create
class menu_create:
    def __init__(self):
        global kelamin, namstat, nameme, web_email, tampil, useragent, uman, passtat, password, update
        try:os.mkdir('Akun_New')
        except Exception as e :pass
        print('      %s◉ %sRekomendasi   %s◉ %sTidak Rekomendasi   ◉ Netral'%(H,P,M,P))
        print('')
        kelamin   = input('%s[%s•%s] %sAkun Laki/Perempuan/Random [%sl%s/%sp%s/%sr%s] : '%(M,P,M,P,H,P,H,P,M,P)).lower()
        namanama  = input('%s[%s•%s] %sGunakan Nama Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,M,P,H,P)).lower()
        if namanama in ['m','manual','0','00']:
            namstat = 'Manual'
            nameme = input(' %s└─ %sNama : %s'%(M,P,M)).split(',')
        else:
            namstat = 'Random'
        print('%s[%s•%s] %sEmail CryptoGmail/SecMail/TempMail/MinuteMail'%(M,P,M,P))
        web_email = input(' %s└─ %s[c/s/t/m] [skip=MinuteMail] : '%(M,P)).lower()
        update    = input('%s[%s•%s] Auto Update Info Akun %s[%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        tampil    = input('%s[%s•%s] %sTampilkan Akun CP [%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        print('%s[%s•%s] %sUser Agent Vivo/Samsung/Realme/Manual'%(M,P,M,P))
        useragent = input(' %s└─ %s[v/s/r/m] [skip=statis] : '%(M,P)).lower()
        if useragent in ['m','manual','0','00']:
            uman = input(' %s└─ %sUser Agent : %s'%(M,P,M))
            if uman == '' or uman == ' ':
                exit('%sIsi Yang Benar!%s'%(M,P))
        else:
            uman = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
        passtat   = input('%s[%s•%s] %sGunakan Password Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,H,P,M,P)).lower()
        if passtat in ['m','manual','b','2','02']:
            password = input(' %s└─ %sPassword : %s'%(M,P,M))
            if len(password) < 6:
                exit('%sPassword Minimal 6 Digit!%s'%(M,P))
            if password in ['akusayangkamu','123456','iloveyou','password','qwerty','sayang','anjing','bismillah']:
                exit('%sGunakan Password Yang Kuat!%s'%(M,P))
        else:
            password = 'dapuntaloverani'
        d = input('%s[%s•%s] %sBeri Delay (%sDalam Menit%s) : '%(M,P,M,P,M,P))
        if d == '' or d == ' ':
            d = 1
        print('')
        l = int(d)*60
        for y in range(10000):
            create_fb()
            self.hitung(l)
    def hitung(self,a):
        for x in range(a+1):
            print('\r[%sOK:%s%s] [%sCP:%s%s] Tunggu %s Detik         '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Create Facebook Account
class create_fb:

    #--> Tampung Kabeh
    def __init__(self):
        self.file  = 'Akun_New/%s.txt'%(waktu())
        self.abc = requests.Session() #--> Sesi Email
        self.xyz = requests.Session() #--> Sesi Facebook
        self.abc.cookies.clear()
        self.xyz.cookies.clear()
        if   useragent in ['v','vivo','1','01','a']:    self.ua = random_ua_vivo()
        elif useragent in ['s','samsung','2','02','b']: self.ua = random_ua_samsung()
        elif useragent in ['r','realme','3','03','c']:  self.ua = random_ua_realme()
        elif useragent in ['m','manual','0','00','z']:  self.ua = random_ua_custom()
        else : self.ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
        self.head_email = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'}
        self.ua_wind = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.headers_get = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, image/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : self.ua}
        self.generate_data()
        self.scrap1()

    #--> Generate Data
    def generate_data(self):
        self.name, soex = self.get_name().split('|')
        self.nope  = self.get_nope()
        if   web_email in ['c','cryptogmail','1','01','a']: self.email = self.get_email_cryptogmail()
        elif web_email in ['s','secmail','2','02','b']:     self.email = self.get_email_onesecmail()
        elif web_email in ['t','tempmail','3','03','c']:    self.email = self.get_email_tempmailio()
        elif web_email in ['m','minutemail','4','04','d']:  self.email = self.get_email_10minutemail()
        else : self.email = self.get_email_10minutemail()
        if soex == 'male' : self.sex = '2'
        else : self.sex = '1'
        if passtat in ['m','manual','b','2','02']: self.pw = password
        else: self.pw = self.get_pass()
        self.ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1970,2001))}
        self.perangkat = '; m_pixel_ratio=3; dpr=1.125; wd=360x650; locale=id_ID;'
    
    #--> Generate Random Name
    def get_name(self):
        if kelamin in ['l','laki','1','01','a']: gder = 'male'
        elif kelamin in ['p','perempuan','2','02','b']: gder = 'female'
        else: gder = random.choice(['male','female'])
        try:
            if gder == 'male':
                if namstat == 'Manual': name = random.choice(nameme)
                else: name = random.choice(boys_name)
            else:
                if namstat == 'Manual': name = random.choice(nameme)
                else: name = random.choice(girls_name)
        except Exception as e:
            nam1 = random.choice(['Eka','Dwi','Tri','Budi','Indah','Dewi'])
            nam2 = random.choice(['Nurhayati','Handoko','Setiyani','Susanto','Permata'])
            nam3 = random.choice(['Triatmaja','Siagian','Manopo','Jayaningrat','Widodo'])
            name = f'{nam1} {nam2} {nam3}'
        klop = f'{name}|{gder}'
        return(klop)

    #--> Generate Random Phone Number
    def get_nope(self):
        na   = random.choice(['12','22','52','77','78','59'])
        ni   = str(random.randrange(1000,10000))
        nu   = str(random.randrange(10000,100000))
        nope = '08%s%s%s'%(na,ni,nu)
        return(nope)

    #--> Generate Random Password
    def get_pass(self):
        up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lw = up.lower()
        nb = '0123456789'
        ch = up + lw + nb
        pw = ''.join(random.choice(ch) for _ in range(12))
        return(pw.lower())

    #--> Generate Email & Code From Cryptogmail
    def get_email_cryptogmail(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['fexbox.org','chitthi.in','fextemp.com','any.pink','merepost.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        return(email)
    def get_code_cryptogmail(self):
        url = f'https://tempmail.plus/api/mails?email={self.email}'
        req = self.abc.get(url,headers=self.head_email).json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From 1SecMail
    def get_email_onesecmail(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['1secmail.com','1secmail.org','1secmail.net','kzccv.com','qiott.com','wuuvo.com','icznn.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        return(email)
    def get_code_onesecmail(self):
        name, domain = self.email.split('@')
        req = self.abc.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}').json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From Temp-Mail.io
    def get_email_tempmailio(self):
        pos = self.abc.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
        email = pos['email']
        return(email)
    def get_code_tempmailio(self):
        req = self.abc.get(f'https://api.internal.temp-mail.io/api/v3/email/{self.email}/messages').json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From 10minutemail
    def get_email_10minutemail(self):
        req = bs(self.abc.get('https://10minutemail.net/m/?lang=id',headers=self.head_email,allow_redirects=True).content,'html.parser')
        self.ses_email = re.search('sessionid="(.*?)"',str(req)).group(1)
        self.tim_email = str(time.time()).replace('.','')[:13]
        dat = {'new':'1','sessionid':self.ses_email,'_':self.tim_email}
        pos = self.abc.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,allow_redirects=True).json()
        email = pos['mail_get_mail']
        self.cookie_email = '; '.join([str(x)+"="+str(y) for x,y in self.abc.cookies.get_dict().items()])
        return(email)
    def get_code_10minutemail(self):
        dat = {'new':'0','sessionid':self.ses_email,'_':self.tim_email}
        pos = self.abc.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,cookies={'cookie':self.cookie_email},allow_redirects=True).json()
        kode = re.search(r'FB-([^ ]+)',str(pos)).group(1)
        return(kode)

    #--> Create Facebook Route
    def scrap1(self): #--> Post Login Awal
        try: get = self.xyz.get('https://www.facebook.com/',headers=self.headers_get.update({'user-agent':self.ua_wind}))
        except Exception as e: pass
        req = bs(self.xyz.get('https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk',headers=self.headers_get).content,'html.parser')
        fom = req.find('form',{'method':'post'})
        teme = re.search('"__spin_t":(.*?),',str(req)).group(1)
        publ = re.search('publicKey:"(.*?)",',str(req)).group(1)
        pubk = re.search('keyId:([0-9]+)',str(req)).group(1)
        rdb = RDM.get_random_bytes((len(auth1)-2)*2)
        dpt = AES.new(rdb, AES.MODE_GCM, nonce=bytes([0]*(len(auth1)-6)), mac_len=len(auth1)-2)
        dpt.update(str(teme).encode("utf-8"))
        epw, ctg = dpt.encrypt_and_digest(self.pw.encode("utf-8"))
        sld = SB(PK(binascii.unhexlify(str(publ)))).encrypt(rdb)
        ecp = base64.b64encode(bytes([1,int(pubk),*list(struct.pack('<h', len(sld))),*list(sld),*list(ctg),*list(epw)])).decode("utf-8")
        encp = '#PWD_BROWSER:%s:%s:%s'%(str(len(auth1)-13),teme,str(ecp))
        lsd = re.search('name="lsd" type="hidden" value="(.*?)"',str(fom)).group(1)
        data = {
            'lsd':lsd,'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)",',str(req)).group(1),'ccp':re.search('name="ccp" type="hidden" value="(.*?)"',str(fom)).group(1),'reg_instance':re.search('name="reg_instance" type="hidden" value="(.*?)"',str(fom)).group(1),'reg_impression_id':re.search('name="reg_impression_id" type="hidden" value="(.*?)"',str(fom)).group(1),'ns':re.search('name="ns" type="hidden" value="(.*?)"',str(fom)).group(1),'app_id':re.search('name="app_id" type="hidden" value="(.*?)"',str(fom)).group(1),'logger_id':re.search('name="logger_id" type="hidden" value="(.*?)"',str(fom)).group(1),
            'suma_create_event':'suma_redirection_click_create_account','field_names[0]':'firstname','field_names[1]':'birthday_wrapper','field_names[2]':'reg_email__','field_names[3]':'sex','field_names[4]':'reg_passwd__','is_birthday_confirmed':'confirmed','multi_step_form':'1','skip_suma':'0','shouldForceMTouch':'1','__user':'0','ref':'dbl',
            'firstname':self.name,'reg_email__':self.nope,'sex':self.sex,'reg_passwd__':self.pw,'encpass':encp,'birthday_day':self.ttl['tgl'],'birthday_month':self.ttl['bln'],'birthday_year':self.ttl['thn'],
            'welcome_step_completed':True,'submission_request':True,'did_use_age':False,'name_suggest_elig':False,'was_shown_name_suggestions':False,'did_use_suggested_name':False,'use_custom_gender':False,
            'custom_gender':'','age_step_input':'','zero_header_af_client':'','helper':'','guid':'','pre_form_step':'','preferred_pronoun':'','korean_tos_is_present':'','checkbox_privacy_policy':'','checkbox_tos':'','checkbox_location_policy':'','submit':'Daftar'}
        rs = '; rs=%s|%s|%s|%s|%s|%s|%s|%s|3|||1'%(str(self.ttl['tgl']),str(self.ttl['bln']),str(self.ttl['thn']),str(self.sex),str(self.nope),str(self.name).split(' ')[0],str(self.name).split(' ')[-1],str(self.name).replace(' ','+'),)
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+rs+self.perangkat
        head_post = {'accept':'*/*','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-length':str(random.randrange(1200,1400)),'content-type':'application/x-www-form-urlencoded','cookie':cok,'origin':'https://m.facebook.com','referer':'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk','sec-ch-prefers-color-scheme':'light','sec-ch-ua':'"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list':'"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-ch-ua-platform-version':'"11.0.0"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':self.ua,'viewport-width':'360','x-asbd-id':'129477','x-fb-lsd':lsd,}
        pos = bs(self.xyz.post('https://m.facebook.com'+fom['action'],data=data,headers=head_post,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        if pos.find('title').text == 'Konfirmasikan Akun Anda': self.scrap4()
        else:
            rog = pos.find('form',{'method':'post'})
            if 'login/device-based/update-nonce' in str(rog['action']): self.scrap2(rog)
            elif 'conf/notifmedium/send_code' in str(rog['action']): self.scrap3(rog)
            elif 'checkpoint' in str(rog['action']): self.printing('CP')
            else: print('\rTerjadi Kesalahan                    ',end='');sys.stdout.flush()
    def scrap2(self,fom): #--> Save Device OK
        print('\rLolos Tahap 1                    ',end='');sys.stdout.flush()
        try:
            data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),'flow':'interstitial_nux','next':'','nux_source':'dbl_nux_after_reg','submit':'OK'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+self.perangkat
            pos = bs(self.xyz.post('https://m.facebook.com'+fom['action'],data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser').find('form',{'method':'post'})
            self.scrap3(pos)
        except Exception as e: self.printing('CP')
    def scrap3(self,fom): #--> Minta Kode Nope
        print('\rLolos Tahap 2                    ',end='');sys.stdout.flush()
        try:
            data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),'medium':'sms','submit':'Kirim kode'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+self.perangkat
            pos = bs(self.xyz.post('https://m.facebook.com' + fom['action'],data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            self.scrap4()
        except Exception as e: self.printing('CP')
    def scrap4(self): #--> Add Email
        print('\rLolos Tahap 3                    ',end='');sys.stdout.flush()
        try:
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+self.perangkat
            req = bs(self.xyz.get('https://m.facebook.com/changeemail/',headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser').find('form',{'method':'post'})
            data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'old_email':re.search('name="old_email" type="hidden" value="(.*?)"',str(req)).group(1),'reg_instance':re.search('name="reg_instance" type="hidden" value="(.*?)"',str(req)).group(1),'new':self.email,'next':'','submit':'Tambahkan'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+self.perangkat
            pos = bs(self.xyz.post('https://m.facebook.com' + req['action'],data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            tunggu_kode(30); self.scrap5(pos)
        except Exception as e: self.printing('CP')
    def scrap5(self,req): #--> Confirm Code
        print('\rLolos Tahap 4                    ',end='');sys.stdout.flush()
        try:
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+self.perangkat
            if   web_email in ['c','cryptogmail','1','01','a']: code = self.get_code_cryptogmail()
            elif web_email in ['s','secmail','2','02','b']:     code = self.get_code_onesecmail()
            elif web_email in ['t','tempmail','3','03','c']:    code = self.get_code_tempmailio()
            elif web_email in ['m','minutemail','4','04','d']:  code = self.get_code_10minutemail()
            else : code = self.get_code_10minutemail()
            data = {'contact':self.email,'type':'submit','is_soft_cliff':False,'medium':'email','code':code,'fb_dtsg':re.search('"dtsg":{"token":"(.*?)",',str(req)).group(1),'jazoest':re.search('"jazoest", "(.*?)",',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1),'__user':re.search('c_user=(.*?);',cok).group(1)}
            pos = bs(self.xyz.post('https://m.facebook.com/confirmation_cliff/',data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            self.semi_final()
        except Exception as e: self.printing('CP')
    def zero_optin(self): #--> Khusus Mode Data (No Wifi)
        try:
            cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req = bs(self.xyz.get('https://mbasic.facebook.com',headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
            nek = ['https://m.facebook.com'+x['href'] for x in req.find_all('a',href=True) if 'dialtone_optin_page' in str(x['href'])][0]
            cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            raq = bs(self.xyz.get(nek,headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser').find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),'submit':'OK, use data'}
            cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            pos = self.xyz.post('https://m.facebook.com' + raq['action'],data=dat,headers=self.headers_get,cookies={'cookie':cok})
            print('\rBerhasil Skip Free Mode                ',end='');sys.stdout.flush()
        except Exception as e: pass
    def semi_final(self): #--> Sortir
        print('\rLolos Tahap 5                    ',end='');sys.stdout.flush()
        try:
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])+self.perangkat
            id = re.search('c_user=(.*?);',cok).group(1)
            self.zero_optin()
            if update in ['1','01','y','a']:
                #--> Ubah Bot Disini
                if self.sex == '2': self.foto = random.choice(['https://e.top4top.io/p_27410eyrw1.jpg','https://i.pinimg.com/736x/47/cb/b4/47cbb446dd61bfb03308af7dbefdba06.jpg','https://i.pinimg.com/736x/b5/13/22/b51322eeaa2b35fac59444ebde6d8d2f.jpg','https://i.pinimg.com/736x/58/07/ba/5807ba1c263caaa5bbe0639d24ada8e2.jpg','https://i.pinimg.com/736x/72/bd/33/72bd338d114cec8922c14bd98322cf8a.jpg','https://i.pinimg.com/736x/c1/3d/21/c13d2188ceed1679fa2b8963031bc3e6.jpg'])
                else: self.foto = random.choice(['https://d.top4top.io/p_2741lrx800.jpg','https://i.pinimg.com/736x/80/8c/97/808c97eb9c7e017964857b957c125917.jpg','https://i.pinimg.com/736x/f8/a0/da/f8a0da275c48b03550990d3cd27d4eb6.jpg','https://i.pinimg.com/736x/7b/66/55/7b66559151d8c0f50892e27175e5c1d3.jpg','https://i.pinimg.com/736x/6b/00/fe/6b00feaa363d752a4020e55437ba0308.jpg','https://i.pinimg.com/736x/44/b0/7e/44b07e3d57a24bacc0b44b3fb4333908.jpg','https://i.pinimg.com/736x/14/b4/35/14b435422805ff41ecf6688ca67fd132.jpg','https://i.pinimg.com/736x/b6/14/93/b61493683fad328b87b54836226b6eb8.jpg','https://i.pinimg.com/736x/1b/9c/fb/1b9cfbd592dcfc682a14b93698b01e1c.jpg','https://i.pinimg.com/736x/98/ff/d7/98ffd7873189fd7ec7121b4de9cccd09.jpg','https://i.pinimg.com/736x/30/cc/11/30cc11c3453294bca7d657f490e2393a.jpg'])
                self.web = 'https://github.com/Dapunta'
                self.comment = 'Semangat Kuliahnya Mas Dapunta!'
                self.account_follow = ['1827084332','100000415317575','100000721771295','100093403210005']
                self.create = ['Hello World!','Salam Kenal Semuanya!']
                self.postid = ['6911595132197595']
                self.listgrup = ['1824553201274304']
                self.react = 1
                self.rl = '2'
                city = 'Yogyakarta'
                self.cookie = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
                if check_account(id) == 'OK':
                    self.kota('https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown','hometown','hometown[]',city)
                    self.kota('https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city','current_city','current_city[]',city)
                    self.website()
                    self.relationship()
                    self.auto_follow()
                    self.auto_react()
                    self.auto_comment()
                    self.join_grup()
                    self.profil()
                    self.cover()
                    self.bio()
                    self.auto_post()
                    # self.logout()
                else: pass
            jeda(10)
            final = check_account(id)
            if final == 'OK': self.printing('OK')
            else: self.printing('CP')
        except Exception as e:
            self.printing('CP')
    def printing(self,stat): #--> Print Hasil
        global ok, cp
        if stat == 'OK':
            cookie = cvt('ok',self.xyz.cookies.get_dict())
            id = self.xyz.cookies.get_dict()['c_user']
            print('\r%sStatus : %sSuccess%s                         '%(P,H,P))
            print('Nama   : %s'%(str(self.name)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(self.pw)))
            print('Email  : %s'%(str(self.email)))
            print('TTL    : %s %s %s'%(self.ttl['tgl'],bulan[self.ttl['bln']],self.ttl['thn']))
            if update in ['1','01','y','a']: print('Action : PP, PS, Bio, Follow, Comment, React')
            print('Cookie : %s\n'%(str(cookie)))
            open(self.file,'a+').write('%s|%s|%s|%s\n'%(self.name,id,self.email,self.pw))
            ok += 1
        else:
            if tampil in ['t','2','02','b']: pass
            else:
                print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
                print('Nama   : %s'%(str(self.name)))
                print('Nope   : %s'%(str(self.nope)))
                print('Pass   : %s\n'%(str(self.pw)))
            cp += 1

    #--> Auto Update Data Akun
    def profil(self): #--> Edit Foto Profil
        try:
            print('\rSedang Pasang Foto Profil                    ',end='');sys.stdout.flush()
            fot = urllib.request.urlopen(self.foto)
            req = bs(self.xyz.get('https://mbasic.facebook.com/photos/upload/?profile_pic&entrypoint=timeline_change_profile_photo',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {x['name']:x['value'] for x in req.find_all('input',{'name':True,'value':True})}
            pos = bs(self.xyz.post(req['action'],data=dat,files={'file1':fot},cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Pasang Foto Profil                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def cover(self): #--> Edit Foto Sampul
        try:
            print('\rSedang Pasang Foto Sampul                    ',end='');sys.stdout.flush()
            fot = urllib.request.urlopen(self.foto)
            req = bs(self.xyz.get('https://mbasic.facebook.com/photos/upload/?cover_photo',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {x['name']:x['value'] for x in req.find_all('input',{'name':True,'value':True})}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,files={'file1':fot},cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Pasang Foto Sampul                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def bio(self): #--> Edit Bio
        try:
            print('\rSedang Update Bio                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get('https://mbasic.facebook.com/profile/basic/intro/bio/',cookies={'cookie':self.cookie}).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),'bio':self.name,'publish_to_feed':True,'submit':'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Update Bio                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def kota(self,url,a,b,kota): #--> Edit Kota Asal & Tempat Tinggal
        try:
            print('\rSedang Edit Kota                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get(url,cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'edit':a,'type':'basic',b:kota,'save':'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Edit Kota                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def website(self): #--> Edit Website
        try:
            print('\rSedang Edit Website                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get('https://mbasic.facebook.com/editprofile.php?type=contact&edit=website',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'type':'contact','edit':'website','add_website':'1','new_info':self.web,'save':'Tambahkan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Edit Website                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def relationship(self): #--> Auto Show Relationship
        try:
            print('\rSedang Edit Relationship                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get(f'https://mbasic.facebook.com/editprofile.php?type=basic&edit=relationship&action={self.rl}',cookies={'cookie':self.cookie}).content,'html.parser')
            raq = [fom for fom in req.find_all('form',{'action':True}) if '/a/editprofile.php?' in fom['action']][0]
            data = {i['name']: i['value'] for i in raq.find_all('input', {'name': True, 'value': True})}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Edit Relationship                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def join_grup(self): #--> Auto Join Grup
        for grup in self.listgrup:
            try:
                print('\rSedang Bergabung Ke Grup %s                    '%(grup),end='');sys.stdout.flush()
                req = bs(self.xyz.get(f'https://mbasic.facebook.com/groups/{grup}',cookies={'cookie':self.cookie}).content,'html.parser')
                raq = [fom for fom in req.find_all('form',{'action':True}) if 'a/group/join/?group_id' in fom['action']][0]
                data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),'submit':'Join Group'}
                pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
                print('\rBerhasil Bergabung Ke Grup %s                    '%(grup),end='');sys.stdout.flush()
            except Exception as e: pass
    def auto_follow(self): #--> Auto Follow
        for x in self.account_follow:
            try:
                print('\rSedang Follow Akun %s                    '%(x),end='');sys.stdout.flush()
                req = bs(self.xyz.get(f'https://mbasic.facebook.com/profile.php?id={x}',cookies={'cookie':self.cookie}).content,'html.parser')
                raq = [x for x in req.find_all('a',href=True) if '/a/subscribe.php' in x['href']][0]
                get = self.xyz.get('https://mbasic.facebook.com'+raq['href'],cookies={'cookie':self.cookie})
                print('\rBerhasil Follow Akun %s                    '%(x),end='');sys.stdout.flush()
            except Exception as e: pass
    def auto_react(self): #--> Auto React
        for post in self.postid:
            try:
                print('\rSedang React Post %s                    '%(post),end='');sys.stdout.flush()
                req = bs(self.xyz.get(f'https://mbasic.facebook.com/photo.php?fbid={post}',cookies={'cookie':self.cookie}).content,'html.parser')
                get = ['https://mbasic.facebook.com' + x['href'] for x in req.find_all('a',href=True) if '/reactions/picker/?is_permalink=1' in str(x['href'])][0]
                raq = bs(self.xyz.get(get,cookies={'cookie':self.cookie}).content,'html.parser')
                rek = ['https://mbasic.facebook.com' + x['href'] for x in raq.find_all('a',href=True) if '/ufi/reaction/?ft_ent_identifier' in str(x['href'])]
                exe = bs(self.xyz.get(rek[self.react],cookies={'cookie':self.cookie}).content,'html.parser')
                print('\rBerhasil React Post %s                    '%(post),end='');sys.stdout.flush()
            except Exception as e: pass
    def auto_comment(self): #--> Auto Comment
        try:
            for post in self.postid:
                print('\rSedang Mengomentari Post %s                   '%(post),end='');sys.stdout.flush()
                for x in range(10):
                    try:
                        req = bs(self.xyz.get(f'https://mbasic.facebook.com/mbasic/comment/advanced/?target_id={post}&pap=1&at=compose&photo_comment=1',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
                        data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'comment_text':self.comment,'post':'Comment'}
                        pos = bs(self.xyz.post(req['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
                    except Exception as e: pass
        except Exception as e: pass
    def auto_post(self): #--> Auto Post
        for capt in self.create:
            try:
                print('\rSedang Membuat Post                    ',end='');sys.stdout.flush()
                req = bs(self.xyz.get('https://mbasic.facebook.com/profile.php?',cookies={'cookie':self.cookie}).content,'html.parser')
                raq = [fom for fom in req.find_all('form',{'action':True}) if '/composer/mbasic/' in fom['action']][0]
                data = {i['name']: i['value'] for i in raq.find_all('input', {'name': True, 'value': True})}
                data.update({'rst_icv':'','view_privacy':'Public','privacyx':'300645083384735','xc_message':capt})
                for x in ['view_photo','view_mle','view_overview']:
                    try: data.pop(x)
                    except Exception as e: pass
                pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
                print('\rBerhasil Membuat Post                    ',end='');sys.stdout.flush()
            except Exception as e: pass
    def logout(self): #--> Logout Manual
        try:
            print('\rSedang Logout                    ',end='');sys.stdout.flush()
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req = bs(self.xyz.get('https://mbasic.facebook.com/me',cookies={'cookie':cok}).content,'html.parser')
            url = ['https://mbasic.facebook.com'+x['href'] for x in req.find_all('a',href=True) if 'logout.php' in str(x['href'])][0]
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            roq = self.xyz.get(url,cookies={'cookie':cok})
            print('\rBerhasil Logout                    ',end='');sys.stdout.flush()
        except Exception as e: pass

#--> Menu Checker Account
class menu_check:
    def __init__(self): #--> Mengecek Ketersediaan Folder
        self.xyz = requests.Session()
        self.file = {}
        self.isi = 0
        self.ok  = 0
        self.cp  = 0
        f = 'Akun_New'
        if os.path.isdir(f):
            p = 0
            l = os.listdir(f)
            for y in l:
                p += 1
                self.file.update({str(p):y})
                c = '%s• %s%s'%(M,P,y)
                print(c)
            self.sortir()
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
    def sortir(self): #--> Memilih File
        try:
            d = input('\n%s[%s•%s] %sMasukkan File : '%(M,P,M,P))
            if d in ['pack','Pack','PACK']: self.new = True; self.pack()
            else:
                self.new = False
                if d in list(self.file.keys()): l = 'Akun_New/%s'%(self.file[d])
                else: l = 'Akun_New/%s'%(d)
                g = open(l,'r').read().splitlines()
                print('')
                for a in g:
                    try:
                        nama, id, email, pw = a.split('|')
                        stat = check_account(id)
                        if stat == 'OK': self.printing('OK',nama,id,email,pw)
                        else: self.printing('CP',nama,id,email,pw)
                    except Exception as e: pass
                if self.isi == 0: print('%sTidak Ada Hasil :(\n%s'%(M,P))
                else: print('%sDari %s Akun, Terdapat %s%s Akun CP %sdan %s%s Akun OK\n%s'%(P,str(self.isi),M,str(self.cp),P,H,str(self.ok),P))
        except Exception as e:
            print('%sError : %s'%(P,e))
            print('%sTerjadi Kesalahan!\n%s'%(M,P))
    def pack(self): #--> Packing Akun Aktif Jadi Satu
        new = input('%s[%s•%s] %sNama File Baru : '%(M,P,M,P))
        print('')
        self.nwf = 'Akun_New/%s.txt'%(new)
        open(self.nwf,'a+')
        for f in os.listdir('Akun_New'):
            try:
                lt = open('Akun_New/%s'%(f),'r').read().splitlines()
                for dt in lt:
                    try:
                        nama, id, email, pw = dt.split('|')
                        stat = check_account(id)
                        if stat == 'OK': self.printing('OK',nama,id,email,pw)
                        else: self.printing('CP',nama,id,email,pw)
                    except Exception as e: pass
            except Exception as e: pass
    def printing(self,stat,nama,id,email,pw): #--> Print Hasil Cek
        if stat == 'OK':
            print('\r%sStatus : %sSuccess%s                         '%(P,H,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s\n'%(str(email)))
            if self.new == True: open(self.nwf,'a+').write('%s|%s|%s|%s\n'%(nama,id,email,pw))
            self.ok += 1
        else:
            print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s\n'%(str(email)))
            self.cp += 1
        self.isi += 1

#--> Setting Bot
class setting_bot:
    def __init__(self):
        try:os.mkdir('Setting_Create_FB')
        except Exception as e :pass
        self.file = 'Setting_Create_FB/my_set.txt'
        self.datata()
        clear()
        menu()
    def datata(self):
        #--> User Agent
        print('%s[%s•%s] %sMasukkan User Agent Perangkatmu'%(M,P,M,P))
        ua = input(' %s└─ '%(M))
        if ua == '' or ua == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Foto Profil
        print('%s[%s•%s] %sMasukkan URL Foto Profil'%(M,P,M,P))
        a = input(' %s└─ '%(M))
        if a == '' or a == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Foto Sampul
        print('%s[%s•%s] %sMasukkan URL Foto Sampul'%(M,P,M,P))
        b = input(' %s└─ '%(M))
        if b == '' or b == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Bio
        print('%s[%s•%s] %sTulis Bio'%(M,P,M,P))
        c = input(' %s└─ '%(M))
        if c == '' or c == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Kota
        print('%s[%s•%s] %sMasukkan Kota'%(M,P,M,P))
        e = input(' %s└─ '%(M))
        if e == '' or e == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Website
        print('%s[%s•%s] %sMasukkan Situs Website'%(M,P,M,P))
        f = input(' %s└─ '%(M))
        if f == '' or f == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Relationship
        print('%s[%s•%s] %sPilih Relationship : Single, Pacaran, Menikah'%(M,P,M,P))
        r = input(' %s└─ [s/p/m] : '%(M)).lower()
        if   r == '' or r == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        elif r == 's' or r == 'single'  or r == '1': rl = '1'
        elif r == 'p' or r == 'pacaran' or r == '2': rl = '2'
        elif r == 'm' or r == 'menikah' or r == '3': rl = '4'
        else: rl = '0'
        #--> Group
        print('%s[%s•%s] %sMasukkan ID Grup Yang Akan Dimasuki'%(M,P,M,P))
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        j = input(' %s└─ '%(M)).split(',')
        if j == '' or j == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Follow
        print('%s[%s•%s] %sMasukkan Akun Yg Mau Difollow'%(M,P,M,P))
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        d = input(' %s└─ '%(M)).split(',')
        if d == '' or d == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> ID Post
        print('%s[%s•%s] %sMasukkan ID Post Yg Mau Direact + Komen'%(M,P,M,P))
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        g = input(' %s└─ '%(M)).split(',')
        if g == '' or g == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> React
        print('%s[%s•%s] %sReaksi : Like, Love, Care, Haha, Wow, Sad, Angry'%(M,P,M,P))
        h = str(int(input(' %s└─ %s[1/2/3/4/5/6/7] %s: '%(M,P,M)))-1)
        if h == '' or h == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        elif int(h) < 0 or int(h) > 6: exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Comment
        print('%s[%s•%s] %sTulis Komentar Tunggal'%(M,P,M,P))
        i = input(' %s└─ '%(M))
        if i == '' or i == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> Post
        print('%s[%s•%s] %sTulis Caption Untuk Dipost'%(M,P,M,P))
        print('%s[%s•%s] %sBanyak Post, Pisahkan Dgn (|)'%(M,P,M,P))
        cr = input(' %s└─ '%(M)).split('|')
        if cr == '' or cr == ' ': exit('%sIsi Yang Benar!%s'%(M,P))
        #--> String Data
        dt = "{'ua':'%s','pp':'%s','ps':'%s','bio':'%s','akun':%s,'kota':'%s','web':'%s','post':%s,'react':%s,'com':'%s','grup':%s,'rl':'%s','create':%s}"%(str(ua),str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i),str(j),str(rl),str(cr))
        open(self.file,'w').write('')
        open(self.file,'w').write(dt)
        input('\n%s[ %sEnter %s]%s'%(M,P,M,P))

#--> Menu Bot Akun
class bot_account:
    def __init__(self): #--> Tampung Data
        try:
            data = eval(open('Setting_Create_FB/my_set.txt','r').read())
            self.ua       = data['ua']
            self.foto_pp  = data['pp']
            self.foto_ps  = data['ps']
            self.nama_bio = data['bio']
            self.city     = data['kota']
            self.web      = data['web']
            self.rl       = data['rl']
            self.listgrup = data['grup']
            self.accfoll  = data['akun']
            self.postid   = data['post']
            self.react    = data['react']
            self.comment  = data['com']
            self.create   = data['create']
            print('%s[%s1%s] %sEdit Profil    %s[%s5%s] %sEdit Kota     %s[%s9%s]  %sBot Follow%s'%(M,P,M,P,M,P,M,P,M,P,M,P,P))
            print('%s[%s2%s] %sEdit Sampul    %s[%s6%s] %sEdit Website  %s[%s10%s] %sBot React%s'%(M,P,M,P,M,P,M,P,M,P,M,P,P))
            print('%s[%s3%s] %sEdit Bio       %s[%s7%s] %sRelationship  %s[%s11%s] %sBot Comment%s'%(M,P,M,P,M,P,M,P,M,P,M,P,P))
            print('%s[%s4%s] %sProfile Guard  %s[%s8%s] %sJoin Grup     %s[%s12%s] %sBot Post%s'%(M,P,M,P,M,P,M,P,M,P,M,P,P))
            print('%s[%s•%s] %sPilih Sekaligus (Ex:1,2,3,4,5)'%(M,P,M,P))
            self.pilih = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).split(',')
            print('\n%s[%s•%s] %sList Akun Dari File/Manual'%(M,P,M,P))
            pil = input(' %s└─ %s[f/m] %s: %s'%(M,P,M,P)).lower()
            print('')
            if pil in ['f','file','1','01']: self.execute_file()
            elif pil in ['m','manual','2','01']: self.execute_tunggal()
            else: exit('%sIsi Yang Benar!%s'%(M,P))
        except Exception as e:
            print('%s[%s!%s] Anda Belum Menyeting Bot!%s'%(M,P,M,P))
            print('%s[%s!%s] %sSetting Terlebih Dahulu Agar Bisa Menggunakannya'%(M,P,M,P))
            time.sleep(5)
            clear()
            menu()
    def execute_tunggal(self): #--> Execute Akun Tunggal
        wey = []
        lop = int(input('%s[%s•%s] %sBerapa ID Yg Ingin Dibot : %s'%(M,P,M,P,M)))
        print('%s[%s•%s] %sContoh Format : 100093403210005|password'%(M,P,M,P))
        for x in range(lop):
            lip = input('    %sID|Pass %s : '%(M,str(x+1)))
            cek = check_nama_account(lip.split('|')[0])
            if cek['stat'] == 'CP': pass
            else: wey.append('%s|%s|Unknown|%s'%(cek['name'],lip.split('|')[0],lip.split('|')[1]))
        print('%s'%(P))
        for y in wey:
            try:
                nama, id, email, pw = y.split('|')
                self.login(nama,id,email,pw)
            except Exception as e: pass
    def execute_file(self): #--> Execute Akun Dari Folder
        self.file = {}
        f = 'Akun_New'
        if os.path.isdir(f):
            p = 0
            l = os.listdir(f)
            for y in l:
                p += 1
                self.file.update({str(p):y})
                c = '%s• %s%s'%(M,P,y)
                print(c)
            self.sortir()
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
    def sortir(self): #--> Memilih File
        try:
            d = input('\n%s[%s•%s] %sMasukkan File : '%(M,P,M,P))
            if d in list(self.file.keys()): l = 'Akun_New/%s'%(self.file[d])
            else: l = 'Akun_New/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g:
                try:
                    nama, id, email, pw = a.split('|')
                    final = check_account(id)
                    if final == 'OK': self.login(nama,id,email,pw)
                    else: self.printing('CP',nama,id,email,pw)
                except Exception as e: pass
            print('%s[%s•%s] %sProses Selesai :)%s\n'%(H,P,H,P,P))
        except Exception as e:
            print('%sError : %s'%(P,e))
            print('%sTerjadi Kesalahan!\n%s'%(M,P))
    def login(self,nama,id,email,pw): #--> Login
        self.perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'
        self.xyz = requests.Session()
        host = 'mbasic.facebook.com'
        head_get = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':None,'Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        url_get = f'https://{host}/login/device-based/password/?uid={id}&flow=login_no_pin'
        req = bs(self.xyz.get(url_get,headers=head_get).content,'html.parser').find('form',{'method':'post'})
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
        head_post = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Content-Type':'application/x-www-form-urlencoded','Origin':f'https://{host}','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Referer':f'https://{host}/login/device-based/password/?uid={id}&flow=login_no_pin','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        url_post = 'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0'
        data = {'shbl': '0','lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'uid': id,'next': 'https://mbasic.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
        pos = self.xyz.post(url_post,data=data,headers=head_post,cookies={'cookie':cok},allow_redirects=True)
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
        if 'checkpoint' in str(pos.text): self.printing('CP',nama,id,email,pw)
        else:
            self.cookie = cok
            if self.nama_bio == 'nama': newbio = nama
            else: newbio = self.nama_bio
            for x in self.pilih:
                if x   == '1': self.profil()
                elif x == '2': self.cover()
                elif x == '3': self.bio(newbio)
                elif x == '4': self.profile_guard(id)
                elif x == '5': self.kota('https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown','hometown','hometown[]',self.city); self.kota('https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city','current_city','current_city[]',self.city)
                elif x == '6': self.website()
                elif x == '7': self.relationship()
                elif x == '8': self.join_grup()
                elif x == '9': self.auto_follow()
                elif x == '10': self.auto_react()
                elif x == '11': self.auto_comment()
                elif x == '12': self.auto_post()
                elif x == '0': self.logout()
                else: pass
            jeda(10)
            final = check_account(id)
            if final == 'OK': self.printing('OK',nama,id,email,pw)
            else: self.printing('CP',nama,id,email,pw)
        self.xyz.close()
    def profil(self): #--> Edit Foto Profil
        try:
            print('\rSedang Pasang Foto Profil                    ',end='');sys.stdout.flush()
            fot = urllib.request.urlopen(self.foto_pp)
            req = bs(self.xyz.get('https://mbasic.facebook.com/photos/upload/?profile_pic&entrypoint=timeline_change_profile_photo',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {x['name']:x['value'] for x in req.find_all('input',{'name':True,'value':True})}
            pos = bs(self.xyz.post(req['action'],data=dat,files={'file1':fot},cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Pasang Foto Profil                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def cover(self): #--> Edit Foto Sampul
        try:
            print('\rSedang Pasang Foto Sampul                    ',end='');sys.stdout.flush()
            fot = urllib.request.urlopen(self.foto_ps)
            req = bs(self.xyz.get('https://mbasic.facebook.com/photos/upload/?cover_photo',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {x['name']:x['value'] for x in req.find_all('input',{'name':True,'value':True})}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,files={'file1':fot},cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Pasang Foto Sampul                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def bio(self,newbio): #--> Edit Bio
        try:
            print('\rSedang Update Bio                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get('https://mbasic.facebook.com/profile/basic/intro/bio/',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'bio':newbio,'publish_to_feed':True,'submit':'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Update Bio                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def profile_guard(self,id): #--> Profile Guard
        try:
            print('\rSedang Mengaktifkan Profile Guard                    ',end='');sys.stdout.flush()
            req = self.xyz.get('https://business.facebook.com/business_locations',cookies={'cookie':self.cookie})
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            var  = {'0':{'is_shielded':True,'session_id':'9b78191c-84fd-4ab6-b0aa-19b39f04a6bc','actor_id':str(id),'client_mutation_id':'b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0'}}
            data = {'variables':json.dumps(var),'method':'post','doc_id':'1477043292367183','query_name':'IsShieldedSetMutation','strip_defaults':'true','strip_nulls':'true','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'IsShieldedSetMutation','fb_api_caller_class':'IsShieldedSetMutation'}
            head = {'Content-Type':'application/x-www-form-urlencoded','Authorization':f'OAuth {tok}'}
            req  = self.xyz.post('https://graph.facebook.com/graphql',data=data,headers=head,cookies={'cookie':self.cookie})
            print('\rBerhasil Mengaktifkan Profile Guard                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def kota(self,url,a,b,kota): #--> Edit Kota Asal & Tempat Tinggal
        try:
            print('\rSedang Edit Kota                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get(url,cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'edit':a,'type':'basic',b:kota,'save':'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Edit Kota                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def website(self): #--> Edit Website
        try:
            print('\rSedang Edit Website                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get('https://mbasic.facebook.com/editprofile.php?type=contact&edit=website',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
            dat = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'type':'contact','edit':'website','add_website':'1','new_info':self.web,'save':'Tambahkan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+req['action'],data=dat,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Edit Website                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def relationship(self): #--> Auto Show Relationship
        try:
            print('\rSedang Edit Relationship                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get(f'https://mbasic.facebook.com/editprofile.php?type=basic&edit=relationship&action={self.rl}',cookies={'cookie':self.cookie}).content,'html.parser')
            raq = [fom for fom in req.find_all('form',{'action':True}) if '/a/editprofile.php?' in fom['action']][0]
            data = {i['name']: i['value'] for i in raq.find_all('input', {'name': True, 'value': True})}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
            print('\rBerhasil Edit Relationship                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def join_grup(self): #--> Auto Join Grup
        for grup in self.listgrup:
            print('\rSedang Bergabung Ke Grup %s                    '%(grup),end='');sys.stdout.flush()
            try:
                req = bs(self.xyz.get(f'https://mbasic.facebook.com/groups/{grup}',cookies={'cookie':self.cookie}).content,'html.parser')
                raq = [fom for fom in req.find_all('form',{'action':True}) if 'a/group/join/?group_id' in fom['action']][0]
                data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),'submit':'Join Group'}
                pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
                print('\rBerhasil Bergabung Ke Grup %s                    '%(grup),end='');sys.stdout.flush()
            except Exception as e: pass
    def auto_follow(self): #--> Auto Follow
        for x in self.accfoll:
            try:
                print('\rSedang Follow Akun %s                    '%(x),end='');sys.stdout.flush()
                req = bs(self.xyz.get(f'https://mbasic.facebook.com/profile.php?id={x}',cookies={'cookie':self.cookie}).content,'html.parser')
                raq = [x for x in req.find_all('a',href=True) if '/a/subscribe.php' in x['href']][0]
                get = self.xyz.get('https://mbasic.facebook.com'+raq['href'],cookies={'cookie':self.cookie})
                print('\rBerhasil Follow Akun %s                    '%(x),end='');sys.stdout.flush()
            except Exception as e: pass
    def auto_react(self): #--> Auto React
        for post in self.postid:
            try:
                print('\rSedang React Post %s                    '%(post),end='');sys.stdout.flush()
                req = bs(self.xyz.get(f'https://mbasic.facebook.com/photo.php?fbid={post}',cookies={'cookie':self.cookie}).content,'html.parser')
                get = ['https://mbasic.facebook.com' + x['href'] for x in req.find_all('a',href=True) if '/reactions/picker/?is_permalink=1' in str(x['href'])][0]
                raq = bs(self.xyz.get(get,cookies={'cookie':self.cookie}).content,'html.parser')
                rek = ['https://mbasic.facebook.com' + x['href'] for x in raq.find_all('a',href=True) if '/ufi/reaction/?ft_ent_identifier' in str(x['href'])]
                exe = bs(self.xyz.get(rek[self.react],cookies={'cookie':self.cookie}).content,'html.parser')
                print('\rBerhasil React Post %s                    '%(post),end='');sys.stdout.flush()
            except Exception as e: pass
    def auto_comment(self): #--> Auto Comment
        try:
            for post in self.postid:
                print('\rSedang Mengomentari Post %s                   '%(post),end='');sys.stdout.flush()
                for x in range(10):
                    try:
                        req = bs(self.xyz.get(f'https://mbasic.facebook.com/mbasic/comment/advanced/?target_id={post}&pap=1&at=compose&photo_comment=1',cookies={'cookie':self.cookie}).content,'html.parser').find('form',{'method':'post'})
                        data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'comment_text':self.comment,'post':'Comment'}
                        pos = bs(self.xyz.post(req['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
                    except Exception as e: pass
        except Exception as e: pass
    def auto_post(self): #--> Auto Post
        for capt in self.create:
            try:
                print('\rSedang Membuat Post                    ',end='');sys.stdout.flush()
                req = bs(self.xyz.get('https://mbasic.facebook.com/profile.php?',cookies={'cookie':self.cookie}).content,'html.parser')
                raq = [fom for fom in req.find_all('form',{'action':True}) if '/composer/mbasic/' in fom['action']][0]
                data = {i['name']: i['value'] for i in raq.find_all('input', {'name': True, 'value': True})}
                data.update({'rst_icv':'','view_privacy':'Public','privacyx':'300645083384735','xc_message':capt})
                for x in ['view_photo','view_mle','view_overview']:
                    try: data.pop(x)
                    except Exception as e: pass
                pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=data,cookies={'cookie':self.cookie}).content,'html.parser')
                print('\rBerhasil Membuat Post                    ',end='');sys.stdout.flush()
            except Exception as e: pass
    def logout(self): #--> Logout Manual
        try:
            print('\rSedang Logout                    ',end='');sys.stdout.flush()
            req = bs(self.xyz.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':self.cookie}).content,'html.parser')
            url = ['https://mbasic.facebook.com'+x['href'] for x in req.find_all('a',href=True) if 'logout.php' in str(x['href'])][0]
            roq = self.xyz.get(url,cookies={'cookie':self.cookie})
            print('\rBerhasil Logout                    ',end='');sys.stdout.flush()
        except Exception as e: pass
    def printing(self,stat,nama,id,email,pw): #--> Print Hasil Cek
        if stat == 'OK':
            print('\r%sStatus : %sSuccess%s                                   '%(P,H,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s'%(str(email)))
            print('%s[%s•%s] %sBerhasil Menambah Aktivitas%s\n'%(H,P,H,H,P))
        else:
            print('\r%sStatus : %sCheckpoint%s                                  '%(P,M,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s'%(str(email)))
            print('%s[%s•%s] %sGagal Menambah Aktivitas%s\n'%(M,P,M,M,P))

#--> Menu Bot Halaman
class bot_page:
    def __init__(self): #--> Tampung Data
        try:
            data = eval(open('Setting_Create_FB/my_set.txt','r').read())
            self.ua       = data['ua']
            self.foto_pp  = data['pp']
            self.foto_ps  = data['ps']
            self.nama_bio = data['bio']
            self.city     = data['kota']
            self.web      = data['web']
            self.rl       = data['rl']
            self.listgrup = data['grup']
            self.accfoll  = data['akun']
            self.postid   = data['post']
            self.react    = data['react']
            self.comment  = data['com']
            self.create   = data['create']
            print('%s[%s1%s] %sBot Follow'%(M,P,M,P))
            print('%s[%s2%s] Bot React%s'%(M,P,M,P))
            print('%s[%s3%s] Bot Comment%s'%(M,P,M,P))
            print('%s[%s•%s] %sPilih Sekaligus (Ex:1,2,3)'%(M,P,M,P))
            self.pilih = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).split(',')
            print('\n%s[%s•%s] %sList Akun Dari File/Manual'%(M,P,M,P))
            pil = input(' %s└─ %s[f/m] %s: %s'%(M,P,M,P)).lower()
            print('')
            if pil in ['f','file','1','01']: self.execute_file()
            elif pil in ['m','manual','2','01']: self.execute_tunggal()
            else: exit('%sIsi Yang Benar!%s'%(M,P))
        except Exception as e:
            print('%s[%s!%s] Anda Belum Menyeting Bot!%s'%(M,P,M,P))
            print('%s[%s!%s] %sSetting Terlebih Dahulu Agar Bisa Menggunakannya'%(M,P,M,P))
            time.sleep(5)
            clear()
            menu()
    def execute_tunggal(self): #--> Execute Akun Tunggal
        wey = []
        lop = int(input('%s[%s•%s] %sBerapa ID Yg Ingin Dibot : %s'%(M,P,M,P,M)))
        print('%s[%s•%s] %sContoh Format : 100093403210005|password'%(M,P,M,P))
        for x in range(lop):
            lip = input('    %sID|Pass %s : '%(M,str(x+1)))
            cek = check_nama_account(lip.split('|')[0])
            if cek['stat'] == 'CP': pass
            else: wey.append('%s|%s|Unknown|%s'%(cek['name'],lip.split('|')[0],lip.split('|')[1]))
        print('%s'%(P))
        for y in wey:
            try:
                nama, id, email, pw = y.split('|')
                self.login(nama,id,email,pw)
            except Exception as e: pass
    def execute_file(self): #--> Execute Akun Dari Folder
        self.file = {}
        f = 'Akun_New'
        if os.path.isdir(f):
            p = 0
            l = os.listdir(f)
            for y in l:
                p += 1
                self.file.update({str(p):y})
                c = '%s• %s%s'%(M,P,y)
                print(c)
            self.sortir()
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
    def sortir(self): #--> Memilih File
        try:
            d = input('\n%s[%s•%s] %sMasukkan File : '%(M,P,M,P))
            if d in list(self.file.keys()): l = 'Akun_New/%s'%(self.file[d])
            else: l = 'Akun_New/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g:
                try:
                    nama, id, email, pw = a.split('|')
                    final = check_account(id)
                    if final == 'OK': self.login(nama,id,email,pw)
                    else: self.printing('CP',nama,id,email,pw)
                except Exception as e: pass
            print('%s[%s•%s] %sProses Selesai :)%s\n'%(H,P,H,P,P))
        except Exception as e:
            print('%sError : %s'%(P,e))
            print('%sTerjadi Kesalahan!\n%s'%(M,P))
    def login(self,nama,id,email,pw): #--> Login
        self.perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'
        self.xyz = requests.Session()
        host = 'mbasic.facebook.com'
        head_get = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':None,'Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        url_get = f'https://{host}/login/device-based/password/?uid={id}&flow=login_no_pin'
        req = bs(self.xyz.get(url_get,headers=head_get).content,'html.parser').find('form',{'method':'post'})
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
        head_post = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Content-Type':'application/x-www-form-urlencoded','Origin':f'https://{host}','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Referer':f'https://{host}/login/device-based/password/?uid={id}&flow=login_no_pin','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        url_post = 'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0'
        data = {'shbl': '0','lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(req)).group(1),'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(req)).group(1),'uid': id,'next': 'https://mbasic.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
        pos = self.xyz.post(url_post,data=data,headers=head_post,cookies={'cookie':cok},allow_redirects=True)
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
        if 'checkpoint' in str(pos.text): self.printing('CP',nama,id,email,pw)
        else:
            self.data_page = []
            self.cookie = cok
            self.id = id
            self.loop_page = 0
            for x in range(4):
                self.create_page()
            try:
                req = self.xyz.get('https://business.facebook.com/business_locations',cookies={'cookie':self.cookie})
                tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
                url = 'https://graph.facebook.com/me/accounts?fields=name,id,access_token&limit=1000&access_token=%s'%(tok)
                req1 = self.xyz.get(url,cookies={'cookie':self.cookie}).json()
                with ThreadPoolExecutor(max_workers=30) as TPE:
                    for namid in req1['data']:
                        TPE.submit(self.get_id_page,namid)
            except Exception as e: pass
            if len(self.data_page) == 0: pass
            else:
                for page in self.data_page:
                    for x in self.pilih:
                        if x   == '1': self.follow(self.cookie,page['id'])
                        elif x == '2': pass#self.react()
                        elif x == '3': pass#self.comment()
                        else: pass
            jeda(10)
            final = check_account(id)
            if final == 'OK': self.printing('OK',nama,id,email,pw)
            else: self.printing('CP',nama,id,email,pw)
        self.xyz.close()
    def get_id_page(self,namid): #--> Generate Page ID
        try:
            url2 = 'https://www.facebook.com/profile.php?id=%s'%(namid['id'])
            head1 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
            req2 = self.xyz.get(url2,headers=head1,cookies={'cookie':self.cookie},allow_redirects=True)
            id_page = re.search(r'id=(\d+)',str(req2.url)).group(1)
            self.data_page.append({'id':id_page,'name':namid['name'],'token':namid['access_token']})
        except Exception as e: pass
    def get_name(self): #--> Generate Nama Random
        gder = random.choice(['male','female'])
        try:
            data = {'country':'indonesian','gender_type':f'{gder}','number_generate':'1','submit':'Generate'}
            reqa = bs(self.xyz.post('http://ninjaname.net/indonesian_name.php',data=data).content,'html.parser')
            name = re.search('• (.*?)<br/>',str(reqa)).group(1)
        except Exception as e:
            nam1 = random.choice(['Eka','Dwi','Tri','Budi','Indah','Dewi'])
            nam2 = random.choice(['Nurhayati','Handoko','Setiyani','Susanto','Permata'])
            name = f'{nam1} {nam2}'
        return(name)
    def create_page(self): #--> Create Pages
        head1 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        req = bs(self.xyz.get('https://www.facebook.com',headers=head1,cookies={'cookie':self.cookie},allow_redirects=True).content,'html.parser')
        try:
            nama_page = self.get_name()
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData":{"token":"(.*?)"}',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            cat = random.choice(['139745066094977','2347428775505624','314853004119510','357887979616332','186230924744328'])
            var = {'input': {'name':nama_page,'categories':[cat],'bio':nama_page,'creation_source':'comet','page_referrer':'launch_point','actor_id':self.id,'client_mutation_id':'1'}}
            data = {'av':self.id,'__user':self.id,'__a':'1','__req':'1a','__hs':haste,'dpr':'1.5','__ccg':'GOOD','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'AdditionalProfilePlusCreationMutation','variables':json.dumps(var),'server_timestamps':'true','doc_id':'5296879960418435'}
            head2 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/pages/creation/?ref_type=launch_point','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'AdditionalProfilePlusCreationMutation','X-Fb-Lsd':lsd}
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=data,headers=head2,cookies={'cookie':self.cookie},allow_redirects=True).json()
            if 'Coba lagi nanti' in str(pos) or 'Please try later' in str(pos):
                print('\rSpam, Coba Lagi Nanti                          ',end=''); sys.stdout.flush()
            else:
                idp = pos['data']['additional_profile_plus_create']['page']['id']
                self.loop_page += 1
                print('\rBerhasil Membuat %s Pages                      '%(str(self.loop_page)),end=''); sys.stdout.flush()
        except Exception as e: pass
    def follow(self,cok,id_page): #--> Bot Follow Page
        cok += ' i_user=%s;'%(id_page)
        cookie = {'cookie':cok}
        for target in self.accfoll:
            url = 'https://www.facebook.com/profile.php?id=%s'%(target)
            head1 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
            req = bs(self.xyz.get(url,headers=head1,cookies=cookie).content,'html.parser')
            try:
                haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
                rev = re.search('{"rev":(.*?)}',str(req)).group(1)
                hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
                dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
                jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
                lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
                spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
                spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
                treq = re.search('"timeOfResponseStart":(.*?),',str(req)).group(1).split('.')[0]
                prod = re.search('"productAttributionId":"(.*?)",',str(req)).group(1)
                var  = {'input': {"attribution_id_v2":f"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,{treq},810115,{prod},","subscribe_location":"PROFILE","subscribee_id":target,"actor_id":id_page,"client_mutation_id":"1"},"scale":1}
                data = {'av':id_page,'__user':id_page,'__a':'1','__ar':'1','__hs':haste,'dpr':'1.5','__ccg':'GOOD','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUserFollowMutation','variables':json.dumps(var),'server_timestamps':'true','doc_id':'6261418267245544'}
                head2 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'CometUserFollowMutation','X-Fb-Lsd':lsd}
                pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=data,headers=head2,cookies=cookie,allow_redirects=True)
                if "'subscribe_status': 'IS_SUBSCRIBED'" in str(pos.text): print('\rBerhasil Follow %s                         '%(target),end=''); sys.stdout.flush()
                elif "'subscribe_status': 'CAN_SUBSCRIBE'" in str(pos.text): print('\rBerhasil Follow %s                         '%(target),end=''); sys.stdout.flush()
                elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(pos.text) or 'Akun Anda dibatasi saat ini' in str(pos.text): print('\rGagal Follow Target!',end=''); sys.stdout.flush()
                else: print('\rBerhasil Follow %s                         '%(target),end=''); sys.stdout.flush()
            except Exception as e: pass
    def printing(self,stat,nama,id,email,pw): #--> Print Hasil Create Pages
        if stat == 'OK':
            print('\r%sStatus : %sSuccess%s                                   '%(P,H,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s'%(str(email)))
            if len(self.data_page) == 0: print('%s[%s•%s] %sGagal Membuat Pages & Aktivitasnya%s\n'%(M,P,M,M,P))
            else: print('%s[%s•%s] %sBerhasil Membuat Pages Dan Aktivitasnya%s\n'%(H,P,H,H,P))
        else:
            print('\r%sStatus : %sCheckpoint%s                                  '%(P,M,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s'%(str(email)))
            print('%s[%s•%s] %sGagal Membuat Pages & Aktivitasnya%s\n'%(M,P,M,M,P))

#--> Check Account
def check_account(id):
    url = f'https://www.facebook.com/p/{id}'
    r = requests.Session()
    head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    req = bs(r.get(url,headers=head,allow_redirects=True).content,'html.parser')
    title = req.find('title').text
    if title == 'Facebook': return('CP')
    else: return('OK')
def check_nama_account(id):
    url = f'https://www.facebook.com/p/{id}'
    r = requests.Session()
    head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    req = bs(r.get(url,headers=head,allow_redirects=True).content,'html.parser')
    title = req.find('title').text.split(' | ')[0]
    if title == 'Facebook': return({'stat':'CP','name':'Unknown'})
    else: return({'stat':'OK','name':title})

#--> Notice
def belum_tersedia():
    print('%sMaaf, Fitur Ini %sBelum Tersedia%s'%(P,M,P))
    print('%sTunggu Update Selanjutnya...'%(P))
    print('%sTerima Kasih!'%(P))
    print('%s- %sDapunta%s\n'%(P,H,P))

#--> Trigger
if __name__ == '__main__':
    clear()
    menu()