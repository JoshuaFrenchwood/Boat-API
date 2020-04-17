#python library for making request
import requests

url = 'https://abs-boat-api.herokuapp.com/'
headers = {'Content-Type': 'application/json'}

def createBoat():
    r = requests.post(url+'data/create',headers=headers)
    if r.status_code == 200:
        print("Created Boat")
        data = r.json()
        result = {'speed':data['boat']['speed'] ,'direction': data['boat']['direction']}
    else:
        print('Only One Boat : createBoat()')
        result = None
    return result

def deleteBoat():
    r = requests.delete(url+'data/delete',headers=headers)
    if r.status_code == 200:
        print('Deleted Boat')
    else:
        print('No Boat Found : deleteBoat()')
    return None

def getBoat():
    r = requests.get(url+'data/get', headers = headers)
    if r.status_code == 200:
        print('Getting Boat')
        data = r.json()
        result = {'speed':data['boat']['speed'] ,'direction': data['boat']['direction']}
    else:
        print('No Boat Found : getBoat()')
        result = None
    return result

def updateBoat(speed, direction):
    data = {'speed':speed,'direction':direction}
    r = requests.post(url+'data/send', headers = headers, json = data)
    if r.status_code == 200:
        print('Updated Boat')
        data = r.json()
        result = {'speed':data['boat']['speed'] ,'direction': data['boat']['direction']}
    else:
        result = None
    return result