from django.shortcuts import render
from home.models import Natoshi


def home(request):
    natoshi = Natoshi.objects.all()

    return render(request, 'home.html', {'natoshi': natoshi})
