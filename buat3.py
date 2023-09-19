#--> Warna
P = "\x1b[38;5;231m" #Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m" # Hijau
A = '\x1b[38;5;248m' # Abu-Abu
K = "\x1b[38;5;228m" # KUNING
B = "\x1b[38;5;86m" # BIRU
D = "\x1b[0;00m" # NETRAL

#--> Impor Modul & Jalankan
mencoba :
    impor os, sys, waktu, re, datetime, acak, urllib, json
    dari tanggal waktu impor tanggal waktu
    dari nama import random_name_US, random_name_IN, random_name_ID, random_name_RU, random_name_PK, random_name_JP, random_name_CN, random_name_ZW, random_name_ES, random_name_BR, random_name_VN, random_name_PH
kecuali Pengecualian sebagai e :
    mencetak(e)
    exit('\nTerjadi Kesalahan!')
mencoba :
    permintaan impor
kecuali Pengecualian sebagai e :
    os.system('permintaan pemasangan pip')
    permintaan impor
mencoba :
    impor bs4
    dari bs4 impor BeautifulSoup sebagai bs
kecuali Pengecualian sebagai e :
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs

#--> Global Variable
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni' ,'7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
oke = 0
cp = 0
susukeqing = acak.pilihan([1, 2, 3])
susuganyu = acak.randint(10**(susukeqing-1), 10**susukeqing-1 - 1)

#--> Hapus Terminal
pasti jelas():
    jika "linux" di sys.platform.lower():os.system('clear')
    elif "menang" di sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember" ][tanggalwaktu.sekarang().bulan - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> Penjeda Waktu
def jeda(t):
    untuk x dalam rentang(t+1):
        print('\r%sTunggu %s Detik '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        jika t == 0 : putus
        lain: waktu.tidur(1)
def tunggu_kode(t):
    untuk x dalam rentang(t+1):
        print('\r%sTunggu Kode %s Detik '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        jika t == 0 : putus
        lain: waktu.tidur(1)

#--> Agen Pengguna Vivo
def acak_ua_vivo():
    a = acak.randrange(112,115)
    b = acak.randrange(1000,10000)
    c = acak.randrange(10,100)
    os_ver = random.randrange(10,13) #--> Versi OS
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Jenis Perangkat
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A']) #--> Tipe Pembuatan
    dv_ver = random.randrange(100000,250000) #--> Versi Perangkat
    sd_ver = random.randrange(1,10) #--> Perbarui Versi
    ch_ver = f'{a}.0.{b}.{c}' #--> Versi Chrome
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/{ ch_ver} Safari Seluler/537.36'
    kembali (ua)

#--> Agen Pengguna Samsung
def acak_ua_samsung():
    a = acak.randrange(112,115)
    b = acak.randrange(1000,10000)
    c = acak.randrange(10,100)
    os_ver = random.randrange(10,13) #--> Versi OS
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B']) #--> Jenis Perangkat
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A']) #--> Tipe Pembuatan
    dv_ver = random.randrange(100000,250000) #--> Versi Perangkat
    sd_ver = random.randrange(1,10) #--> Perbarui Versi
    ch_ver = f'{a}.0.{b}.{c}' #--> Versi Chrome
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/{ ch_ver} Safari Seluler/537.36'
    kembali (ua)

#--> Agen Pengguna Realme
def acak_ua_realme():
    a = acak.randrange(112,115)
    b = acak.randrange(1000,10000)
    c = acak.randrange(10,100)
    os_ver = random.randrange(10,13) #--> Versi OS
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020']) #--> Jenis Perangkat
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A']) #--> Tipe Pembuatan
    dv_ver = random.randrange(100000,250000) #--> Versi Perangkat
    sd_ver = random.randrange(1,10) #--> Perbarui Versi
    ch_ver = f'{a}.0.{b}.{c}' #--> Versi Chrome
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/{ ch_ver} Safari Seluler/537.36'
    kembali (ua)

#--> Agen Pengguna Kustom
def acak_ua_custom():
    mencoba:
        _file_ = manusia
        jika 'Android' di str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(10,13))
            ua1 = _file_.replace(ad_ver,os_ver)
        lain: ua1 = _file_
        jika 'Bangun' di str(_file_):
            od_ver = 'Bangun/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = acak.pilihan(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A','PKQ1'])
            dv_ver = acak.randrange(100000,250000)
            sd_ver = acak.randrange(1,10)
            nw_str = 'Bangun/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.ganti(od_ver,nw_str)
        lain: ua2 = ua1
        jika 'Chrome' di str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            a = acak.randrange(112,115)
            b = acak.randrange(1000,10000)
            c = acak.randrange(10,100)
            ch_ver = f'{a}.0.{b}.{c}'
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.ganti(ch_lama,ch_baru)
        lain: ua3 = ua2
        kembali (ua3)
    kecuali Pengecualian sebagai e:
        return('Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36')

#--> Konversi Cookie
def cvt(st,lari):
    mencoba:
        jika st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s;'%(ran['sb'],ran[' datr'],lari['c_user'],lari['xs'],lari['fr']))
        elif st == 'cp': cookie = ('pos pemeriksaan=%s;datr=%s;fr=%s;'%(ran['pos pemeriksaan'],ran['datr'],ran['fr'] ))
    kecuali Pengecualian sebagai e : cookie = '; '.join([str(x)+"="+str(y) untuk x,y berturut-turut])
    kembali(str(kue))

#--> Logo
def logo():
    cetak('%s__________ __ %s________________ %s'%(P,M,P))
    mencetak('%s\_ ___ \_______ ____ _____ _/ |_ ____%s\_ ____|___ \\%s'%(P,M,P))
    mencetak('%s/ \ \/\_ __ \ __ \\\\__ \\\\ __\/ __ \%s| __) | _/%s'%(P,M,P))
    print('%s\ %s0.2 %s\____| | \/ ___/ / __ \| | \ ___/%s| \ | | \\%s'%(P,H,P,M,P ))
    print('%s \________/|__| \_____>______/__| \____>%s|___/ |_______/%s'%(P,M,P))
    print('%s\n â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â ”€ %sâ€¢ %sRan_Arraya %sâ€¢ %sâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â ”€â”€â”€\n%s'%(A,M,P,M,A,P))
    mencetak('')

