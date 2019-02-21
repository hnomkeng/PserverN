import os, re,random,sys
from msvcrt import getch
class Cfixproxy:
    #fix proxy
    def Ffixproxy(data):
        while True:
            try:
                openfile = open(data['proxy_destination']).read().splitlines()
                rndProxy = random.choice(openfile)
                if rndProxy in open(data['proxy_blacklist']).read():
                    print('\n '+data['proxy']+' --- > proxy is blacklist')
                else:
                    return rndProxy

            except:
                print('\n Please Check you destination proxy file !! ' + data['proxy_destination'])
                junk = getch()
                sys.exit()
