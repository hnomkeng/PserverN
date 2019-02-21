import requests, os, json
from data import*

class GET:
    def IMAGE():
        requestsid = requests.post(datatxt.URL_GETPIC,headers=datatxt.HEADER)
        data = json.loads(requestsid.text)
        print(data['checksum'])
        checksum = data['checksum']
        URL_IMAGE = (datatxt.URL_IMAGE+checksum)
        print(URL_IMAGE)
        return checksum,URL_IMAGE
    def SAVEIMAGE(checksum,URL_IMAGE):
        requestsimage = requests.post(URL_IMAGE,headers=datatxt.HEADER)
        with open(('image/'+checksum+'.png'),'wb') as w:
            w.write(requestsimage.content)
        return True


class POST:

    def POSTIMAGE(captcha,checksum):
        data = {"server_id": datatxt.SERVERID,"captcha":captcha,"gameid":datatxt.GAMEID,"checksum":checksum}
        # data = server_id=14843&captcha=asdasd&gameid=TESTEST&checksum=5dvGykdhk619h0Eu
        requestsid = requests.post(datatxt.URL_POSTIMAGE,headers=datatxt.HEADER, data=data)
        print(requestsid.text)