#--> Menu Utama
menu kelas:
    def __init__(diri):
        jelas();logo()
        mandiri.main_menu()
    def main_menu(diri):
        print('%s<%s1%s> %sBuat Akun'%(M,P,M,P))
        print('%s<%s2%s> %sPeriksa Hasil'%(M,P,M,P))
        print('%s<%s3%s> %sInfo & Catatan Perubahan'%(M,P,M,P))
        x = input(' %sâ””â”€ %sPilih %s: %s'%(M,P,M,P)).lower()
        mencetak('')
        jika x dalam ['1','01','001','a']: menu_create()
        elif x di ['2','02','002','b']: menu_check()
        elif x di ['3','03','003','c']: changelog_content = changelog();print(changelog_content);input("\n\nMasuk untuk melanjutkan")
        else: print('%sIsi Yang Benar!%s'%(M,P));time.sleep(2);clear();menu()

#--> Menu Buat
menu kelas_buat:
    def __init__(diri):
        global gender, namstat, nameme, naran, web_email, tampil, useragent, uman, passstat, kata sandi
        coba:os.mkdir('HASIL')
        kecuali Pengecualian sebagai e :pass
        print(' %sâ—‰ %sRekomendasi %sâ—‰ %sTidak Rekomendasi â—‰ Netral'%(H,P,M,P))
        mencetak('')
        print('%s<%s/%s> %sPemilihan Jenis Kelamin'%(M,P,M,P))
        jenis kelamin = input('%sâ€¢ %sLaki-Laki/Perempuan/Acak [%sl%s/%sp%s/%sr%s] : '%(B,P,H,P,H,P,M ,P)).lebih rendah()
        print('%s<%s/%s> %sNama Bagian'%(M,P,M,P))
        namanama = input('%sâ€¢ %sGunakan Nama Acak/Manual [%sr%s/%sm%s] : '%(B,P,M,P,H,P)).lower().
        jika namanama dalam ['m','manual']:
            namstat = 'Manual'
            nama saya = input('%sâ””â”€ %sNama : %s'%(M,P,H)).split(',')
        elif namanama dalam ['r','acak']:
             namstat = 'Acak'
             print('%s<%s/%s> %sPilih nama acak dari negara yang tersedia.'%(M,P,M,P))
             naran = masukan('%sâ€¢ %s[%sUS%s/%sIN%s/%sID%s/%sPK%s/%sRU%s/%sJP%s/%sCN%s/%sZW% s/%sES%s/%sBR%s/%sVN%s/%sPH%s]: '%(H,P,M,P,M,P,K,P,H,P,P,P, H,P,K,P,P,P,H,P,K,P,H,P,H,P)).atas()
        print('%s<%s/%s> %sBagian Email'%(M,P,M,P))
        web_email = masukan('%sâ€¢ %sCryptoGmail/SecMail/MinuteMail [%sc%s/%ss%s/%sm%s] : '%(B,P,H,P,H,P,M,P )).lebih rendah()
        print('%s<%s/%s> %sBagian Hasil'%(M,P,M,P))
        tampil = input('%sâ€¢ %sTampilkan Akun CP [%sy%s/%st%s] : '%(B,P,M,P,H,P)).lower()
        print('%s<%s/%s> %sBagian Agen Pengguna'%(M,P,M,P))
        agen pengguna = input('%sâ€¢ %sVivo/Samsung/Realme/Manual [v/%ss%s/%sr%s/m] : '%(B,P,H,P,H,P)). lebih rendah()
        jika agen pengguna di ['m','manual','0','00']:
            uman = input('%sâ””â”€ %sAgen Pengguna : %s'%(M,P,M))
            jika uman == '' atau uman == ' ':
                exit('%sâ€¢ %sMasukan User-Agent yang valid.%s'%(B,M,P))
        kalau tidak:
            uman = 'Mozilla/5.0 (Linux; Android 13; RMX3686) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
        print('%s<%s/%s> %sBagian Kata Sandi'%(M,P,M,P))
        passstat = input('%sâ€¢ %sAcak/Manual [%sr%s/%sm%s] : '%(B,P,H,P,M,P)).lower().
        jika status sandi di ['m','manual','b','2','02']:
            kata sandi = masukan('%sâ””â”€ %sKata sandi : %s'%(M,P,M))
            jika len(kata sandi) <6:
                exit('%sâ€¢ %sPassword Minimal 6 Digit.%s'%(B,M,P))
            jika password di ['akusayangkamu','123456','iloveyou','password','qwerty','sayang','anjing','bangsat']:
                exit('%sâ€¢ %sGunakan Kata Sandi Yang Kuat!%s'%(B,M,P))
        kalau tidak:
            kata sandi = '@ini adalah kata sandimu'
        print('%s<%s/%s> %sBagian Penundaan Waktu'%(M,P,M,P))
        mencoba:
            d = int(input('%sâ€¢ %sBeri Delay (%s1 = 1 menit%s) : '%(B,P,H,P)))
        kecuali ValueError:
            d = 1
        mencetak('')
        aku = ke dalam(d)*60
        untuk y dalam rentang (10.000):
            buat_fb()
            mandiri.hitung(l)
    def hitung(diri sendiri,a):
        untuk x dalam rentang(a+1):
            print('\r[%sLIVE:%s%s] [%sDEAD:%s%s] Tunggu %s Detik '%(H,str(ok),P,M,str(cp),P,str( a)),end='');sys.stdout.flush()
            sebuah -= 1
            waktu.tidur(1)

