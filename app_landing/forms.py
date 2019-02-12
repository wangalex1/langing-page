from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Messages


def ValidateEmail(email):
    try:
        validate_email(email)
        return email
    except ValidationError:
        raise ValidationError('Email format is incorrect')


class MessagesForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ['email', 'name', 'message']

    def clean_email(self):
        email = ValidateEmail(self.cleaned_data.get("email"))
        return email

