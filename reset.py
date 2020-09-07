# -*- coding: utf-8 -*-
import requests
import subprocess
import urllib

message = 'iisResetMrm01'
group = '' #get group id by @id37bot

def send_to_telegram(chat,message):
	try:
		print('Telegram:',message)
		headers = {
			"Origin": "http://scriptlab.net",
			"Referer": "http://scriptlab.net/telegram/bots/relaybot/",
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
			}
		url     = "http://scriptlab.net/telegram/bots/relaybot/relaylocked.php?chat="+chat+"&text="+urllib.parse.quote_plus(message)
		return requests.get(url,headers = headers)
	except Exception as e:
		return str(e)

try:
    print('Content-Type: text/plain')
    print('')    
    result = 'result: '
    result += str( subprocess.call('schtasks /Run /TN "iisResetMrm01"') )
    print(result)
    send_to_telegram(group,message+': '+result)

except Exception as e:
    print(str(e))
