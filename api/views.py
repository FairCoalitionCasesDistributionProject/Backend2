from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import pyrebase
import json
from .division import Division
from .util import *
from .inputcheck import isvalidinput


config = {
    "apiKey": "AIzaSyBrRTqVU9Nk4tMFfKW1aAYs4V3BkmNr8PM",
    "authDomain": "faircoalitiondistribution.firebaseapp.com",
    "projectId": "faircoalitiondistribution",
    "storageBucket": "faircoalitiondistribution.appspot.com",
    "messagingSenderId": "986413816761",
    "appId": "1:986413816761:web:ddcb6c8eda93ff0e46b468",
    "databaseURL": "https://faircoalitiondistribution-default-rtdb.europe-west1.firebasedatabase.app"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def run_algo(json_data, type):
    try:
        if not isinstance(json_data, dict) or not isvalidinput(json_data) or not isinstance(json_data['key'],str):
            return Response("Invalid Input")
        if 'type' in json_data.keys() and isinstance(json_data['type'], int) and json_data['type'] == 0:
            database.child(json_data['key'].replace('.','/')).set(json.dumps(json_data))
        else:
            database.child(json_data['key'].replace('.','/')).set(str(json_data['preferences']))
        
        prefs = json_data['preferences']
        div = Division(number_of_items=json_data['items'])
        div.add_parties([(i, json_data['mandates'][i]) for i in range(len(prefs))])
            
        for i in range(len(prefs)):
            div.set_party_preferences(i, normalize(prefs[i]))
        allocation = transpose(bundle_to_matrix(div.divide()))
        if type == 0:
            return Response(str(allocation).replace("[","{").replace("]","}"))
        else:
            return Response({"allocation": allocation, "rounded_allocation": round_allocation(allocation)})
        
    except Exception as e: 
        return Response("Encountered an error: " + str(e))

@api_view(['POST'])
def AlgoResponseView(request):
    if isinstance(request.data, dict) and "_content" in request.data.keys() and isinstance(request.data['_content'], str):
            return run_algo(json.loads(request.data['_content']), 0)
    else:
        return run_algo(request.data, 0)

@api_view(['POST'])
def AlgoResponseTestView(request):
    if isinstance(request.data, dict) and "_content" in request.data.keys() and isinstance(request.data['_content'], str):
            return run_algo(json.loads(request.data['_content']), 1)
    else:
        return run_algo(request.data, 1)

@api_view(['POST'])
def ReturnSaveView(request):
    try:
        if not isinstance(request.data['key'],str):
            return Response(-1)
        data = database.child(request.data['key'].replace('.','/')).get().val()
        if not isinstance(data,str):
            return Response(-1)
        return Response(data)
    except:
        return Response(-1)