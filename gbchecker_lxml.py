import requests
import lxml.html
import tkinter as tk
from tkinter import messagebox

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
LOGING_DATA = {
    'login_omen': '1',
    'submiter': 'ok',
    'login': '*****',
    'pass': '*****',
    'ok': 'ok'
}
URL1 = 'https://stat.everest.vn.ua/login.php'
URL2 = 'https://stat.everest.vn.ua/client_info.php?cmenu_selected=se#cmenu'

try:
    with requests.Session() as session:
        logging = session.post(URL1, data=LOGING_DATA, headers=HEADERS)
        responce = session.get(URL2)
except Exception as e:
    print(e)
tree = lxml.html.document_fromstring(responce.text)
result = tree.xpath('//*[@id="css_grid"]/tr[4]/td[7]/text()')[0]
masg = ('Осталось\n' + result + ' Mb')
root = tk.Tk()
root.withdraw()
tk.messagebox.showinfo("gbchecker", masg)
