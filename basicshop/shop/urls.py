from django.contrib import admin
from django.urls import path
from .views import Index , Signup, Login, Cart, CheckOut, OrderView, store, logout, clients, searchBar, sell
from .auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup.html', Signup.as_view(), name='signup'),
    path('login.html', Login.as_view(), name='login'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart.html', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    

    path('clients.html', clients , name='clients'),
    path('search', searchBar, name='search'),
    path('sell.html', sell, name='sell')
]

