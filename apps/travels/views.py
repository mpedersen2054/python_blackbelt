from django.shortcuts import render, redirect
from django.contrib import messages
from ..log_and_reg.models import User
from .models import Travel
from datetime import datetime

# Create your views here.
def index(request):
    if not 'user_id' in request.session \
    or request.session['user_id'] == None:
        messages.error(request, 'You need to be logged in to go there.')
        return redirect('log_and_reg:index')

    user = User.objects.filter(id=request.session['user_id']).first()
    trips = Travel.objects.all()
    print user.trips.all()

    user_trips = user.trips.all()

    context = {
        'home': True,
        'user': user,
        'trips': trips,
        'user_trips': user_trips
    }
    return render(request, 'travels/index.html', context)

def show_travel(request, id):
    if not 'user_id' in request.session \
    or request.session['user_id'] == None:
        messages.error(request, 'You need to be logged in to go there.')
        return redirect('log_and_reg:index')

    return render(request, 'travels/show_travel.html')

def add_travel(request):
    if not 'user_id' in request.session \
    or request.session['user_id'] == None:
        messages.error(request, 'You need to be logged in to go there.')
        return redirect('log_and_reg:index')

    return render(request, 'travels/new_travel.html')

def create_travel(request):
    if request.method != 'POST':
        return redirect('travels:add_travel')
    # print 'REQPSOT: ', request.POST

    user = User.objects.filter(id=request.session['user_id']).first()

    errors = Travel.objects.check_validity(request.POST)

    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('travels:add_travel')
    else:
        formatted_data = Travel.objects.format_data(request.POST, user)
        trip = Travel.objects.create(
            destination = formatted_data['destination'],
            description = formatted_data['description'],
            date_from = formatted_data['date_from'],
            date_to = formatted_data['date_to'],
            added_by = user
        )
        user.trips.add(trip)
        user.save()
        # print 'FORMATTED DATA!', formatted_data
        messages.success(request, 'Successfully added trip!')
        return redirect('travels:index')
