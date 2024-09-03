from django.urls import path
from .views import *

urlpatterns = [
    path('', profil, name='profil'),
    path('index/', index, name='index'),
    path('creatuser/', creatuser, name='creatuser'),
    path('detail/<int:pk>', detail, name='detail'),
    path('qarz_delete/<int:pk>', qarz_delete, name='qarz_delete'),
    
    path('profil2/', profil2, name='profil2'),
    path('index2/', index2, name='index2'),
]