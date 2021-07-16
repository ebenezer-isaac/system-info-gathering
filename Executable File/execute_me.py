import platform,socket,re,uuid,requests,hashlib,base64
from Crypto.Cipher import AES
from Crypto import Random

def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

def my_encrypt(data):
    encryption_key = base64.b64decode('c7e1wJFz+PBwQix80D1MbIwwOmOceZOzFGoidzDkF5g=')
    bs = AES.block_size
    cipher = AES.new(encryption_key, AES.MODE_CFB, "1101020304050607")
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted)

print("Hey, You have completed all parts of the puzzle!! Congrats")
print("You will get my contact number at the end of this program.")
print("You need to have an active internet connection to submit your proof of work.")

while not is_connected("172.217.166.68"):
	pass
print("Active Internet Connection found.")
print("")
print("Submit all keys along with your email as proof of work.")
"""email = input("Enter your Email ID   :")
key_1 = input("Paste your key_1 here :")
key_2 = input("Paste your key_2 here :")
key_3 = input("Paste your key_3 here :")
key_4 = input("Paste your key_4 here :")
"""
email = "ebenezerv99@gmail.com"
key_1 = "34fbaa7b7723671fb0c76eeab25a5a68fb3f4efb49fab4b483d24b916b97ce71"
key_2 = "cddpwhvh2alphskawn2k3afs42gw4ak6ajxkieikh6knf9j3uy6t53ehoqv6b7aj"
key_3 = "g9s9ty6kuizhcwbsan9gsm4h2e4347m6ezdn05j21crfejjxmhdme1cn59zrfnq8"
key_4 = "u0dhlu8gix7ax4l1uek4lj1ppzpfpu1wjxd3yk8fppbe66pck1x2uvolinvpns2e"
print("Fetching Data Now ...")
message = {}
try:
    message['platform']=platform.system()
    message['platform-release']=platform.release()
    message['architecture']=platform.machine()
    message['hostname']=socket.gethostname()
    message['ip-address']=requests.get('https://ipinfo.io/ip').text.replace("\n","")
    message['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
except Exception as e:
	message = str(message) + str(e)
data_encrypted = my_encrypt(str(message))

url = 'https://ebenezer-isaac.com/contactNumber/dates.php'
myobj = {
	'email': email,
	'key_1': key_1,
	'key_2': key_2,
	'key_3': key_3,
	'key_4': key_4,
	'combined': data_encrypted
}
x = requests.post(url, data = myobj)
print("")
print(x.text)
print("")
if x.text.find("base64") == -1:
	pass
else:
	try:
		name = message['hostname']
		remove_text = re.compile(re.escape('linux'), re.IGNORECASE)
		name = remove_text.sub('', name)
		remove_text = re.compile(re.escape('windows'), re.IGNORECASE)
		name = remove_text.sub('', name)
		remove_text = re.compile(re.escape('pc'), re.IGNORECASE)
		name = remove_text.sub('', name)
		remove_text = re.compile(re.escape('home'), re.IGNORECASE)
		name = remove_text.sub('', name)
		remove_text = re.compile(re.escape('kali'), re.IGNORECASE)
		name = remove_text.sub('', name)
		remove_text = re.compile(re.escape('manjaro'), re.IGNORECASE)
		name = remove_text.sub('', name)
		if name[len(name)-1]=='-'or name[len(name)-1]=='_':
			name = name[:-1]
		if name[0]=='-'or name[0]=='_':
			name = name[1:]
		print("Hey" ,name,",","Congrats for solving the puzzle")
	except Exception as e:
		message = str(message) + str(e)
	print("Hope to hear from you soon!!")