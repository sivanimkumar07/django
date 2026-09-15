from django.shortcuts import render
from .forms import ContactForm


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            return render(
                request,
                "contactapp/success.html",
                {"name": contact.full_name}
            )

    else:
        form = ContactForm()

    return render(
        request,
        "contactapp/index.html",
        {"form": form}
    )
