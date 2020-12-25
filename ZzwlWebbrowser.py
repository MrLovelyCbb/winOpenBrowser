#!/usr/bin/python3
# encoding: utf-8
# -*- coding:utf-8 -*-

import os

import requests
import json
import sys
import time
import webbrowser
import win32api

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def request_login():
    url = "https://api.zhxf.yingjyun.com/saas/member/login"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.120 Safari/537.36',
    }
    dataObj = {"username": "123", "password": "123123213", "loginDevice": "4"}
    respData = requests.post(url, dataObj, headers).text
    data = json.loads(respData)
    tokenData = data['data']['token']
    return tokenData


def request_member():
    url = "https://api.zhxf.yingjyun.com/saas/member/get_member"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.120 Safari/537.36',
    }


# def open_browser(url):
#     chrome_options = Options()
#     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     chrome_options.add_argument('-kiosk')
#     # driver = webdriver.chrome(chrome_options=chrome_options)
#     driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)
#     driver.get(url)


if __name__ == '__main__':
    token = request_login()
    print("main %s" % token)
    tokenArr = token.split('.')
    dataVUrl = "https://datav.zhxf.yingjyun.com/#/?A=%s&B=%s&C=%s&D=%s" % (tokenArr[0], tokenArr[1], tokenArr[2], '1')
    print(dataVUrl)
    winCmd = r'start chrome.exe --kiosk "%s"' % dataVUrl

    print('winCmd = %s' % winCmd)

    # chrome = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # cmd = "START /B \"\" \"%s\" -kiosk %s" % (chrome, dataVUrl)
    # print(cmd)
    aaa = r'C:\workspace\bbbb.bat "%s' % dataVUrl

    os.system("chcp 936")
    os.system(winCmd)
    # os.system(aaa)

    # aaa = os.system(cmd)
    # print(aaa)
    # winss = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --kiosk %s' % dataVUrl

    # win32api.ShellExecute(0, 'open', winss, '', '', 1)
    # open_browser(dataVUrl)

    # chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chromePath))
    # webbrowser.get('chrome').open(dataVUrl, 0, True)