#--> Buat Akun Facebook
kelas buat_fb:

    #--> Kampung Kabeh
    def __init__(diri):
        self.file = 'HASIL/%s.txt'%(waktu())
        self.abc = permintaan.Sesi() #--> Sesi Email
        self.xyz = permintaan.Sesi() #--> Sesi Facebook
        self.youridz = ["10028056", "100002457379452"]
        self.postidL = "pfbid02Z7zd35emhWmD9Sq3GcyXytaCUFKCCGNCqHqZCnzkHHPU36Zgy4V54MuDxySAzorJl"
        self.postidC = "pfbid02Z7zd35emhWmD9Sq3GcyXytaCUFKCCGNCqHqZCnzkHHPU36Zgy4V54MuDxySAzorJl"
        self.groupid = ["992573388177226", "1055033602018704", "623917041583871", "66395894663"]
        akun_yang diikuti sendiri = {}
        self.susukafka = f"https://boredhumans.com/faces2/{susukanyu}.jpg"
        self.susunahida = f"https://picsum.photos/id/{susuganyu}/600/263"
        self.textbio = f"Dibuat : {waktu()}"
        mandiri.abc.cookies.clear()
        self.xyz.cookies.clear()
        jika agen pengguna di ['v','vivo','1','01','a']: self.ua = random_ua_vivo()
        agen pengguna elif di ['s','samsung','2','02','b']: self.ua = random_ua_samsung()
        agen pengguna elif di ['r','realme','3','03','c']: self.ua = random_ua_realme()
        agen pengguna elif di ['m','manual','0','00','z']: self.ua = random_ua_custom()
        else : self.ua = 'Mozilla/5.0 (Linux; Android 13; RMX3686) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
        self.head_email = {'Terima':'teks/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/ pertukaran bertanda tangan;v=b3;q=0.7','Terima-Encoding':'gzip, deflate','Bahasa Terima':'en-US,en;q=0.9','Pragma':'akamai- x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get- ssl-klien-sesi-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x- dapatkan-klien-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform' :'','Sec-Fetch-Dest':'dokumen','Sec-Fetch-Mode':'navigasi','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G532G Build/ MMB29T; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/20.0.2254.110284'}
        self.ua_wind = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.headers_get = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8, aplikasi/pertukaran bertanda tangan: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-lingual' : 'id-ID, id;q=0.9, en-US;q= 0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Tidak : Sebuah merek"; v="99", "Chromium";V="112"','sec-ch-ua-daftar-versi lengkap' : '"Bukan:Merek-A"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"' ,'sec-ch-ua-platform-version' : '"11.0.
        mandiri.menghasilkan_data()
        mandiri.scrap1()

    #--> Hasilkan Data
    def generate_data(diri):
        diri.nama, soex = diri.get_name().split('|')
        self.nope = random.choice([self.getnumus(), self.getnumid(), self.getnumin(), self.getnumus()])
        jika web_email di ['c','cryptogmail','1','01','a']: self.email = self.get_email_cryptogmail()
        elif web_email di ['s','secmail','2','02','b']: self.email = self.get_email_onesecmail()
        elif web_email di ['m',' Minutemail','4','04','d']: self.email = self.get_email_10 Minutemail()
        lain : self.email = self.get_email_10menitmail()
        if soex == 'pria' : self.sex = '2'
        else : self.sex = '1'
        if passtat in ['m','manual','b','2','02']: self.pw = password
        else: self.pw = self.get_pass(self.name)
        self.ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1970,2001))}
        self.perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'

    #--> Generate Random Name
    def get_name(self):
        if kelamin in ['l', 'laki', '1', '01', 'a']:
            gder = 'male'
        elif kelamin in ['p', 'perempuan', '2', '02', 'b']:
            gder = 'female'
        else:
            gder = random.choice(['male', 'female'])
        try:
            jika namstat == 'Manual':
                nama = acak.pilihan(nama saya)
                kembalikan f'{nama}|{gder}'
            elif namstat == 'Acak':
                jika naran di ["US", "IN", "ID", "PK", "RU", "JP", "CN", "ZW", "ES", "BR", "VN", "PH "]:
                    nama_daftar = (
                        nama_acak_US[gder]
                        jika naran == "AS" yang lain
                        nama_acak_IN[gder]
                        jika naran == "MASUK" yang lain
                        ID_nama_acak[gder]
                        jika naran == "ID" lain
                        nama_acak_PK[gder]
                        jika naran == "PK" lain
                        nama_acak_RU[gder]
                        jika naran == "RU" lain
                        nama_acak_JP[gder]
                        jika naran == "JP" lain
                        nama_acak_CN[gder]
                        jika naran == "CN" lain
                        nama_acak_ZW[gder]
                        jika naran == "ZW" lain
                        nama_acak_ES[gder]
                        jika naran == "ES" lain
                        nama_acak_BR[gder]
                        jika naran == "BR" lain
                        nama_acak_VN[gder]
                        jika naran == "VN" lain
                        nama_acak_PH[gder]
                        jika naran == "PH" lain
                        Tidak ada
                    )
                    nama1 = acak.pilihan(daftar_nama)[0]
                    nama2 = acak.pilihan(daftar_nama)[1]
                    nama3 = acak.pilihan(daftar_nama)[2]
                    nama = f"{nama1} {nama2} {nama3}"
                    kembalikan f'{nama}|{gder}'
                kalau tidak:
                    print("%sAnda belum memasukkan kode negara yang valid dari opsi yang tersedia.\nSilakan lihat log perubahan untuk informasi lebih lanjut.\n%s"%(M,P))
                    x = input('Tekan enter untuk kembali ke menu utama.');menu()
            kalau tidak:
                print('%sPilih yang benar%s'%(M,P))
        kecuali Pengecualian sebagai e:
            nam1 = acak.pilihan(['Eka','Dwi','Tri','Budi','Indah','Dewi'])
            nam2 = random.choice(['Nurhayati','Handoko','Setiyani','Susanto','Permata'])
            nam3 = random.choice(['Triatmaja','Siagian','Manopo','Jayaningrat','Widodo'])
            nama = f'{nam1} {nam2} {nam3}'
        klop = f'{nama}|{gder}'
        kembalikan Klop

    #--> Hasilkan Nomor Telepon Acak
    def getnumin(diri): #India
        na = acak.pilihan(['74', '90', '91', '75', '97', '98', '99'])
        ni = str(random.randrange(10000000, 100000000))
        tidak = '+91%s%s'%(tidak, tidak)
        kembali (tidak)
    def getnumbd(diri): #Bangladesh
        na = acak.pilihan(['13', '14', '15'])
        ni = str(random.randrange(10000000, 100000000))
        tidak = '+880%s%s'%(tidak, tidak)
        kembali (tidak)
    def getnumid(diri): #Indonesia
        na = acak.pilihan(['96','78','21'])
        ni = str(acak.randrange(1000,10000))
        nu = str(random.randrange(1000,10000))
        tidak = '+628%s%s%s'%(na, ni, nu)
        kembali (tidak)
    def getnumus(diri): #USA
        na = acak.pilihan(["225", "209", "201", "812", "204", "709", "647", "306", "613", "250", "902" ])
        ni = str(random.randrange(1000000, 10000000))
        tidak = '+1%s%s'%(na, ni)
        kembali (tidak)

    #--> Hasilkan Kata Sandi Acak
    def get_pass(diri, nama):
        angka = acak.randrange(100000, 1000000)
        pw = f"@{nama}{angka}".replace(" ", "")
        kembali(pw.bawah())

    #--> Hasilkan Email & Kode Dari Cryptogmail
    def get_email_cryptogmail(diri):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        berlari = str(random.randrange(1000,10000))
        dom = acak.pilihan(['fexbox.org','chitthi.in','fextemp.com','any.pink','merepost.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        kembali (email)
    def get_code_cryptogmail(diri):
        url = f'https://tempmail.plus/api/mails?email={self.email}'
        req = self.abc.get(url,headers=self.head_email).json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        kembali (kode)

    #--> Hasilkan Email & Kode Dari 1SecMail
    def get_email_onesecmail(diri):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        berlari = str(random.randrange(1000,10000))
        dom = acak.pilihan(['1secmail.com','1secmail.org','1secmail.net','kzccv.com','qiott.com','wuuvo.com','icznn.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        kembali (email)
    def get_code_onesecmail(diri):
        nama, domain = self.email.split('@')
        req = self.abc.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}').json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        kembali (kode)

    #--> Hasilkan Email & Kode Dari 10Minutemail
    def get_email_10menitmail(mandiri):
        req = bs(self.abc.get('https://10 Minutemail.net/m/?lang=id',headers=self.head_email,allow_redirects=True).content,'html.parser')
        self.xyz_email = re.search('sessionid="(.*?)"',str(req)).group(1)
        self.tim_email = str(time.time()).replace('.','')[:13]
        dat = {'baru':'1','sessionid':self.xyz_email,'_':self.tim_email}
        pos = self.abc.post('https://10 Minutemail.net/address.api.php',data=dat,headers=self.head_email,allow_redirects=True).json()
        email = pos['mail_get_mail']
        mandiri.cookie_email = '; '.join([str(x)+"="+str(y) untuk x,y di self.abc.cookies.get_dict().items()])
        kembali (email)
    def get_code_10menitmail(mandiri):
        dat = {'baru':'0','sessionid':self.xyz_email,'_':self.tim_email}
        pos = self.abc.post('https://10 Minutemail.net/address.api.php',data=dat,headers=self.head_email,cookies={'cookie':self.cookie_email},allow_redirects=True) .json()
        kode = re.search(r'FB-([^ ]+)',str(pos)).group(1)
        kembali (kode)

    def scrap1(self): #--> Posting Login Awal
        req = bs(self.xyz.get('https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk',headers=self.headers_get).content,'html.parser')
        fom = req.find('form',{'method':'post'})
        data = {
            'lsd' : re.search('name="lsd" type="hidden" value="(.*?)"', str(fom)).group(1),
            'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"', str(fom)).group(1),
            'fb_dtsg' : re.search('{"dtsg":{"token":"(.*?)",', str(req)).group(1),
            'ccp' : re.search('name="ccp" type="hidden" value="(.*?)"', str(fom)).group(1),
            'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"', str(fom)).group(1),
            'reg_impression_id' : re.search('name="reg_impression_id" type="hidden" value="(.*?)"', str(fom)).grup(1),
            'ns' : re.search('name="ns" type="hidden" value="(.*?)"', str(fom)).group(1),
            'app_id' : re.search('name="app_id" type="hidden" value="(.*?)"', str(fom)).group(1),
            'logger_id' : re.search('name="logger_id" type="hidden" value="(.*?)"', str(fom)).group(1),
            'suma_create_event' : 'suma_redirection_click_create_account',
            'nama_bidang[0]' : 'nama depan',
            'nama_bidang[1]' : 'pembungkus_ulang tahun',
            'nama_bidang[2]' : 'reg_email__',
            'nama_bidang[3]' : 'jenis kelamin',
            'nama_bidang[4]' : 'reg_passwd__',
            'is_birthday_confirmed' : 'dikonfirmasi',
            'bentuk_langkah_banyak' : '1',
            'lewati_suma' : '0',
            'harusForceMTouch' : '1',
            'ref' : 'dbl',
            'nama depan' : nama diri,
            'reg_email__' : mandiri.tidak,
            'seks' : diri.seks,
            'reg_passwd__' : mandiri.pw,
            'hari_ulang tahun' : self.ttl['tgl'],
            'bulan_ulang tahun' : self.ttl['bln'],
            'tahun_ulang tahun' : self.ttl['thn'],
            'welcome_step_completed' : Benar,
            'submission_request' : Benar,
            'age_step_input' : Salah,
            'did_use_age' : Salah,
            'custom_gender' : Salah,
            'name_suggest_elig' : Salah,
            'was_shown_name_suggestions' : Salah,
            'did_use_suggested_name' : Salah,
            'use_custom_gender' : Salah,
            'zero_header_af_client' : '',
            'pembantu' : '',
            'panduan' : '',
            'langkah_pra_bentuk' : '',
            'korean_tos_is_present' : '',
            'kotak centang_kebijakan_privasi' : '',
            'kotak centang_tos' : '',
            'kebijakan_lokasi_kotak centang' : ''
        }
        kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
        cok += diri.perangkat
        selanjutnya = 'https://m.facebook.com' + fom['aksi']
        pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        if pos.find('title').text == 'Konfirmasikan Akun Anda': #--> Jika Akun Sudah Dibuat
            self.scrap4()
        else:
            rog = pos.find('form',{'method':'post'})
            if rog is not None:
                if 'login/device-based/update-nonce' in str(rog.get('action', '')):
                    self.scrap2(rog)
                elif 'conf/notifmedium/send_code' in str(rog.get('action', '')):
                    self.scrap3(rog)
                elif 'checkpoint' in str(rog.get('action', '')):
                    self.printing('CP')
            else:
                print(f'\râ€¢ {M}Tidak merespons{D} ',end='');sys.stdout.flush()
    def scrap2(self,fom): #--> Simpan Perangkat OK
        print('\rLolos Tahap 1',end='');sys.stdout.flush()
        data = {
            'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).grup(1),
            'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
            'aliran' : 'interstisial_nux',
            'Berikutnya' : '',
            'nux_source' : 'dbl_nux_after_reg',
            'kirim' : 'Oke'}
        kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
        cok += diri.perangkat
        selanjutnya = 'https://m.facebook.com' + fom['aksi']
        pos = bs(self.xyz.post(selanjutnya,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        rog = pos.find('form',{'method':'post'})
        diri.scrap3(rog)
    def scrap3(self,fom): #--> Minta Kode Tidak
        print('\rLolos Tahap 2',end='');sys.stdout.flush()
        mencoba:
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).grup(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'sedang' : 'sms',
                'kirim' : 'Kirim kode'}
            kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
            cok += diri.perangkat
            selanjutnya = 'https://m.facebook.com' + fom['aksi']
            pos = bs(self.xyz.post(selanjutnya,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            mandiri.scrap4()
        kecuali Pengecualian sebagai e:
            mandiri.mencetak('CP')
    def scrap4(mandiri): #--> Tambahkan Email
        print('\rLolos Tahap 3',end='');sys.stdout.flush()
        kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
        cok += diri.perangkat
        mencoba:
            req = bs(self.xyz.get('https://m.facebook.com/changeemail/',headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).grup(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'email_lama' : re.search('name="old_email" type="hidden" value="(.*?)"',str(fom)).grup(1),
                'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"',str(fom)).group(1),
                'baru' : email mandiri,
                'Berikutnya' : '',
                'kirim' : 'Tambahkan'}
            kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
            cok += diri.perangkat
            selanjutnya = 'https://m.facebook.com' + fom['aksi']
            pos = bs(self.xyz.post(selanjutnya,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            tunggu_kode(30)
            mandiri.scrap5(pos)
        kecuali Pengecualian sebagai e:
            mandiri.mencetak('CP')
    def scrap5(self,req): #--> Konfirmasi Kode
        print('\rLolos Tahap 4',end='');sys.stdout.flush()
        kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
        cok += diri.perangkat
        mencoba:
            jika web_email di ['c','cryptogmail','1','01','a']: kode = self.get_code_cryptogmail()
            elif web_email di ['s','secmail','2','02','b']: kode = self.get_code_onesecmail()
            elif web_email di ['m','menitmail','4','04','d']: kode = self.get_code_10menitmail()
            lain : kode = self.get_code_10menitmail()
            id = re.search('c_user=(.*?);',cok).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            dtsg = re.search('"dtsg":{"token":"(.*?)",',str(req)).group(1)
            jazoest = re.search('"jazoest", "(.*?)",',str(req)).group(1)
            data = {
                'kontak': self.email,
                'ketik': 'kirim',
                'is_soft_cliff': Salah,
                'sedang': 'email',
                'kode': kode,
                'fb_dtsg': dtsg,
                'jazoest': jazoest,
                'lsd': lsd,
                '__identitas pengguna}
            pos = bs(self.xyz.post('https://m.facebook.com/confirmation_cliff/',data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True). konten,'html.parser')
            mandiri.semi_final()
        kecuali Pengecualian sebagai e:
            mandiri.mencetak('CP')
    def zero_optin(self): #--> Mode Data Khusus (Tanpa Wifi)
        mencoba:
            kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()]) + self.perangkat
            req1 = bs(self.xyz.get('https://mbasic.facebook.com',headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser' )
            nek = ['https://mbasic.facebook.com'+x['href'] untuk x di req1.find_all('a',href=True) if 'dialtone_optin_page' di str(x['href']) ] [0]
            kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()]) + self.perangkat
            req2 = bs(self.xyz.get(nek,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            fom = req2.find('form',{'method':'post'})
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).grup(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'kirim' : 'Oke, Gunakan Data'}
            nuk = 'https://mbasic.facebook.com' + fom['aksi']
            kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()]) + self.perangkat
            pos7 = self.xyz.post(nuk,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True)
            print('\rBerhasil Lewati Mode Bebas',end='');sys.stdout.flush()
        kecuali Pengecualian sebagai e: pass
    def semi_final(mandiri): #--> Sortir
        print('\rLolos Tahap 5',end='');sys.stdout.flush()
        kok = '; '.join([str(x)+"="+str(y) untuk x,y di self.xyz.cookies.get_dict().items()])
        cok += diri.perangkat
        mencoba:
            id = re.search('c_user=(.*?);',cok).group(1)
            mandiri.zero_optin()
            jeda(10)
            final = cek_rekening(id)
            if final == 'OK': self.printing('OK')
            yang lain: self.printing('CP')
        kecuali Pengecualian sebagai e:
            mandiri.mencetak('CP')
    def pencetakan(mandiri,stat): #--> Cetak Hasil
        global oke, cp
        jika status == 'OK':
            cookie = cvt('ok',self.xyz.cookies.get_dict())
            buka("cookies.json","a").tulis(cookie+"\n")
            id = self.xyz.cookies.get_dict()['c_user']
            mencetak('\r%s<%s/%s> %sLIVE%s '%(M,P,M,H,P))
            print('â€¢ Nama : %s'%(str(nama sendiri)))
            print('â€¢ UID : %s'%(str(id)))
            print('â€¢ Lulus : %s'%(str(self.pw)))
            print('â€¢ Email : %s'%(str(self.email)))
            print('â€¢ Telepon : %s'%(str(self.nope)))
            print('â€¢ TTL : %s %s %s'%(self.ttl['tgl'],bulan[self.ttl['bln']],self.ttl['thn']))
            print('â€¢ Kue : %s%s%s'%(B,kue,D))
            print('%s<%s/%s> %sMenambahkan pengaturan lain'%(M,P,M,P))
            mandiri.ikuti()
            mandiri.bio()
            mandiri.kota_saat ini()
            mandiri.kampung halaman()
            diri.nama panggilan(nama diri)
            diri.komentar()
            diri.reaksi()
            mandiri.grup()
            mandiri.tambahkan_status()
            self.setprofile(cookie)
            self.setcover(cookie)
            mencetak('%s<%s/%s> %sSelesai!\n'%(M,P,M,P))
            open(self.file,'a+').write('%s|%s|%s|%s\n'%(self.name,id,self.email,self.pw))
            oke += 1
        kalau tidak:
            jika tampil di ['t','2','02','b']: lulus
            kalau tidak:
                mencetak('\r%s<%s/%s> %sMATI%s '%(M,P,M,M,P))
                print('â€¢ Nama : %s'%(str(nama sendiri)))
                print('â€¢ Telepon : %s'%(str(self.nope)))
                print('â€¢ Lulus : %s\n'%(str(self.pw)))
            cp += 1

    def ikuti(diri):
        untuk target di self.youridz:
            self.res = self.xyz.get(f"https://mbasic.facebook.com/{target}/?v=info&refid=17&paipv=0")
            self.par = bs(self.res.teks, "html.parser")
            if (pler := self.par.find("a", href=lambda i: "/a/subscribe.php" di i)):
                self.xyz.get("https://mbasic.facebook.com" + pler["href"])
                nama = self.par.find("judul").teks
                self.followed_accounts[target] = nama
        jika akun_diikuti sendiri:
            untuk target, beri nama di self.followed_accounts.items():
                print(f"â€¢ Mengikuti {H}{nama}{D}")
        kalau tidak:
            print(f'â€¢ {M}Kesalahan Mengikuti!{D}')

    def bio(diri):
        self.res = self.xyz.get("https://mbasic.facebook.com/profile/basic/intro/bio/?refid=17&paipv=0")
        self.par = bs(self.res.teks, "html.parser")
        self.form = self.par.find("form", metode="post")
        self.data = {i["name"]: i["value"] untuk i di self.form.find_all("input", {"name": True, "value": True})}
        self.data.update({"bio": {self.textbio}, "publish_to_feed": "on"})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
        print(f"â€¢ {D}Added Bio" if True else f"â€¢ {M}Failed Added Bio!{D}")

    def current_city(self):
        kota = random.choice(["Jakarta", "Bandung", "Depok", "Bekasi"])
        self.res = self.xyz.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city&paipv=0&refid=17")
        self.par = bs(self.res.teks, "html.parser")
        self.form = self.par.find("form", metode="post")
        self.data = {i["name"]: i["value"] untuk i di self.form.find_all("input", {"name": True, "value": True}) jika "privacy_setting" tidak di saya["nama"]}
        self.data.update({"kota_saat ini[]": kota})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "detik -fetch-user": "?1", "sec-fetch-site": "asal yang sama", "tipe konten": "application/x-www-form-urlencoded", "origin": "https: //mbasic.facebook.com", "kontrol cache": "max-age=0", "referer": self.res.url})
        print(f"â€¢ Menambahkan {H}{kota}{D} sebagai default Kota Saat Ini" jika "edit_success" di self.res.url else f"â€¢ {M}Gagal menambahkan kota saat ini {D}")

    def kampung halaman(diri):
        kota = random.choice(["Jakarta", "Bandung", "Depok", "Bekasi"])
        self.res = self.xyz.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown&paipv=0&refid=17")
        self.par = bs(self.res.teks, "html.parser")
        self.form = self.par.find("form", metode="post")
        self.data = {i["name"]: i["value"] untuk i di self.form.find_all("input", {"name": True, "value": True}) jika "privacy_setting" tidak di saya["nama"]}
        self.data.update({"kampung halaman[]": kota})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "detik -fetch-user": "?1", "sec-fetch-site": "asal yang sama", "tipe konten": "application/x-www-form-urlencoded", "origin": "https: //mbasic.facebook.com", "kontrol cache": "max-age=0", "referer": self.res.url})
        print(f"â€¢ Menambahkan {H}{kota}{D} sebagai Kampung Halaman default" jika "edit_success" di self.res.url else f"â€¢ {M}Gagal menambahkan kampung halaman {D}")

    nama panggilan def (diri sendiri, nama panggilan):
        self.res = self.xyz.get("https://mbasic.facebook.com/profile/edit/info/nicknames/?info_surface=info&refid=17&paipv=0")
        self.par = bs(self.res.teks, "html.parser")
        self.form = self.par.find("form", metode="post")
        self.data = {i["name"]: i["value"] untuk i di self.form.find_all("input", {"name": True, "value": True})}
        self.data.update({"dropdown": "nama panggilan", "teks": {nama panggilan}, "kotak centang": "on"})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "detik -fetch-user": "?1", "sec-fetch-site": "asal yang sama", "tipe konten": "application/x-www-form-urlencoded", "origin": "https: //mbasic.facebook.com", "kontrol cache": "max-age=0", "referer": self.res.url})
        print(f"â€¢ Menambahkan nama panggilan {H}{nick}{D} sebagai default" jika "nocollections" di self.res.url else f"â€¢ {M}Gagal memperbarui nama panggilan!{D}")

    def add_status(diri):
        connection_status = random.choice(['Lajang', 'Bertunangan', 'Menikah', 'Berhubungan sipil', 'Tinggal bersama', 'Menjalin hubungan tanpa status', 'Rumit', 'Berpisah', 'Bercerai', 'Menjanda /Menduda'])
        self.res = self.xyz.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=relationship&paipv=0&refid=17")
        self.par = bs(self.res.teks, "html.parser")
        self.status = self.par.find("a", href=Benar, string=relationship_status)
        self.res = self.xyz.get("https://mbasic.facebook.com" + self.status["href"])
        self.par = bs(self.res.teks, "html.parser")
        self.form = self.par.find("form", metode="post")
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] untuk saya di self.form.find_all("input", {"name": Benar, "nilai": Benar})}, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache -control": "max-age=0", "referer": self.res.url})
        print(f"â€¢ Menambahkan status hubungan ke {H}{relationship_status}{D} sebagai default" if "edit_success" di self.res.url else f"â€¢ {M}Gagal menambahkan status hubungan{D} ")

    def komentar(diri):
        HARI sekarang = tanggal waktu.sekarang().hari
        MONnow = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember" ][tanggalwaktu.sekarang().bulan - 1]
        YEAnow = tanggalwaktu.sekarang().tahun
        HOUnow = tanggalwaktu.sekarang().jam
        MINnow = tanggalwaktu.sekarang().menit
        SECnow = tanggalwaktu.sekarang().detik
        timenow = f"{DAYnow} {MONnow} {YEAnow} - {HOUnow:02}:{MINnow:02}:{SECnow:02}"
        comment_textz = [f"{timenow}", "[none]"] # Ganti dengan teks yang diinginkan
        self.res = self.xyz.get(f"https://mbasic.facebook.com/{self.postidC}")
        hitungan = len(komentar_teksz)
        untuk w dalam rentang (hitungan):
            self.par = bs(self.res.teks, "html.parser")
            self.form = self.par.find("form", action=lambda i: "/a/comment.php?" di i)
            comment_text = comment_textz[w] # Menggunakan teks komentar dari list
            self.data = {"fb_dtsg": self.form.find("input", {"name": "fb_dtsg"})["value"], "jazoest": self.form.find("input", { "nama": "jazoest"})["nilai"], "teks_komentar": komentar_teks}
            self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "detik -fetch-user": "?1", "sec-fetch-site": "asal yang sama", "tipe konten": "application/x-www-form-urlencoded", "origin": "https: //mbasic.facebook.com", "kontrol cache": "max-age=0", "referer": self.res.url})
            print(f"â€¢ Komentar otomatis {H}{comment_text}{D} berhasil")

    reaksi def (diri):
        self.res = self.xyz.get(f"https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={self.postidL}")
        self.par = bs(self.res.teks, "html.parser")
        jika tidak self.par.find("span", string="(Hapus)"):
            if (pler := self.par.find("a", href=lambda i: "reaction_type=" + self.acak di i)):
                self.xyz.get("https://mbasic.facebook.com" + pler["href"])
                print(f"â€¢ Suka otomatis berhasil")

    grup def (diri sendiri):
        untuk group_id di self.groupid:
            self.res = self.xyz.get(f"https://mbasic.facebook.com/groups/{group_id}/")
            self.par = bs(self.res.teks, "html.parser")
            self.form = self.par.find("form", action=lambda i: "/a/group/join/" di i)
            self.data = {i["name"]: i["value"] untuk i di self.form.find_all("input", {"name": True, "value": True})}
            self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "detik -fetch-user": "?1", "sec-fetch-site": "asal yang sama", "asal": "https://mbasic.facebook.com", "cache-control": "max- age=0", "referer": self.res.url})
            self.group_name = self.par.find("judul").teks
            jika 'Anggota' di self.res.text:
                print(f"â€¢ Otomatis bergabung ke {H}{self.group_name}{D} group")
            kalau tidak:
                print(f"â€¢ {M}Gagal Gabung Grup {D}{self.group_name}")

    @Properti
    def acak(diri):
        mandiri.type = [2, 16, 4]
        return str(random.choice(random.sample(self.type, len(self.type))))

    def setprofile(mandiri, cokz):
        self.cookie = {'cookie': cokz}
        mencoba:
            fot = urllib.request.urlopen(self.susukafka)
            url = 'https://mbasic.facebook.com/profile_picture/'
            req = bs(self.xyz.get(url, cookies=self.cookie).content, 'html.parser')
            raq = req.find('form', {'method': 'post'})
            tanggal = {
                'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(raq)).group(1),
                'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
                'kirim': 'Simpan'}
            fil = {'gambar': foto}
            pos = bs(self.xyz.post(raq['action'], data=dat, files=fil, cookies=self.cookie).content, 'html.parser')
            cek = pos.find('judul').teks
            if cek == 'Akun Anda dibatasi saat ini' atau cek == 'Anda Diblokir Sementara' atau cek == 'Kesalahan':
                print(f'{D}â€¢ {M}Gagal mengubah foto profil.{D}')
            kalau tidak:
                print(f'{D}â€¢ Foto profil telah diubah')
        kecuali Pengecualian sebagai e:
            print(f'{D}â€¢ {M}Gagal mengubah foto profil.{D}')

    def setcover(diri, cokz):
        self.cookie = {'cookie': cokz}
        mencoba:
            fot = urllib.request.urlopen(self.susunahida)
            url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            req = bs(self.xyz.get(url, cookies=self.cookie).content, 'html.parser')
            raq = req.find('form', {'method': 'post'})
            tanggal = {
                'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(raq)).group(1),
                'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
                'return_uri': re.search('name="return_uri" type="hidden" value="(.*?)"', str(raq)).group(1),
                'return_uri_error': re.search('name="return_uri_error" type="hidden" value="(.*?)"', str(raq)).grup(1),
                'ref': re.search('name="ref" type="hidden" value="(.*?)"', str(raq)).group(1),
                'csid': re.search('name="csid" type="hidden" value="(.*?)"', str(raq)).group(1),
                'ctype': re.search('name="ctype" type="hidden" value="(.*?)"', str(raq)).group(1),
                'profile_edit_logging_ref': re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"', str(raq)).grup(1),
                'kirim': 'Unggah',
            }
            fil = {'file1': foto}
            pos = bs(self.xyz.post('https://mbasic.facebook.com' + raq['action'], data=dat, files=fil, cookies=self.cookie).content, 'html.parser ')
            cek = pos.find('judul').teks
            if cek == 'Akun Anda dibatasi saat ini' atau cek == 'Anda Diblokir Sementara' atau cek == 'Kesalahan':
                print(f'{D}â€¢ {M}Gagal mengganti foto sampul{D}')
            kalau tidak:
                print(f'{D}â€¢ Foto sampul telah diubah')
        kecuali Pengecualian sebagai e:
            print(f'{D}â€¢ {M}Gagal mengubah foto sampul.{D}')

