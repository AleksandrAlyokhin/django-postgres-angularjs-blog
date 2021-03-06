# -*- coding: utf-8 -*-

from django.contrib import auth
import json
from jsonview.decorators import json_view


# update profile
@json_view
def actionProfileUpdate(request):
    """Update record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    validateResult, validateCode = User.validateProfileUpdateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return {'code': 'account/usernofound', 'values': [json_data['email']]}, 404

    #try:
    validateResult, validateCode = user.updateFromJsonObject(json_data)
    if validateCode != 200:
        return validateResult, validateCode

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    #except:
    #    return {'code': 'account/profile/fail/update'}, 404

    return {'code': 'ok', 'data': [user.getUserData()]}


# Login
@json_view
def actionLogin(request):
    """Login action"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    validateResult, validateCode = User.validateLoginJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except KeyError:
        emailField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = ''

    try:
        user = User.objects.get(email=emailField)
    except User.DoesNotExist:
        return {'code': 'account/usernofound', 'values': [emailField]}, 404

    user = auth.authenticate(username=user.username, password=passwordField)

    if user is None:
        return {'code': 'account/wrongpassword'}, 404

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/notactive'}, 404


# Logout
@json_view
def actionLogout(request):
    """Logout action"""

    auth.logout(request)
    return {'code': 'ok'}
