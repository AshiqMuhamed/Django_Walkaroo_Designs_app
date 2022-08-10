from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from cart.models import cartlist
from .models import tmens, ratingreview
from django.views.generic import DetailView, UpdateView, DeleteView
from .form import ReviewForm
from django.http import HttpResponseRedirect
from django.db.models import Avg
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'home.html')


def adminpannel(request):
    return render(request, 'adminhome.html')


def additem(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        img = request.FILES.get('imag')
        mc = request.POST.get('maincategory')
        sc = request.POST.get('category')
        db = request.POST.get('dby')
        s = tmens(name=n, img=img, category=sc, maincategory=mc, designedby=db)
        s.save()
        return render(request, 'additem.html')
    else:
        return render(request, 'additem.html')


def users(request):
    usr = User.objects.all().order_by('-id')
    return render(request, 'users.html', {'user': usr})


class delete(DeleteView):
    model = tmens
    template_name = 'confirmdelete.html'
    context_object_name = 'tmen'
    success_url = reverse_lazy('editdelete')


def editdelete(request):
    # FOR MENS EDIT/DELETE
    mf = tmens.objects.all().filter(category='formal', maincategory='mens').order_by('-id')
    mc = tmens.objects.all().filter(category='casual', maincategory='mens').order_by('-id')
    ms = tmens.objects.all().filter(category='semi-formal', maincategory='mens').order_by('-id')
    # FOR LADIES EDIT/DELETE
    lf = tmens.objects.all().filter(category='formal', maincategory='ladies').order_by('-id')
    lc = tmens.objects.all().filter(category='casual', maincategory='ladies').order_by('-id')
    ls = tmens.objects.all().filter(category='semi-formal', maincategory='ladies').order_by('-id')
    # FOR GIRLS EDIT/DELETE
    gf = tmens.objects.all().filter(category='formal', maincategory='girls').order_by('-id')
    gc = tmens.objects.all().filter(category='casual', maincategory='girls').order_by('-id')
    gs = tmens.objects.all().filter(category='semi-formal', maincategory='girls').order_by('-id')
    # FOR BOYS EDIT/DELETE
    bf = tmens.objects.all().filter(category='formal', maincategory='boys').order_by('-id')
    bc = tmens.objects.all().filter(category='casual', maincategory='boys').order_by('-id')
    bs = tmens.objects.all().filter(category='semi-formal', maincategory='boys').order_by('-id')
    # FOR KIDS EDIT/DELETE
    kf = tmens.objects.all().filter(category='formal', maincategory='kids').order_by('-id')
    kc = tmens.objects.all().filter(category='casual', maincategory='kids').order_by('-id')
    ks = tmens.objects.all().filter(category='semi-formal', maincategory='kids').order_by('-id')
    return render(request, 'viewfordelete.html', {'menf': mf, 'menc': mc, 'mens': ms,
                                                  'ladif': lf, 'ladic': lc, 'ladis': ls,
                                                  'boyf': bf, 'boyc': bc, 'boys': bs,
                                                  'girlf': gf, 'girlc': gc, 'girls': gs,
                                                  'kidf': kf, 'kidc': kc, 'kids': ks, })


def mainviews(request, ctg):
    objf = tmens.objects.all().filter(category='formal', maincategory=ctg, cartflag=False).order_by('-id')
    objc = tmens.objects.all().filter(category='casual', maincategory=ctg, cartflag=False).order_by('-id')
    objs = tmens.objects.all().filter(category='semi-formal', maincategory=ctg, cartflag=False).order_by('-id')
    return render(request, 'mainview.html', {'tmenf': objf, 'tmenc': objc, 'tmens': objs, 'ctgry': ctg})


def submit_review(request, product_id):
    objtmen = tmens.objects.get(id=product_id)
    if request.method == "POST":
        rr = ratingreview.objects.all()
        try:
            reviews = ratingreview.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            avrg = ratingreview.objects.filter(product__id=product_id).aggregate(Avg('rating'))
            print(avrg['rating__avg'])
            a = ("{:.1f}".format(avrg['rating__avg']))
            print(a)
            objtmen.rating = a
            objtmen.save()
            # tmens.save(self)
            # print(tmens.rating)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except ratingreview.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ratingreview()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                avrg = ratingreview.objects.filter(product__id=product_id).aggregate(Avg('rating'))
                print(avrg['rating__avg'])
                a = ("{:.1f}".format(avrg['rating__avg']))
                print(a)
                # objtmen.objects.update(rating=avrg['rating__avg'])
                objtmen.rating = a
                objtmen.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# class detail(DetailView):
#     model = tmens
#     template_name = 'ratingdetail.html'
#     context_object_name = 'tmen'

def detail(request, did):
    dt = tmens.objects.get(id=did)
    rvw = ratingreview.objects.filter(product_id=did)
    return render(request, 'ratingdetail.html', {'tmen': dt, 'rview': rvw})
