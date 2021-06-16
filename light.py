# light.py
import requests
import json

class Light:
    def __init__(self, device, model): 
        self.device = device
        self.model = model 
        self.base_url = 'https://developer-api.govee.com/v1/devices'
        self.headers = {
            "Govee-API-Key": 'YOUR_API_KEY_HERE', 
            "Content-Type": 'application/json'
        }
    # create a formatted string of the Python JSON object
    def _jprint(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    # Provide 'on' or 'off'
    def turn(self, action):
        params = {
            'device': self.device,
            'model': self.model,
            'cmd': {
                "name": 'turn',
                "value": action
            }
        }
        response = requests.put(self.base_url+"/control",headers=self.headers,json=params)
        print(response.status_code)
        self._jprint(response.json())


    # Provide R,G,B values of the color you want (0-255)
    def color(self,r,g,b):
        params = {
            'device': self.device,
            'model': self.model,
            'cmd': {
                "name": "color",
                "value": {
                    "r": r,
                    "g": g,
                    "b": b
                }
            }
        }
        response = requests.put(self.base_url+"/control",headers=self.headers,json=params)
        print(response.status_code)
        self._jprint(response.json())

    # Provide temperature value (2000-9000)
    def temperature(self, value):
        params = {
            'device': self.device,
            'model': self.model,
            'cmd': {
                "name": "colorTem",
                "value": value
            }
        }
        response = requests.put(self.base_url+"/control",headers=self.headers,json=params)
        print(response.status_code)
        self._jprint(response.json())

    # Provide brightness value (0-100)
    def brightness(self, value):
        params = {
            'device': self.device,
            'model': self.model,
            'cmd': {
                "name": "brightness",
                "value": value
            }
        }
        response = requests.put(self.base_url+"/control",headers=self.headers,json=params)
        print(response.status_code)
        self._jprint(response.json())


    # Returns Devices 
    def getDevices(self):
        response = requests.get(self.base_url,headers=self.headers)
        print(response.status_code)
        self._jprint(response.json())



