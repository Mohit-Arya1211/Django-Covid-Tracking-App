from django.shortcuts import render
import requests
import json
from myApp.config import *

url = url

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworld(request):
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)

    mylist = []
    noofresults = int(response['results'])
    for i in range(0, noofresults):
        mylist.append(response['response'][i]['country'])
        context = {'mylist' : mylist}
    return render(request, 'helloworld.html', context)