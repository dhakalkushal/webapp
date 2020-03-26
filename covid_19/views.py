from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = "https://covid19.mathdro.id/api"

    object_list = []

    r = requests.get(url).json()

    data = {
        'confirmed' : r['confirmed']['value'],
        'recovered':r['recovered']['value'],
        'deaths':r['deaths']['value'],
        'image': r['image']
    }
    context = {
        'data' : data
    }

    return render(request, 'covid_19/home.html', context)