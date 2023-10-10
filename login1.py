
# Rakit Sendiri Ya pante
import os
import sys
import time
import random
import requests
from bs4 import BeautifulSoup as bs

url = 'https://m.facebook.com'
xurl = url + '/login.php'


def banner():
    os.system('clear')
    _ = "-" * 44
    ban = f"""
{_}
  _      ____   _____ _____ _   _ 
 | |    / __ \ / ____|_   _| \ | |
 | |   | |  | | |  __  | | |  \| |
 | |   | |  | | | |_ | | | | . ` |
 | |___| |__| | |__| |_| |_| |\  |
 |______\____/ \_____|_____|_| \_|
                                  
[Note   : New Methode Login Test ]
{_}
"""
    print(ban)

#Ganti user-agent pakai JAVA ME
ua = ('Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36')#Cuma Contoh

def login():
    banner()
    user = ('idmu')#UID
    pswd = ('password')#PW
    print("[+] Please wait..")
    try:
        req = requests.Session()
        req.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en_US', 'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
            'user-agent': ua
        })

        # Membuat permintaan GET langsung ke URL tanpa menggunakan with statement
        response_body = req.get(url)

        inspect = bs(response_body.text, 'html.parser')
        lsd_key = inspect.find('input', {'name': 'lsd'})['value']
        jazoest_key = inspect.find('input', {'name': 'jazoest'})['value']
        m_ts_key = inspect.find('input', {'name': 'm_ts'})['value']
        li_key = inspect.find('input', {'name': 'li'})['value']
        try_number_key = inspect.find('input', {'name': 'try_number'})['value']
        unrecognized_tries_key = inspect.find('input', {'name': 'unrecognized_tries'})['value']
        bi_xrwh_key = inspect.find('input', {'name': 'bi_xrwh'})['value']
        data = {
            'lsd': lsd_key, 'jazoest': jazoest_key,
            'm_ts': m_ts_key, 'li': li_key,
            'try_number': try_number_key,
            'unrecognized_tries': unrecognized_tries_key,
            'bi_xrwh': bi_xrwh_key, 'email': user,
            'pass': pswd, 'login': "submit"
        }
        response_body2 = req.post(xurl, data=data, allow_redirects=True, timeout=300)
        open("resopnse.html", 'wb').write(response_body2.content)
        cookie = str(req.cookies.get_dict())
        if 'checkpoint' in cookie:
            sys.exit("Checkpoint")
        elif 'c_user' in cookie:
            kuki = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])

            print(f'\n   [\033[38;5;83mSuccessfully Log In!\033[0m] \033[0m\nCookies : {kuki}\n')
            # Get_Link
            indeks_awal = kuki.find("c_user=")
            indeks_akhir = kuki.find(";", indeks_awal)
            c_user = kuki[indeks_awal + len("c_user="):indeks_akhir].strip()
            print(f"Link : facebook.com/{c_user}\n")
            # Buat nyimpen
            with open("login.txt", "a") as file:
                file.write(f'{user}|{pswd}|{kuki}\n')

            
        else:
            sys.exit("\033[38;5;208mSalah\033[0m")
    except requests.exceptions.ConnectionError:
        sys.exit('No internet')


login()