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
    mylist = []
    noofresults = int(response['results'])
    for i in range(0, noofresults):
        mylist.append(response['response'][i]['country'])
    
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                total = response['response'][x]['cases']['total']
                recovered = response['response'][x]['cases']['recovered']
                critical = response['response'][x]['cases']['critical']
                deaths = int(total) - int(active) -int(recovered)
        
        context =  {'selectedcountry' : selectedcountry, 'mylist' : mylist, 'new' : new,'active' : active,'critical' : critical,'recovered' : recovered,'deaths' : deaths,'total' : total}
        return render(request, 'helloworld.html', context)
    