from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from mensapp.views import users
from .form import resetpasswordform


# Create your views here.
def register(request):

    if request.method == "POST":
        uname = request.POST['username']
        admn = request.POST['yes_no']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        if pwd1 != pwd2:
            messages.info(request, 'password mismartch')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.info(request, 'user already exist')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'mail already exist')
            return redirect('register')
        else:
            user = User.objects.create_user(username=uname, is_superuser=admn, is_staff=admn, first_name=fname, last_name=lname, email=email,
                                            password=pwd1)
            user.save()
            return redirect(users)
    else:
        return render(request, 'register.html')

    # return render(request,"register.html")


def login(request):
    # url=request.META.get('HTTP_REFERER')
    if request.method == "POST":
        usname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=usname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalied details')
            return redirect('login')
    else:
        return render(request, "login.html")


#
def logout(request):
    url=request.META.get('HTTP_REFERER')
    auth.logout(request)
    return redirect(url)

#
def deleteuser(request,uid):
    usr=User.objects.get(id=uid)
    usr.delete()
    return redirect(users)

