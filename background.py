import os
import sys, string, os
import keyboard
import requests
import json
import time

    
while True:
    try:

        empid=os.environ['USERPROFILE'].split('\\')[2]
        
        finalUrl = f"http://172.16.11.3/api/biometric/{empid}"
        response = requests.request("GET", url=finalUrl)
        time.sleep(5)
        
        if response.json()['status'] == 200:
            if response.json()['message'] == True:
                break
            else:
                keyboard.block_key('tab') 
                keyboard.block_key('alt')
                keyboard.block_key('windows')
                os.system("windows.exe")
    except Exception as ep:
        break


