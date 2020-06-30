from django import forms
from homepage.models import Registration
#Login and Registration form


class LogForm(forms.Form):
    Username = forms.CharField(max_length=30)
    Password = forms.CharField(widget=forms.PasswordInput,min_length=8)

    class Meta:
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        widgets={
            'Password': forms.PasswordInput(),
        }
        fields='__all__'
