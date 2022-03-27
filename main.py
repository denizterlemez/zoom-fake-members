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