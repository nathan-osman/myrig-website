from django import forms

class OpenIDLoginForm(forms.Form):
    '''
    Prompts a user for the URL of their OpenID
    '''
    
    openid = forms.URLField(help_text='The absolute URL of your OpenID')