#--> Menu Pemeriksa Akun
menu kelas_periksa:
    def __init__(self): #--> Mengecek Ketersediaan Folder
        self.xyz = permintaan.Sesi()
        mandiri.file = {}
        diri.isi = 0
        mandiri.ok = 0
        diri.cp = 0
        f = 'RESULTS'
        if os.path.isdir(f):
            p = 0
            l = os.listdir(f)
            for y in l:
                p += 1
                self.file.update({str(p):y})
                c = '%sâ€¢ %s%s'%(M,P,y)
                print(c)
            self.sortir()
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
    def sortir(self): #--> Memilih File
        try:
            d = input('\n%s<%s/%s> %sMasukkan File : '%(M,P,M,P))
            if d in list(self.file.keys()): l = 'RESULTS/%s'%(self.file[d])
            else: l = 'RESULTS/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g:
                try:
                    nama, id, email, pw = a.split('|')
                    status = cek_akun(id)
                    if stat == 'OK': self.printing('OK',nama,id,email,pw)
                    yang lain: self.printing('CP',nama,id,email,pw)
                kecuali Pengecualian sebagai e: pass
            if self.isi == 0: print('%sTidak Ada Hasil :(\n%s'%(M,P))
            else: print('%sDari %s%s%s Akun, Terdapat %s%s Akun DEAD %sdan %s%s Akun LIVE\n%s'%(P,B,str(self.isi),D, M,str(self.cp),P,H,str(self.ok),P));i=input(f'{H}ENTER{D} untuk kembali ke menu utama. ');menu()
        kecuali Pengecualian sebagai e:
            mencetak('%sKesalahan : %s'%(P,e))
            print('%sTerjadi Kesalahan!\n%s'%(M,P))
    def printing(self,stat,nama,id,email,pw): #--> Cetak Hasil Cek
        jika status == 'OK':
            mencetak('\r%s<%s/%s> %sLIVE%s '%(M,P,M,H,P))
            print('â€¢ Nama : %s'%(str(nama)))
            print('â€¢ UID : %s'%(str(id)))
            print('â€¢ Lulus : %s'%(str(pw)))
            print('â€¢ Email : %s\n'%(str(email)))
            mandiri.ok += 1
        kalau tidak:
            mencetak('\r%s<%s/%s> %sMATI%s '%(M,P,M,M,P))
            print('â€¢ Nama : %s'%(str(nama)))
            print('â€¢ UID : %s'%(str(id)))
            print('â€¢ Lulus : %s'%(str(pw)))
            print('â€¢ Email : %s\n'%(str(email)))
            mandiri.cp += 1
        diri.isi += 1

