from django import forms
from .models import MyUser, Interests, Skills
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
#from django.contrib.admin.widgets import AdminDateWidget

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class UserForm(forms.Form):
        username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class':'form-control'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
        email = forms.EmailField(label=_("Email address"))
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProfileForm(forms.Form):
        firstname = forms.CharField(max_length = 120, required = False, widget=forms.TextInput(attrs={'class':'form-control'}))
        lastname = forms.CharField(max_length = 120, required = False,widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(required = False,widget=forms.TextInput(attrs={'class':'form-control'}))
        skype = forms.CharField(required = False,widget=forms.TextInput(attrs={'class':'form-control'}))
        skill = forms.ModelChoiceField(required = False, queryset = Skills.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
        searching = forms.BooleanField(required = False)
class SearchForm(forms.Form):
    text = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class':'form-control'}))