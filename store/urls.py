from . import views
from django.urls import  path

urlpatterns = [
     path('',views.home,name='home'),
     path('search/',views.search,name='search'),
     path('cart/place-order.html',views.checkout,name='checkout'), # sample for demo
]
