#! python3
import requests
import json
import io
import tarfile
from vtapikey import apikey

def url_report():
   url = 'https://www.virustotal.com/vtapi/v2/url/scan'
   url2=input("Input a url to scan. Include http://")
   params = {'apikey': apikey, 'url':url2}
   response = requests.post(url, data=params)
   print(response.json())
   
def ip_report():
   ip=input("Input an IP address with this format: X.X.X.X ")
   url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
   params = {'apikey':apikey,'ip':ip}
   response = requests.get(url, params=params)
   print(response.json())


print('Welcome to the VT url scan script.')
choice=input("Do you want a url report[1] or ip report[2]?")

if choice=='1':
    url_report()
elif choice=='2':
    ip_report()
else:
    print("You must enter the digits 1 or 2 to make a choice.")
    print("Run the script again with correct input to use.")

