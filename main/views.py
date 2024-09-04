from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306215816',
        'name': 'Arya Raditya Kusuma',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
