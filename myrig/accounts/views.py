from django.contrib.auth import logout as logout_user
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.utils.http import urlquote_plus
from myrig.accounts.forms import OpenIDLoginForm

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
    return render(request, 'form.html', {
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
    
