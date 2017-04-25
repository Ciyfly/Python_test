# -*- coding: utf-8 -*-
import urllib
import chardet
import os
import re
regex=r'blob-code blob-code-inner js-file-line">(.+?)</td>'
url="https://github.com/racaljk/hosts/blob/master/hosts"
hosts='C:\Windows\System32\drivers\etc\hosts'
print 'Start getting hosts'
html1 = urllib.urlopen(url)
html = html1.read()
html1.close()
ip = re.findall(regex,html)
print 'Start setting hosts'
print ip
if os.path.exists(hosts):
	os.remove(hosts)
print '......'
for a in ip:
	with open(hosts,'a') as f:
		f.write(a+ "\n")


