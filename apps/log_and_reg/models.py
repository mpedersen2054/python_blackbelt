from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
from ..travels.models import Travel

class UserManager(models.Manager):
    def validate_register(self, registerData):
        errors = []
        # letter_only_regex = '^[a-zA-Z]+$'
        # email_format_regex = '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'

        name_valid          = False
        username_valid      = False
        password_valid      = False
        password_conf_valid = False
        user_exists         = False

        # first_name & last_name more than 2 chars, letters only
        if len(registerData['name']) > 3:
            name_valid = True
        # email valid format & exists
        if len(registerData['username']) > 3:
            username_valid = True
        # password exists, more than 8 chars
        if len(registerData['password']) > 8:
            password_valid = True
        # password matches password conf
        if registerData['password'] == registerData['password_conf']:
            password_conf_valid = True

        # check if email exists in the db
        user = User.objects.filter(username=registerData['username'])
        if len(user) > 0:
            user_exists = True

        if not name_valid:
            errors.append('The name was invalid. It needs to be only letters and at least 2 characters')
        if not username_valid:
            errors.append('The username was not valid.')
        if not password_valid:
            errors.append('The password was not valid.')
        if not password_conf_valid:
            errors.append('The password confirmation did not match the password.')
        if user_exists:
            errors.append('The user already exists in the database. Try a different email.')

        return errors

    def validate_login(self, loginData):
        errors = []

        user = User.objects.filter(username=loginData['username']).first()

        if not user:
            errors.append('A user with that email doesnt exist in the database. Please register.')
        else:
            pwhash = user.password.encode()
            if pwhash == bcrypt.hashpw(loginData['password'].encode(), pwhash):
                print 'PASSWORD MATCHED!!!'
            else:
                errors.append('User with that email exists, but password was incorrect.')

        if user:
            return (user.id, errors)
        else:
            return (None, errors)

    def encrypt_password(self, password):
        if not password:
            return False
        else:
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=100)
    username   = models.CharField(max_length=100)
    password   = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trips      = models.ManyToManyField(Travel)
    objects    = UserManager()
