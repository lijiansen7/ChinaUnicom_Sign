import requests

def sign(cookie):
    sign_url = 'http://act.10010.com/SigninApp/signin/daySign'
    headers = {
        'Host': 'act.10010.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 10s Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;',
        'Referer': 'https://img.client.10010.com/SigininApp/index.html',
        'Cookie': cookie
        }
    data = {}
    sign = requests.post(url=sign_url,headers=headers,data=data).text
    return sign

def Task(key,qq_num,cookie):
    i=0
    while i<2:
        sign_2 = sign(cookie)
        if '0002' in sign_2:
            qmsg = f'https://qmsg.zendee.cn/send/{key}?msg=您今天已经签到啦&qq_num={qq_num}'
            requests.get(url=qmsg)
            i+=2
            print(sign_2)
        else:
            i+=1
            qmsg = f'https://qmsg.zendee.cn/send/{key}?msg=签到失败&qq_num={qq_num}'
            requests.get(url=qmsg)

for cookie in cookie_list:
    Task(key,qq_num,cookie)
