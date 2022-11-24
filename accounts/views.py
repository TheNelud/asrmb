from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
def base(request):
    return render(request,"base.html")


# class SignUp(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")