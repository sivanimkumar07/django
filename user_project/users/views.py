from django.shortcuts import render

def home(request):
    return render(request, "users/index.html")


def result(request):
    username = request.GET.get("username")

    return render(request, "users/result.html", {
        "username": username,
        "form_data": request.GET
    })
