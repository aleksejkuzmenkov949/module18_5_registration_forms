from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    context = {
        'items': [
            {'name': 'Super Mario'},
            {'name': 'Super Wario'},
            {'name': 'Super Mario Kart'}
        ]
    }

    return render(request, 'third_task/games.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')


