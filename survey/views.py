from django.shortcuts import render


def home(request):

    if request.method == 'POST':
        print '@' + request.POST['twitter']

    context = {

    }
    return render(request, "home.html", context)


def finished(request):

    context = {

    }
    return render(request, "finished.html", context)