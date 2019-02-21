import requests, re, os,ap
from reqeusthttp import*

if __name__=='__main__':
    #wait for new fix
    checksum,URL_IMAGE = GET.IMAGE()
    GETIMAGE = GET.SAVEIMAGE(checksum,URL_IMAGE)
    if (GETIMAGE == True):
        captcha = input('What you see ? :')
        POST.POSTIMAGE(captcha,checksum)
