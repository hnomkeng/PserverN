import os ,configparser


config = configparser.RawConfigParser()
config.readfp(open(r'config.txt'))
class datatxt:
    URL_SERVER = config.get('SERVER','URL')
    URL_POSTIMAGE = ("http://playserver.co/index.php/Vote/ajax_submitpic/"+URL_SERVER)
    URL_IMAGE = ("http://playserver.co/index.php/VoteGetImage/")
    URL_GETPIC = ("http://playserver.co/index.php/Vote/ajax_getpic/"+URL_SERVER)
    HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Referer": ("http://playserver.in.th/index.php/Vote/prokud/"+URL_SERVER)
    }


    SERVERID = config.get('USER','SERVERID')
    GAMEID = config.get('USER','GAMEID')
