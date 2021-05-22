# frida_rpc_player.py

'''
POST /WebObjects/MZBuy.woa/wa/buyProduct HTTP/1.1
Host: p46-buy.itunes.apple.com
User-Agent: iTunes/12.6.5 (Windows; Microsoft Windows 10.0 x64 Enterprise Edition (Build 19042); x64) AppleWebKit/7605.1033.1002.2
Content-Length: 1226
Content-Type: application/x-apple-plist
X-Dsid: 12263680861
X-Apple-Tz: 28800
X-Apple-MD: AAAABAAAABA3hIN/KYf4Ri4tdZAiwaB5
Cookie: amp=JG7EpvImu+/h0yS5mTqQMLarQce6xuYNfyzC6cun/bRt+7VLQUqfUrDB4cdRyV6SLDGBRCG3Oz/PcY28nx94GdTGkdOYX83a54KHZTSq3jI=; amia-12263680861=dPQK5oK/9b6q7HeGIids4a6gE5oiE8yLcVjQO7EknSTERhI0OawL4FQcmJ60560H+PbZhCCt6Na8jLSDiU09aw==; mt-asn-12263680861=2; mt-tkn-12263680861=AmDauzfLChTup9vGq17bGVJvSurhbsyoCLyrpJG8t8uECuyAI3xr3o/vS9pVpKeg4dSlCxJtLUS8+H47Qtpou0VGgGBAn/dXAPozhdJKTyPdUqyT4My89dujXg48XNgIVUjFj2w4IhN1gg5wn3BfSg1bFChodxuHadsRibnYzkUPmR+TVTnivu9e4/QLJmh58Va8rmg=; mt-tkn-10255130069=Ala2nKdNzZWOlapGgvRzcNExINc8j4sbrcMn3ruJ9M3Cb17MGiGqvyTe9yUzh/fSNLEL+4s0j57Eht/AWXrG2e3+GptHZlTi1vZ4a+3PdD9dtfSP8no7s9/bMX6JTtnE+fwV1z8QudsvAs+kjEz0MqFgoxFZZntBKI1L81+CBTnmsBolRdk+wqqPGZ3AD5bdybUTwD4=; countryVerified=1; mzf_in=467080; itspod=46; vrep=CN3W49ctEgQIChAAEgQICBAAEgQIBxAAEgQIBBAAEgQIDRAAEgQIBhAAEgQIDBAAEgQIAxAAEgQICRAAEgQIEBAAEgQIDhAAEgQIARAAEgQIDxAAEgQIERAAEgQIBRAAEgQICxAAEgQIAhAA; wosid-lite=jRoFTHWbZZZkSOfvfDELf0; mz_at_ssl-12263680861=AwUAAAECAAHXHQAAAABgqAeMT5/7LbF5106/zxFn9xH4n7jgwEw=; mz_at0-12263680861=AwQAAAECAAHXHQAAAABgp/7Z1enk1z4615lhp9QKlDQfmo7Hq60=; pldfltcid=524b36a58d0d4249a127affd05921dab046; X-Dsid=12263680861; xp_ab=1#WqjkRLH+-2+TCEF_ea00#yNFpB6B+-2+c9imSgD01; xp_abc=TCEF_ea00; mz_at0-10255130069=AwQAAAECAAHXHQAAAABgnNBzeacT12/WPi/iSOROyaMVQrfmkqE=; mz_at_ssl-10255130069=AwUAAAECAAHXHQAAAABgnNBzNHT9PbcrsAARLEWi0+8ElnKZ54c=; xp_ci=3z3h6Y0vzFQQz4XtzB5DzZvQkYhyo
X-Apple-AMD-M: rjK8HkwTcIoiOk6UoA9LXta0h/19+ss41RU7YLxGunAtLnl1Fus5i4VS56O71ifgDWwrEl/jIbPrDLfS
X-Apple-AMD: AAAABAAAABCqItI0AgfIcPIc0+zGpNtr
X-Apple-Store-Front: 143462-9,32
Accept-Language: zh-cn
Date: Fri, 21 May 2021 21:33:42 GMT
X-Apple-MD-M: rjK8HkwTcIoiOk6UoA9LXta0h/2Qyn969daQuVAdJbkmCnWee7s+joaQ3fvc4v1JTJB0sUJcDwc0Q12z
X-Apple-I-MD-RINFO: 50660608
X-Apple-I-MD-M: rjK8HkwTcIoiOk6UoA9LXta0h/0W22FXNYql4KAM12/n20O3iVf54IK85PbrLb51CvEfn5/b6eoX5d1d
X-Apple-I-MD: AAAABQAAABA+EMexoFPqOMeyQ5zIkQYPAAAAAg==
Accept-Encoding: gzip, deflate
Connection: close

<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
	<key>guid</key>
	<string>46994789.C2E39C5C.B1D62DC2.025D2569.3D6E49B5.AB7F7EB4.F6D17565</string>
	<key>kbsync</key>
	<data>
	AAQAA5+HiDofKn/iW9aKVsKo1XU0cRuzPrQGMfC57fQaA7YaZBWlSS+s4SS2Ay6pchYG
	x/h+cJccHMoA/NDtHcWsRl9nmDwzAnuW9WH7nHQAEt95wkj2eMQVBHyj3OSkSoEGFnS8
	r4irSIve3V4np1lvbEUgHdJmOEV6gAd8SFzItmgxFImn55qoUX/xt4pdXagPmhBXaYFI
	+B/uYLxOYLO4fM1fGpQQ8/1EIpzrbahFjpG8L8kMjhVIWpn2Ut30p2deyjcL47JbSjx7
	/RId4XZlSEqXf9SOETcsxCkVhDWTghGYRWKlEe7j32CVrxOkg2lvlQLHB1XBhTpQiLSm
	PR0hDIG5dQif0jaIeQJ9zGqq3kgkl9RlFHGbcvfMdrJsYGOgYMzXh1jfF/v21xPfauYh
	PIE9LQu/TTiAGDvS+BYrM2xVaPHZPNUpLaVlk/2zIqiWo/Zj2se4FXGOl4LAVKqrbOYN
	2YONkSY4CQOZTmNmoO6SBU2NJHBYtVVeIhOLGLoS9/xzPwMdFevvZJFD7iQvL0RDKCBt
	z5r7dnFz2WlZsdx0aMsbV3HRdnJtmBh7zA3AaO/4rJtWAQqAID2gAF8YMoNdJJp13Bdr
	f34iRpVYbsDxrBNJXtanTgDdNO3xXpyZhQTgOrBDcsv7mD68E1E6bE5ac97/z9R8cLf0
	8/X8/ie7tUBcqVThW81DiM4RGh3LSg==
	</data>
	<key>price</key>
	<string>0</string>
	<key>pricingParameters</key>
	<string>STDRDL</string>
	<key>productType</key>
	<string>C</string>
	<key>salableAdamId</key>
	<string>1234806557</string><key>appExtVrsId</key>
	<string>839637337</string>
</dict>
</plist>
'''

