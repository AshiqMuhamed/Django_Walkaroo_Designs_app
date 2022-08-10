from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('mycart',views.mycart,name='mycart'),
    path('addtocart/<int:product_id>/',views.addtocart,name='addtocart'),
    path('remove/<int:did>',views.remove,name='remove'),
    path('updatestatus/<int:uid>',views.updatestatus,name='updatestatus'),
    path('rfgallery/<str:rfstatus>',views.rfgallery,name='rfgallery'),
    # path('finalgallery',views.finalgallery,name='finalgallery'),
    path('allcart',views.allcart,name='allcart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)