from django.shortcuts import render
from home.models import Natoshi
from django.core.serializers import serialize



def home(request):

    d = serialize("geojson", Natoshi.objects.all())
    data = {"data": d}


    return render(request, 'home.html', {'natoshi': data})
