import urllib

response = urllib.urlopen("http://cpc.people.com.cn/gbzl/index.html")

print response.read()