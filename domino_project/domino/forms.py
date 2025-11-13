from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from domino.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'profile_image', 'preferred_store', 'subscribe_promos']
        widgets = {
        'address': forms.Textarea(attrs={'rows':3}),
}


# Optional: a combined simple form for front-end validation (JS can use this)
class ProfileSettingsForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    preferred_store = forms.CharField(required=False)
    subscribe_promos = forms.BooleanField(required=False)
    profile_image = forms.ImageField(required=False)