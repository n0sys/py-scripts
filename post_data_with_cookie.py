import requests

# POST url
URL = "http://www.example.com"

# cookies
jar = requests.cookies.RequestsCookieJar()
jar.set('Name', 'Value', domain='example.com', path='/')

# Post data
data = {
"key":"value",
}

r = requests.post(URL, data=data, cookies=jar)
if r.status_code == 200:
   print("request sent successfully")
