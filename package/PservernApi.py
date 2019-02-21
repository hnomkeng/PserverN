import os ,configparser,requests,re
import urllib.parse

class package_api:
    def load():
        loadconfig = configparser.RawConfigParser()
        loadconfig.readfp(open(r'control/config.txt'))
        # > load control/config.txt
        key = loadconfig.get('default', 'key')
        userid = loadconfig.get('default', 'userid')
        server_id = loadconfig.get('default', 'server_id')
        proxy = loadconfig.get('default', 'proxy')
        proxy_Source = loadconfig.get('proxymode', 'Source')
        proxy_destination = loadconfig.get('proxymode', 'destination')
        proxy_blacklist = loadconfig.get('proxymode', 'blacklist')
        genproxy = loadconfig.get('proxymode', 'genproxy')
        maxproxy = loadconfig.get('proxymode', 'maxproxy')
        proxyfix = int(loadconfig.get('protect', 'proxyfix'))
        logfail = int(loadconfig.get('protect', 'log_FAIL'))
        proxyfix = int(loadconfig.get('protect', 'proxyfix'))
        manyfail = int(loadconfig.get('protect','mf'))

        # set url api playserver
        url_server = ('https://playserver.in.th/index.php/Server/')
        url_vote = ("https://playserver.in.th/index.php/Vote/prokud/")
        url_image = ("http://playserver.co/index.php/VoteGetImage/")
        # set url server from id -------------------------------------------------------------
        rquest_unpack = requests.get(url_server+str(server_id))                             #|
        unpack_text = re.search(url_vote+'(.+?)"',rquest_unpack.text)                       #|
        unpack_unicode = (unpack_text.group(1))                                             #|
        unpack_Entities = urllib.parse.quote(unpack_unicode)                                #|
        #-------------------------------------------------------------------------------------
        url_getpic = ("http://playserver.co/index.php/Vote/ajax_getpic/"+unpack_Entities)
        url_submitpic = ("http://playserver.co/index.php/Vote/ajax_submitpic/"+unpack_Entities)
        header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Referer": (url_vote+unpack_Entities)
        }
        # svae data ; return data
        data = {'key':key, 'server':server_id, 'userid':userid, 'url_image': url_image, 'url_getpic': url_getpic, 'url_post': url_submitpic, 'header': header, 'proxy': proxy,'proxy_Source':proxy_Source,'proxy_destination':proxy_destination,'logfail':logfail,'proxyfix':proxyfix,'proxy_blacklist':proxy_blacklist,'manyfail':manyfail,'genproxy':genproxy,'maxproxy': int(maxproxy) }
        return data
