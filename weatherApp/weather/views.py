from django.shortcuts import render


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

    return render(request, 'weather/index.html')
