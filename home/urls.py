

from django.urls import path
from .views import Home
from django.conf import settings
from django.conf.urls.static import static
from .views import services, contactus, gallery
from django.conf.urls.static import static
from . import views
from .views import dynamic_home


urlpatterns = [
    path('',Home.as_view(),name="home"),
    # path('', views.dynamic_home, name='dynamic_home'),
    path('services/', services, name='services'),
    path('contactus/', contactus, name='contactus'),
    path('gallery/',gallery,name='gallery'),

]
