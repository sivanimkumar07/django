from django.shortcuts import render
from .forms import RegistrationForm


def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["full_name"]

            return render(
                request,
                "registrationapp/success.html",
                {"name": name}
            )

    else:
        form = RegistrationForm()

    return render(
        request,
        "registrationapp/index.html",
        {"form": form}
    )