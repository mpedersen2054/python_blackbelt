from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    if not 'user_id' in request.session \
    or request.session['user_id'] == None:
        messages.error(request, 'You need to be logged in to go there.')
        return redirect('log_and_reg:index')
    context = {
        'home': True
    }
    return render(request, 'travels/index.html', context)

def show_travel(request, id):
    return render(request, 'travels/show_travel.html')

def add_travel(request):
    return render(request, 'travels/new_travel.html')
