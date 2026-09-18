from django.shortcuts import render

def teacher_list(request, message):

    teachers = [
        'John',
        'Mary',
        'David'
    ]

    return render(
        request,
        'teachers/teacher_list.html',
        {
            'teachers': teachers,
            'message': message
        }
    )