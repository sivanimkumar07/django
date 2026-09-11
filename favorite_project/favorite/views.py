from django.shortcuts import render

def home(request):
    return render(request, "favorite/index.html")


def result(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")

        return render(request, "favorite/result.html", {
            "name": name,
            "color": color,
            "form_data": request.POST
        })
