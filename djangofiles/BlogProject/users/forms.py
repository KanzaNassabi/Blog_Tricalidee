from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

ROLES = [
    #('Admin', 'Admin'),
    ('Reader', 'Reader'),
    ('Author', 'Author'),
]
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #image = forms.ImageField(required=False)
    type = forms.ChoiceField(choices = ROLES, label="", initial='', widget=forms.Select(), required=False)
    #forms.CharField(max_length=100,help_text='user type')
    class Meta:
        model = User
        fields =['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta: 
        model = User
        fields =['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image','type']
    def clean(self):
        cleaned_data = super(ProfileUpdateForm, self).clean()
        #fields Validation 
        return cleaned_data
