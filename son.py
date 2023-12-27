import requests
from bs4 import BeautifulSoup


login_url = "http://erp.danawacomputer.com/Login/LoginProcess.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

user = "ssk5766"
password = "dacom0422!!"

session = requests.session()

params = dict()
params['UserID'] = user
params['UserPW'] = password

res = session.post(login_url,headers=headers,  data = params)
res.raise_for_status()
print(session.cookies.get_dict())


url1 = "http://erp.danawacomputer.com/ADMIN2/AS/ASList.php"
res1 = session.get(url1 , headers=headers )
res1.raise_for_status()
res1.encoding = 'UTF-8'

soup = BeautifulSoup(res1.text, "html.parser")
text = soup.find("body").get_text()
print(text)
