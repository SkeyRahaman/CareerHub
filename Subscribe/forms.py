from django import forms
from .models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeModelForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields='__all__'
        labels = {
            'first_name' : _('Enter First Name.'),
            'last_name' : _('Enter Last Name.'),
            'email' : _('Enter Email'),
        }