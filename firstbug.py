

import urllib3
response = urllib3.request("https://www.baidu.com")
print (response.read())
