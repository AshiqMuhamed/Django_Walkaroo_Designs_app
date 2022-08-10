from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('adminpannel', views.adminpannel, name='adminpannel'),
    path('additem', views.additem, name='additem'),
    path('users', views.users, name='users'),
    path('editdelete', views.editdelete, name='editdelete'),
    path('delete/<int:pk>', views.delete.as_view(), name='delete'),
    path('mainviews/<str:ctg>', views.mainviews, name='mainviews'),# for viewing design based category
    path('detail/<int:did>', views.detail, name='detail'),
    path('submit_review/<int:product_id>/',views.submit_review,name='submit_review'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