#--> Periksa Rekening
def check_akun(id):
    url = f'https://free.facebook.com/p/{id}'
    r = permintaan.Sesi()
    head = {'terima' : 'teks/html,aplikasi/xhtm 1+xml,aplikasi/xml;q=0.9, gambar e/avif,gambar/webp, gambar/apng,*/ *;q=0.8,aplikasi/ pertukaran bertanda tangan: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-lingual' : 'id-ID, id;q=0.9, en-US;q=0.8, id;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Tidak: A -Merek"; v="99", "Chromium";V="112"','sec-ch-ua-daftar-versi lengkap' : '"Bukan:Merek-A"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"' ,'sec-ch-ua-platform-version' : '"11.0.0"',
    req = bs(r.get(url,headers=head,allow_redirects=True).content,'html.parser')
    judul = req.find('judul').teks
    if title == 'Konten Tidak Ditemukan': return('CP')
    lain: kembali ('OK')

def log perubahan():
    file_path = "..changelog"
    mencoba:
        dengan open(file_path, "r") sebagai file:
            konten = file.baca()
            mengembalikan konten
    kecuali FileNotFoundError:
        kembalikan "File tidak ditemukan."
    kecuali Pengecualian sebagai e:
        return "Terjadi kesalahan: " + str(e)

def verifikasi():
    mencoba:
        xyz = buka("..memuat",'r').baca()
        menu()
    kecuali FileNotFoundError:
        jernih()
        teks = f"""
 Kode ini tidak resmi, bercabang dari {H}[https://github.com/Dapunta/AutoCreateFB]{D}.
{B}Tuan. Dapunta{D} memiliki akses penuh ke kode ini, kami baru saja menambahkan beberapa elemen yang diperlukan untuk membuat kode lebih disesuaikan dengan kebutuhan bot Anda.

Salam kepada {B}Tuan Dapunta, {D}dan {B}Anda{M}â™¥ï¸ {D}.

*Apa yang baru? Periksa di log perubahan."""
        mencetak (teks)
        waktu.tidur(3)
        open('..load','w').write("lanjut mang")
        x = masukan('\n\n\nMasuk untuk melanjutkan')
        menu()

#--> Pemicu
jika __nama__ == '__utama__':
    verifikasi()
    menu()