from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        username_is = "Delroy Brown"
        context = {"username_is": username_is}
    else:
        context = {"username_is": "Stranger Danger!"}
    template = 'base.html'
    return render(request, template, context)
