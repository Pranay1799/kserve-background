import webview
import time
import json
import requests
import datetime

def toggle_fullscreen(window):
    # wait a few seconds before toggle fullscreen:

    window.toggle_fullscreen()
    timeout = 27
    access_url = "https://kserve.qandle.com/oauth/access-token"

    access_payload = json.dumps({
                                "grant_type": "client_credentials",
                                "client_id": "6371208025",
                                "client_secret": "khyrdr56fd87hfr086hg53srf"
                                })
    access_headers = {
                    'Content-Type': 'application/json'
                    }

    access_response = requests.request("POST", access_url, headers=access_headers, data=access_payload)


    user_url = "https://kserve.qandle.com/client-api/custom/all-user/7294"

    user_headers = {
                    'Authorization': f"Bearer {access_response.json()['access_token']}"
                }

    user_response = requests.request("GET", user_url, headers=user_headers)

    joiningdate = user_response.json()['data']['joining_date']
    joining_date = datetime.datetime.strptime(joiningdate,'%d-%b-%Y')
    todays_date = datetime.datetime.now()
    total_days = todays_date-joining_date
    
    if total_days.days % 90 == 0:
        timeout = 150
    time.sleep(timeout)
    window.destroy()

def alt_f4(event):
    global pressed_f4


if __name__ == '__main__':
    window = webview.create_window('Kserve','http://172.16.11.3/emp/login/')
    webview.start(toggle_fullscreen, window)