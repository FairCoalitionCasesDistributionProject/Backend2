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

def run_algo(request, type):
    try:
        if not isinstance(request.data, dict) or not isvalidinput(request.data) or not isinstance(request.data['key'],str):
            return Response("Invalid Input")
        if 'type' in request.data.keys() and isinstance(request.data['type'], int) and request.data['type'] == 0:
            database.child(request.data['key'].replace('.','/')).set(json.dumps(request.data))
        else:
            database.child(request.data['key'].replace('.','/')).set(str(request.data['preferences']))
        
        prefs = request.data['preferences']
        div = Division(number_of_items=request.data['items'])
        div.add_parties([(i, request.data['mandates'][i]) for i in range(len(prefs))])
            
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
    return run_algo(request, 0)

@api_view(['POST'])
def AlgoResponseTestView(request):
    return run_algo(request, 1)

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
    
class FormTestView(APIView):
    def post(self, request):
        return Response(request.data)