from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import UserRegistrationForm


def user_registration(request):
    """User Registration View"""

    # If the form is submitted we check if the inputs are valid then
    # proceed to allow the user to login, otherwise present them with
    # the registration form.
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("user_auth:login")
            )

    else:
        form = UserRegistrationForm()

    # Passing through the form as context
    context = {"form": form}
    return render(request, "authentication/registration.html", context)
