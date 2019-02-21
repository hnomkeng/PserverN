from prompt_toolkit.shortcuts import print_tokens
from prompt_toolkit.styles import style_from_dict
from pygments.token import Token
import time
from threading import Semaphore

screen_lock = Semaphore(value=1)

style = style_from_dict({
    Token.WARNING: '#b8cc00', #Orange
    Token.SUCCESS: '#00cc14',  #green
    Token.ERROR: '#cc1400', #rad
    Token.COMMAND: '#00cc14', #green
    Token.USER: '#00b8cc', #blue
    Token.TIME: '#ffffff', #White
    Token.DRFFZ: '#78827f',#Gray
    Token.SPROXY: '#2affb8', #grenn /2
    Token.PurpleX: '#e929ff', #purple
    Token.YellowX: '#e9ff28', #yellow

})


WARNING = [
    (Token.WARNING, '\n     WARNING !! '),

]

COMMAND = [
    (Token.USER, 'USER:~'),
    (Token.COMMAND, '$'),
]

# message usage ::
def USAGE_SET(proxy_Source,proxy_destination):
    USAGE = [
        (Token.DRFFZ, '     Usage:\n'),
        (Token.DRFFZ, '                proxy  | Proxy Mode  \n'),
        (Token.DRFFZ, '                         [c]  Check working proxy '),
        (Token.SPROXY,'control'),
        (Token.DRFFZ,'/'),
        (Token.SPROXY,'config.txt  '),
        (Token.DRFFZ,'╮\n'),
        (Token.DRFFZ, '                                                                      |\n'),
        (Token.COMMAND, '                              proxymode'),
        (Token.DRFFZ, ' <-----------------------------╯ \n'),
        (Token.ERROR, '                                       |---Source '),
        (Token.TIME, ': /'+proxy_Source+'         |'),
        (Token.USER, 'CHECK\n'),
        (Token.ERROR, '                                       |---destination'),
        (Token.TIME, ': /'+proxy_destination+'   |'),
        (Token.USER, 'SAVE\n'),
        (Token.DRFFZ, '                psn    | recapcha \n\n\n'),

        ]
    return USAGE




# message request ::
def message_request(proxy,command,message,submessage):

    if (command == 'GET'):
        message_fix = [
            (Token.TIME, '\n'+(time.strftime("%I:%M:%S%p |"))),
            (Token.SPROXY, ' ['),
            (Token.SPROXY,  proxy),
            (Token.SPROXY, '] '),
            (Token.SPROXY, 'GET'),
            (Token.SPROXY, ' < '),
            (Token.TIME, str(message)),
            (Token.SPROXY, ' > '),
            (Token.SPROXY,  str(submessage)+'\n')
            ]
        return message_fix
    elif (command == 'POST'):
        message_fix = [
            (Token.TIME, '\n'+(time.strftime("%I:%M:%S%p |"))),
            (Token.SUCCESS, ' ['),
            (Token.SUCCESS,  proxy),
            (Token.SUCCESS, '] '),
            (Token.SUCCESS, 'POST'),
            (Token.SUCCESS, ' < '),
            (Token.TIME, str(message)),
            (Token.SUCCESS, ' > '),
            (Token.SUCCESS,  str(submessage)+'\n')
            ]
        return message_fix
    elif (command == 'ERROR'):
        message_fix = [
            (Token.TIME, '\n'+(time.strftime("%I:%M:%S%p |"))),
            (Token.ERROR, ' ['),
            (Token.ERROR,  proxy),
            (Token.ERROR, '] '),
            (Token.ERROR, 'error !! '),
            (Token.ERROR, ' < '),
            (Token.TIME, str(message)),
            (Token.ERROR, ' > '),
            (Token.ERROR,  str(submessage)+'\n')
            ]
        return message_fix
    elif (command == 'FAIL'):
        message_fix = [
            (Token.TIME, '\n'+(time.strftime("%I:%M:%S%p |"))),
            (Token.DRFFZ, ' ['),
            (Token.DRFFZ,  proxy),
            (Token.DRFFZ, '] '),
            (Token.DRFFZ, 'fail !! '),
            (Token.DRFFZ, ' < '),
            (Token.DRFFZ, str(message)),
            (Token.DRFFZ, ' > '),
            (Token.DRFFZ,  str(submessage)+'\n')
            ]
        return message_fix


class Pmessage:
    #call message
    def WARNING_(message):
        screen_lock.acquire()
        print_tokens(WARNING, style=style),print(message+'\n')
        screen_lock.release()
    def USAGE_(proxy_Source,proxy_destination):
        screen_lock.acquire()
        print_tokens((USAGE_SET(proxy_Source,proxy_destination)), style=style)
        screen_lock.release()
    def COMMAND_():
        print_tokens(COMMAND, style=style)
        return ": "
    def GETPOST(proxy,command,message,submessage):
        screen_lock.acquire()
        print_tokens((message_request(proxy,command,message,submessage)), style=style)
        screen_lock.release()
