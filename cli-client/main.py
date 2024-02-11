import argparse
import requests
import json
import sys
from pathlib import Path

def login(ar):
    url = 'http://127.0.0.1:5000/login'
    info = {'username': ar.username, 'password': ar.passw}
    res = requests.post(url, data=info, verify=False)
    
    json = res.json() 
    print(res.status_code)


    if (res.status_code == 200):
        print(json['accessToken'])
        home = str(Path.home())
        f = open(home + '/softeng20bAPI.token','w')
        f.write(json['accessToken'])
        f.close()
        sys.exit(0)
    return True


parser = argparse.ArgumentParser()
parser.add_argument('--username', help='Give username', required='TRUE')
parser.add_argument('--passw', help='Give password', required='TRUE')

args = parser.parse_args()

login(args)
sys.exit(1)
