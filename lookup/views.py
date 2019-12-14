from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=44094&distance=5&API_KEY=E88988C7-32DD-4683-83B7-602757C25164")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e: 
        api = "Error..."


    return render(request, 'home.html', {'api': api}) 

def about(request):
    return render(request, 'about.html', {})

