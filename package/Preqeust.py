import json,requests, base64,time,hashlib,binascii,ctypes

class Hexmd5_error: #erro_message cov to hexmd5
    Capchaincorrect = '47b84f936cfa1a104fa5d44821639363' #The code in the image is incorrect.
    Capchabeenused  = 'b4ecb33fc4dd1515eae17c9afcf8b90d' #The image has expired or has been used.
    Sever_idfail = '4468e48cc758e31ae6d66a2da91d6ddd' # data fail userid/severid / or  something
    failbase64 = 'd41d8cd98f00b204e9800998ecf8427e'


class playserver:

        # show your title bar
    def score_(status,data):
        with open('package/score.json','r') as f:
            jx = json.load(f)
            if status == 1:
                b = jx['true'] + 1
                jx['true'] = b
            if status == 2:
                b = jx['fail'] + 1
                jx['fail'] = b
            with open('package/score.json','w') as w:
                json.dump(jx,w)
            with open('package/score.json','r') as f:
                nx = json.load(f)
                t = int(nx['true'])
                f = int(nx['fail'])
                if t != 0 or f != 0:
                    fianl = t+f
                    persen = t/fianl*100
                else:
                    persen = 0
            ctypes.windll.kernel32.SetConsoleTitleW(' ' + str(data['userid'])+' :  s'+str(data['server'])+' ,  succes_ ' + str(nx['true']) +'   fail_ ' + str(nx['fail']) +' |* rate(%.2f' %persen +'%) - PserverN' )

    def MD5_CHECK(errormad):
        md5_error = hashlib.md5(binascii.unhexlify(errormad)).hexdigest()
        if (md5_error == Hexmd5_error.Capchaincorrect):
            return 'CODE IN THE IMAGE IS INCORRECT !!'
        if (md5_error == Hexmd5_error.Capchabeenused):
            return 'IMAGE HAS EXPIRED OR HAS BEEN USED !!'
        if (md5_error == Hexmd5_error.Sever_idfail):
            return 'MUST ENTER THE SERVER_ID '
        else:
            return str(md5_error)

        # get image playserver
    def getpic(data):
        reqeustpic = requests.post(data['url_getpic'], headers=data['header'], proxies={"http": data['proxy'], "https": data['proxy']})
        pic_data = json.loads(reqeustpic.text)
        picid = pic_data['checksum']
        urlimage = (data['url_image']+picid)
        request_content = requests.post(urlimage,  headers=data['header'], proxies={"http": data['proxy'], "https": data['proxy']})
        pic_content = (request_content.content)
        try:
            pr = playserver.MD5_CHECK(pic_content)
            if str(pr) == Hexmd5_error.failbase64 :
                return False,False,False
        except:
            # cov connect to base64
            base64pic = base64.b64encode(pic_content)
            return picid,pic_content,base64pic

        #  check erro_message

        #vote playserver
    def votepic(data,vote):
        requestvote = requests.post(data['url_post'], headers=data['header'], data=vote ,proxies={"http": data['proxy'], "https": data['proxy']})
        dataplayloads = json.loads(requestvote.text)
        data_success = dataplayloads['success']
        data_delay = int(dataplayloads['wait'])
        erro_message = (dataplayloads['error_msg'].encode('utf8').hex())
        if (data_success == True):
            playserver.score_(1,data)
            return True,data_delay
        elif  (data_delay > 0 ):
            return 4,int(data_delay)
        elif (data_success != True):
            playserver.score_(2,data)
            md5_error = playserver.MD5_CHECK(str(erro_message))
            return 0,md5_error


        #reqid 2captcha and return captchakey
    def two_captcha(reqid,data):
            for timeout in range(60):
                load_captcha = requests.get('http://2captcha.com/res.php?key={0}&action=get&id={1}'.format(data, reqid))
                if load_captcha.text.find('CAPCHA_NOT_READY') > -1:
                    time.sleep(10)
                if load_captcha.text.find('ERROR') > -1:
                    return 0
                if load_captcha.text.find('OK') > -1:
                    captchakey = load_captcha.text[load_captcha.text.find('|')+1:]
                    return captchakey

            return 0
