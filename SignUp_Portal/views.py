from urllib import request
from django.shortcuts import render
from .forms import SignUpForm,UserCreationForm

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid :
        pass
    else:
        form = SignUpForm()

    context = {
        "form" : form
    }
    return render(request, "signup.html", context)