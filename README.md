import requests
from bs4 import BeautifulSoup
from tkinter import *

window = Tk()
window.title("다컴시스템 고객지원팀")
window.geometry("700x600")

login_url = "http://erp.danawacomputer.com/Login/LoginProcess.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"}
session = requests.session()

user = "ssk5766"
password = "dacom0422!!"

def run_login():
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
    # print(text)
    info_label.configure(text=str(text))

#제품 UI만들기 시작
#ID
user_label=Label(window, text="아이디", font=("System", 20, "bold"))
user_label.pack()
#PW
pw_label=Label(window, text="비밀번호", font=("System", 20, "bold"))
pw_label.pack()
#버튼
button=Button(window, text="로그인", font=("System", 20, "bold"), command=run_login )
button.pack()

info_label=Label(window, text="")
info_label.pack()

textbox=

window.mainloop()
