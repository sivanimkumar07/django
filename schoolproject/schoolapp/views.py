from django.shortcuts import render

def home(request):

    students = [
        'Rahul',
        'Anu',
        'Siva'
    ]

    return render(
        request,
        'home.html',
        {'students': students}
    )


def result(request, name):

    return render(
        request,
        'result.html',
        {'name': name}
    )