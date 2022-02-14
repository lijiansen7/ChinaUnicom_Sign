import random
import requests

cookie_list = ['cookei1','cookie2']#这里填联通营业厅cookie,几天就可能失效了，暂时不会写服务密码登录

def sign(cookie):
    sign_url = 'http://act.10010.com/SigninApp/signin/daySign'
    ip = random.randint(15,26)
    headers = {
        'X-Forword-ip' : f'58.142.78.{ip}',
        'Host': 'act.10010.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; MI 10s Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;',
        'Referer': 'https://img.client.10010.com/SigininApp/index.html',
        'Cookie': cookie
        }
    data = {}
    sign = requests.post(url=sign_url,headers=headers,data=data).json()
    print(ip)
    return sign

for cookie in cookie_list:
    print(sign(cookie)['msg'])
