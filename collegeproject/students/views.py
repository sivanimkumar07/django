from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def student_list(request, message):

    students = [
        'Rahul',
        'Anu',
        'Siva'
    ]

    return render(
        request,
        'students/student_list.html',
        {
            'students': students,
            'message': message
        }
    )