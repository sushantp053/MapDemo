from django.shortcuts import render
from home.models import Natoshi
from django.core.serializers import serialize



def home(request):

    d = serialize("geojson", Natoshi.objects.all())
    data = {"data": d}
    crops = Natoshi.objects.all().values_list('crop', flat=True).distinct()
    print(crops)


    return render(request, 'home.html', {'natoshi': data, "crops": crops})

def indextest(request):
    return render(request, 'index.html')
