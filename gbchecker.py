import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
login_data = {
    'login_omen': '1',
    'submiter': 'ok',
    'login': '*****',
    'pass': '*****',
    'ok': 'ok'
    }

with requests.Session() as s:
    url = 'https://stat.everest.vn.ua/login.php'
    url2 = 'https://stat.everest.vn.ua/client_info.php?cmenu_selected=se#cmenu'
    r = s.post(url, data=login_data, headers=headers)
    req = s.get(url2)
    soup = BeautifulSoup(req.content, 'html.parser')
    trfind = soup.find('tr', class_='grid_footer')
    # gbs = trfind.select('td:nth-child(7)') Это на всякий случай для похожих кейсов
    gbs = trfind.find_all('td', align='right')[1]
    # print(gbs.text) Это для проверки получаемого

masg = ('Осталось\n' + gbs.text + ' Mb')
root = tk.Tk()
root.withdraw()
tk.messagebox.showinfo("gbchecker", masg)
