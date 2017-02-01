from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'home': True
    }
    return render(request, 'travels/index.html', context)

def show_travel(request, id):
    return render(request, 'travels/show_travel.html')

def add_travel(request):
    return render(request, 'travels/new_travel.html')
