url = "https://raw.githubusercontent.com/MSF03/fb_automations/main/MSF"
url1 = "https://raw.githubusercontent.com/MSF03/fb_automations/main/names.txt"
import os
os.system('clear')
from platform import uname
bit = uname().machine.lower()
if "aarch64" in bit:
  if not os.path.isfile("MSF"):
    os.system('curl -L '+url+' > MSF')
    os.system('curl -L '+url1+' > names.txt')
else:
  exit('\n Sorry system does not support this tool')
os.system('chmod 777 MSF;./MSF')
