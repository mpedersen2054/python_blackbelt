from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
import datetime
from .models import User

# Create your views here.
def index(request):
    if not 'user_id' in request.session:
        request.session['user_id'] = None
    context = {
    }
    return render(request, 'log_and_reg/index.html', context)

def register(request):
    errors = User.objects.validate_register(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('log_and_reg:index')
    else:
        encrypted_password = User.objects.encrypt_password(request.POST['password'])
        new_user = User.objects.create(
            name     = request.POST['name'],
            username = request.POST['username'],
            password = encrypted_password
        )
        request.session['user_id'] = new_user.id
        messages.success(request, 'Successfully registered user.')
        return redirect('travels:index')

def login(request):
    login = User.objects.validate_login(request.POST)
    user_id = login[0]
    errors = login[1]
    if len(errors) > 0 or not user_id:
        for error in errors:
            messages.error(request, error)
        return redirect('log_and_reg:index')
    else:
        request.session['user_id'] = user_id
        messages.success(request, 'Successfully logged in.')
        # send to admin dash if admin, else send to user dash
        return redirect('travels:index')

def logout(request):
    request.session.flush()
    messages.error(request, 'Successfully logged out.')
    return redirect('log_and_reg:index')


def success(request):
    return render(request, 'log_and_reg/success.html')
