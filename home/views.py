from django.shortcuts import render
from products.models import Testimony


def index(request):
    context = {
        'testimonies': Testimony.objects.all().order_by('-id')[:3]
    }
    return render(request, 'home/index.html', context)
