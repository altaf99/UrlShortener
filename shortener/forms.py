from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import URL


class ShortUrlForm(forms.ModelForm):

    class Meta:
       fields = ("full_url",)
       model = URL