"""
Ref: https://stackoverflow.com/questions/32860296/how-do-i-extend-usercreationform-to-include-email-field/53716907
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """User Registration Form Child Model"""

    # Declaring first name field
    first_name = forms.CharField(max_length=100, required=True)

    class Meta:
        """Here we extend the parent UserCreationForm and set the fields
        we need for the registration form"""
        model = User
        fields = ("username", "first_name", "password1", "password2")

    def save(self, commit=True):
        """Overwrite the save form function to include the additional
          fields"""
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        return user
