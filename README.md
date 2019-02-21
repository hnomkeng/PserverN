

![47280575](https://user-images.githubusercontent.com/47280575/53146145-aee41480-35d5-11e9-978d-cf243672ddf6.png)

**PserverN** is custom client  vote captcha to [Playserver](https://playserver.in.th)
use api by  [2captcha](https://2captcha.com/2captcha-api)

***PSN***  ` (PserverN Auto Vote) `

You must be sure that Priority of API parameters sent by software
[2captcha/edit](https://2captcha.com/setting/edit)
![2captcha/edi](https://user-images.githubusercontent.com/47280575/53150577-71868380-35e3-11e9-91a0-597f57a042ab.png)
![psn](https://user-images.githubusercontent.com/47280575/53148402-25d0db80-35dd-11e9-877f-002cf43d437e.gif)

**Usage:**

```py
USER:~: psn

#conifg | control\config.txt
[default]
server_id = <14705>                    # |server  id
userid = <playnew>                     # |user id for vote
key =  <key>                           # |key 2captcha
proxy = proxylist.txt                  # |proxy list for vote



[proxymode]
maxproxy = 4                            # |max proxy in proxy file default <0> use all proxy in file


[protect]         
log_FAIL = 1     # 0 = off            # |if fail vote system will proceed save image/<name = capchakey>.png 
proxyfix = 1     # 0 = off            # |if porxy fail to connect 
                                      # |system will auto use proxy in proxy/destination.txt
mf = 5                                # |max proxy fail connect for proxyfix <1>

```

***Proxy Checker***  ` (cleaning Death Proxy and save Working Proxy) `

![proxycheck](https://user-images.githubusercontent.com/47280575/53145094-7b06f000-35d1-11e9-97a5-0d6b1d6e43d5.gif)

**Usage**
```py
USER:~: proxy c

#conifg | control\config.txt
[proxymode]
genproxy = newproxy.txt               # |Check this file -----------------------------|
destination = proxy/destination.txt   # |Save Working proxy to this file--------------|
```



