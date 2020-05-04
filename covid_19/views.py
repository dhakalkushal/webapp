from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = "https://covid19.mathdro.id/api"

    url2 = "https://corona.lmao.ninja/v2/countries"

    url3 = "https://corona.lmao.ninja/v2/countries/Nepal"


    object_list = []

    r = requests.get(url).json()

    r2 = requests.get(url2).json()

    r3 = requests.get(url3).json()

    data = {
        'confirmed' : r['confirmed']['value'],
        'recovered':r['recovered']['value'],
        'deaths':r['deaths']['value'],
        'image': r['image']
    }

    data2 = {
        'country': r3['country'],
        'cases': r3['cases'],
        'todayCases': r3['todayCases'],
        'deaths': r3['deaths'],
        'todayDeaths': r3['todayDeaths'],
        'recovered': r3['recovered'],
        'active': r3['active'],
        'critical': r3['critical'],
        #'flag': r['flag'],
    }

    for x in range(211):

        test = {
            'country': r2[x]['country'],
            'cases': r2[x]['cases'],
            'todayCases' : r2[x]['todayCases'],
            'deaths' : r2[x]['deaths'],
            'todayDeaths' : r2[x]['todayDeaths'],
            'recovered' : r2[x]['recovered'],
            'active' : r2[x]['active'],
            'critical' : r2[x]['critical'],
        }
        object_list.append(test)

    context = {
        'data' : data,
        'object_list': object_list,
        'data2':data2,
    }

    return render(request, 'covid_19/home.html', context)

def yesterday(request):

    url = "https://covid19.mathdro.id/api"

    url3 = "https://corona.lmao.ninja/v2/countries/Nepal"

    url4 = "https://corona.lmao.ninja/v2/yesterday"

    yesterday_object_list = []

    r = requests.get(url).json()

    r4 = requests.get(url4).json()

    r3 = requests.get(url3).json()

    data = {
        'confirmed' : r['confirmed']['value'],
        'recovered':r['recovered']['value'],
        'deaths':r['deaths']['value'],
        'image': r['image']
    }

    data2 = {
        'country': r3['country'],
        'cases': r3['cases'],
        'todayCases': r3['todayCases'],
        'deaths': r3['deaths'],
        'todayDeaths': r3['todayDeaths'],
        'recovered': r3['recovered'],
        'active': r3['active'],
        'critical': r3['critical'],
        #'flag': r['flag'],
    }

    for x in range(211):

        test = {
            'country': r4[x]['country'],
            'cases': r4[x]['cases'],
            'todayCases' : r4[x]['todayCases'],
            'deaths' : r4[x]['deaths'],
            'todayDeaths' : r4[x]['todayDeaths'],
            'recovered' : r4[x]['recovered'],
            'active' : r4[x]['active'],
            'critical' : r4[x]['critical'],
        }
        yesterday_object_list.append(test)

    context = {
        'data': data,
        'data2': data2,
        'yesterday_object_list': yesterday_object_list,
    }

    return render(request, 'covid_19/yesterday.html', context)


def country_detail(request, country):

    url = "https://corona.lmao.ninja/countries/{}"

    r = requests.get(url.format(country)).json()

    data = {
        'country': r['country'],
        'cases': r['cases'],
        'todayCases': r['todayCases'],
        'deaths': r['deaths'],
        'todayDeaths': r['todayDeaths'],
        'recovered': r['recovered'],
        'active': r['active'],
        'critical': r['critical'],
        'flag': r['countryInfo']['flag'],
    }

    context = {
        'data': data,
    }

    return render(request, 'covid_19/country_detail.html', context)

def compare(request):

    return render(request, 'covid_19/compare.html',)