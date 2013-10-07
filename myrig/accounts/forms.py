from django import forms

class OpenIDLoginForm(forms.Form):
    '''
    Prompts a user for the URL of their OpenID
    '''
    
    openid = forms.URLField(help_text='The absolute URL of your OpenID')

class ChangeDisplayNameForm(forms.Form):
    '''
    Prompts a user for a first and last name
    '''
    
    first_name = forms.CharField(help_text='Your first name (given name)')
    last_name  = forms.CharField(help_text='Your last name (surname)')
