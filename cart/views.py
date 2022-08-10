from django.shortcuts import render, redirect
from .models import cartlist
from mensapp.models import *
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import updatstatusform
from django.db.models import Q
from datetime import date, datetime
import datetime


# Create your views here.
def mycart(request):
    obj = cartlist.objects.filter((~Q(status='reject')),(~Q(status='final')), cuser__id=request.user.id).order_by('id')
    return render(request, 'mycart.html', {'ctr': obj})


def addtocart(request, product_id):
    url = request.META.get('HTTP_REFERER')
    data = cartlist()
    data.ip = request.META.get('REMOTE_ADDR')
    data.cproduct_id = product_id
    data.cuser_id = request.user.id
    data.save()
    data1 = tmens.objects.get(id=data.cproduct_id)
    data1.cartflag = True
    data1.save()
    # obj=cartlist.objects.get
    return redirect(url)


def remove(request, did):
    url = request.META.get('HTTP_REFERER')
    obj = cartlist.objects.get(id=did)
    data1 = tmens.objects.get(id=obj.cproduct_id)
    data1.cartflag = False
    data1.save()
    obj.delete()
    return redirect(url)


def updatestatus(request, uid):
    url = request.META.get('HTTP_REFERER')
    obj1 = cartlist.objects.get(id=uid)
    form = updatstatusform(request.POST or None, instance=obj1)
    if form.is_valid():
        form.save()
        return redirect(mycart)
    return render(request, 'updatstatus.html', {'obj1': obj1, 'form': form})


def rfgallery(request,rfstatus):
    lists = cartlist.objects.filter(status=rfstatus)
    return render(request, 'rejectfinalgllry.html', {'lst': lists,'rf':rfstatus})

# def finalgallery(request):
#     lists = cartlist.objects.filter(status='final')
#     return render(request, 'rejectfinalgllry.html', {'lst': lists})


def allcart(request):
    obj = cartlist.objects.all()
    for i in obj:
        old = i.added_at
        new = date.today()
        date_delta = new - old
        number_of_days = date_delta.days
        i.tilldate = number_of_days
        i.save()
    obj1=cartlist.objects.filter((~Q(status='reject')),(~Q(status='final')))
    return render(request, 'allcart.html', {'crt': obj1})

    # # obj1 = cartlist.objects.get(id=3)
    # clr = None
    # dic = {}
    # for i in obj:
    #     print(i.id)
    #     olddate = i.added_at
    #     currentdate = date.today()
    #     date_delta = currentdate - olddate
    #     number_of_days = date_delta.days
    #     print(number_of_days)
    #     dic[i]=number_of_days
    #     if number_of_days == 4:
    #         print('red')
    #         clr = 'indicator red'
    #
    #     elif number_of_days == 1:
    #         print('green')
    #         clr = 'indicator green'
    #     else:
    #         print('yello')
    #         clr = 'indicator yellow'

    # oldate=obj1.added_at
    # print(oldate)
    # crndate=date.today()
    # print(crndate)
    #
    # date_delta=crndate-oldate
    # number_of_days = date_delta.days
    # print(number_of_days)
    # clr = 'indicator offline'
