from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    return render(request,"./master/index.html")

def exit(request):
    logout(request)
    return redirect("/")
