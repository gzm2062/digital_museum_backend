from urllib import request

from requests import post

resp = post("http://127.0.0.1:5000/test", json={"name": "gzm"})
print(resp)
print(resp.json())