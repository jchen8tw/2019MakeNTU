import requests

r = requests.get("http://ec2-52-69-255-179.ap-northeast-1.compute.amazonaws.com/RPi?b=234")
print(r.status_code)