import sys
import codecs
import frida
from time import sleep
import requests
import plistlib
import re
import json
import os
import base64
from get_version import *

session = frida.attach('iTunes.exe')
#session = frida.attach('iTunesFucked.exe')

with codecs.open(os.path.dirname(os.path.realpath(__file__)) + '/get_header_rpc.js', 'r', 'utf-8') as f:
    source = f.read()

script = session.create_script(source)
script.load()

def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])

script.on('message', on_message)

rpc = script.exports

PAYLOAD='''<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
	<key>guid</key>
	<string>%s</string>
	<key>kbsync</key>
	<data>
	%s
	</data>
	<key>price</key>
	<string>0</string>
	<key>pricingParameters</key>
	<string>STDRDL</string>
	<key>productType</key>
	<string>C</string>
	<key>salableAdamId</key>
	<string>%s</string>
	<key>appExtVrsId</key>
	<string>%s</string>
</dict>
</plist>
'''

def getIpaDownUrl(appUrl, storeFront):
    appId, appVer = getAppInfo(appUrl, storeFront)
    print("Got app's id: %s, ver: %s" % (appId, appVer))

    retHdrs = rpc.get_header("https://p46-buy.itunes.apple.com/WebObjects/MZBuy.woa/wa/buyProduct")
    retHdrs["Content-Type"] = "application/x-apple-plist"
    print("Got iTunes header: %s" % retHdrs)
    kbsync = bytes.fromhex(retHdrs.pop('kbsync'))
    guid = retHdrs.pop('X-Guid')

    payload = PAYLOAD % (guid, base64.b64encode(kbsync).decode(), appId, appVer)
    print(payload)
    r = requests.post('https://p46-buy.itunes.apple.com/WebObjects/MZBuy.woa/wa/buyProduct', headers=retHdrs, data=payload)
    print(r, r.text)
    t = plistlib.loads(r.text.encode('utf-8'))
    sinf = t['songList'][0]['sinfs'][0]['sinf']
    ipaUrl = t['songList'][0]['URL']
    return ipaUrl, appId, appVer, sinf


def download_file(url, filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return filename


def main(args):
    store = args[0].upper()
    url = args[1]
    filename = args[2]
    
    #downUrl = getIpaDownUrl("https://apps.apple.com/jp/app/id1377018522", '143462-9,32')
    downUrl, appId, appVer, sinf = getIpaDownUrl(url, store)
    print("Got down url: %s" % (downUrl))
    
    download_file(downUrl, filename + ".ipa")
    with open('curver.txt', 'w') as f:
        f.write(appVer)
    
    with open(filename + '.sinf', 'wb') as f:
        f.write(sinf)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))

session.detach()