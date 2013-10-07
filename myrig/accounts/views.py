from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.utils.http import urlquote_plus
from myrig.accounts.forms import OpenIDLoginForm, ChangeDisplayNameForm

def login(request):
    '''
    Displays the login form
    '''
    if request.method == 'POST':
        form = OpenIDLoginForm(request.POST)
        if form.is_valid():
            return redirect('%s?openid_identifier=%s' % (
                reverse('social:begin', args=('openid',)),
                urlquote_plus(form.cleaned_data['openid']),
            ))
    else:
        form = OpenIDLoginForm()
    return render(request, 'accounts/login.html', {
        'title':       'Login',
        'description': 'Please enter your OpenID below to login or register for a new account.',
        'form':        form,
        'action':      'Login',
    })

def logout(request):
    '''
    Logs the user out
    '''
    logout_user(request)
    return redirect(reverse('home'))

@login_required
def profile(request):
    '''
    Displays the user's profile page
    '''
    return render(request, 'accounts/profile.html')

@login_required
def change_display_name(request):
    '''
    Allows the user to change their display name
    '''
    if request.method == 'POST':
        form = ChangeDisplayNameForm(request.POST)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name  = form.cleaned_data['last_name']
            request.user.save()
            return redirect(reverse('profile'))
    else:
        form = ChangeDisplayNameForm(initial={
            'first_name': request.user.first_name,
            'last_name':  request.user.last_name,
        })
    return render(request, 'form.html', {
        'title':       'Change Display Name',
        'description': 'Please fill in the form below to change your display name.',
        'form':        form,
        'action':      'Submit',
    })
