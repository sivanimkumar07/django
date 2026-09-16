from django.shortcuts import render
from .forms import MovieForm

def movie_form(request):

    if request.method == "POST":

        form = MovieForm(request.POST)

        if form.is_valid():

            movie = form.save()

            return render(
                request,
                "movieapp/success.html",
                {
                    "movie_name": movie.movie_name,
                    "year": movie.release_year
                }
            )

    else:
        form = MovieForm()

    return render(
        request,
        "movieapp/index.html",
        {"form": form}
    )