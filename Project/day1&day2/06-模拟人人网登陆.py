# http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018841735878

import requests
import json
import js2py

#
session = requests.session()
headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
# 登陆之前访问 http://activity.renren.com/livecell/rKey
response = session.get("http://activity.renren.com/livecell/rKey",headers=headers)

rKeyData = json.loads(response.text)
print(rKeyData)

context = js2py.EvalJs()

phoneNum = "13641112526"
password = "chenze24"
#
context.t = {
    "password":password,
    "phoneNum":phoneNum,
    "c1":'0',
    'rKey':rKeyData["data"]["rkey"]
}

with open('Barrett.js', "rb") as f:
    barrett_js_string = f.read().decode("utf-8")
    context.execute(barrett_js_string)

with open('BigInt.js',"rb") as f:
    bigint_js_string = f.read().decode("utf-8")
    context.execute(bigint_js_string)

with open('RSA.js', "rb") as f:
    rsa_js_string = f.read().decode("utf-8")
    context.execute(rsa_js_string)

    
context.n = rKeyData['data']
js = '''
     t.password = t.password.split("").reverse().join(""),
     setMaxDigits(130);
     console.log(t)
     var o = new RSAKeyPair(n.e,"",n.n)
     var r = encryptedString(o, t.password);
     t.password = r,
     t.rKey = n.rkey
    '''
context.execute(js)

# print(context.t.password)



#登陆
login_url = "http://activity.renren.com/livecell/ajax/clog"
#
headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
#
# phoneNum = "13641112526"
#
# #原始密码 --> js加密 --->这串密码
# password = "4641bc30402fd53720dcc90b5e517be9d3e3894c1b4038099c24e84cef24597e"
#
data = {
    "phoneNum": "13641112526",
    "password": context.t.password,
    "c1": "0",
    "rKey": rKeyData["data"]['rkey']

}
#
session.post(login_url,data=data,headers=headers)
session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

response = session.get("http://www.renren.com")
with open("2-sample.html","wb") as f:
    f.write(response.content)

