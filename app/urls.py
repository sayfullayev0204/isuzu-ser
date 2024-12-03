from django.urls import path
from .views import home,about,custom,part,dmax

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('custom/', custom, name='custom'),
    path('part/', part, name='part'),
    path('dmax/', dmax, name='dmax'),
]